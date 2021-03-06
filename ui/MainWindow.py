import subprocess

from PyQt5 import QtCore
from PyQt5.QtCore import QDir
from PyQt5.QtCore import pyqtSlot, Q_FLAGS
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTreeWidgetItem
from math import floor

from core.Constants import *
from core.Player import MediaPlayer
from core.Updater import Updater
from core.Workers import MetadataWorker, SubtitleWorker
from core.Workers import SearchWorker
from core.plugins.PluginLoader import PluginLoader
from core.plugins.PluginMenu import PluginMenu
from ui.About import About
from ui.Preferences import PlayerSettings
from ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):

    COL_TITLE = 0
    COL_LEN = 1
    COL_PLUGIN = 2
    COL_RATING = 3

    workers = []

    def __init__(self, app, flags, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.disableMovieInfo()

        # the inner objects

        self.playIcon = QIcon(RES_SETTINGS_ICON)
        self.icon = QIcon(RES_PROGRAM_ICON)
        #self.worker = SearchWorker()
        self.metadataWorker = MetadataWorker()
        self.subtitleWorker = SubtitleWorker()
        self.player = MediaPlayer()


        # decorate ui

        self.ui.actionVideo_player.setIcon(self.playIcon)
        self.setWindowIcon(self.icon)
        self.setWindowTitle(STRING_PROGRAM_NAME)

        # qt connections

        self.ui.movie_tree.itemDoubleClicked.connect(self.onMovieDoubleClick)
        self.ui.movie_tree.header().resizeSection(0, 300)
        self.ui.play_button.clicked.connect(self.onPlayButtonClicked)
        self.ui.actionVideo_player.triggered.connect(self.openPreferences)
        self.ui.search_bar.returnPressed.connect(self.onSearchReturnPressed)
        self.ui.actionAbout.triggered.connect(self.openAbout)

        self.metadataWorker.fetchError.connect(self.showError)
        self.metadataWorker.done.connect(self.onMetadataReceive)
        self.subtitleWorker.startPlayerCallback.connect(self.startPlayer)
        self.player.playerError.connect(self.showErrorDialog)
        self.player.playerClosed.connect(self.onPlayerClosed)

        self.ui.movie_tree.setSortingEnabled(True)

        self.updater = Updater()
        self.updater.updateAvailable.connect(self.updateAvailable)
        self.updater.start()


    def updateAvailable(self, version):

        if version < PCS_VERSION:
            self.ui.status_bar.setText("WARNING: RUNNING DEVELOPMENT BUILD !!!")
        else:
            update_str = str(version)
            self.ui.status_bar.setText("Update available: PCS v{}.{}".format(update_str[0], update_str[1]))

            box = QMessageBox()
            reply = box.question(self, "Update available!", "Do you want to update PCS?", QMessageBox.Yes, QMessageBox.Close)

            if reply == QMessageBox.Yes:
                try:
                    subprocess.Popen(["python", "updater/StandaloneUpdater.py", str(PCS_VERSION)])
                    self.app.exit(0)
                except BaseException as e:
                    self.showErrorDialog(str(e))


            else:
                return

    def openAbout(self):
        self.about = About(flags=Q_FLAGS())
        self.about.show()


    def showEvent(self, *args, **kwargs):

        self.menu = PluginMenu()
        self.menu.constructMenu(self.ui.menuPlugins)

    def show(self):
        super().show()

        try:
            self.plugins = PluginLoader.getLoadedPlugins()
            self.ui.status_bar.setText("Loaded {} plugin(s)".format(len(self.plugins)))
        except BaseException as e:
            self.showError("Error loading plugins: " + str(e))

    def onPlayerClosed(self):
        self.ui.centralwidget.setEnabled(True)
        self.ui.status_bar.setText("READY")

    def openPreferences(self):
        self.settings = PlayerSettings(flags=Q_FLAGS())
        self.settings.show()

    @QtCore.pyqtSlot(name="clicked")
    def onPlayButtonClicked(self):

        if len(self.streams) == 0:
            self.showWarning("No streams found, broken plugin?")
            return

        subtitlePath = None

        if self.ui.subtitle_combo.currentIndex() == SUBTITLES_DISABLED:

            self.startPlayer(subtitlePath)

        elif self.ui.subtitle_combo.currentIndex() == SUBTITLES_CUSTOM:

            subtitlePath = QFileDialog.getOpenFileName(caption="Open subtitle file",
                                                       filter="Subtitles (*.srt)",
                                                       options=QFileDialog.ReadOnly)

            self.startPlayer(QDir.toNativeSeparators(subtitlePath[0]))

        else:

            self.disableMovieInfo()
            self.ui.status_bar.setText("DOWNLOADING SUBTITLE")
            self.subtitleWorker.setUrl(self.subtitles[self.ui.subtitle_combo.currentIndex() - 2].getSource())

            # this calls back startPlayer below with the subtitles
            self.subtitleWorker.start()

    def startPlayer(self, subtitlePath):

        link = self.streams[self.ui.quality_combo.currentIndex()].getSource()

        self.enableMovieInfo()
        self.ui.centralwidget.setEnabled(False)
        self.ui.status_bar.setText("PLAYING MOVIE")
        self.player.play(link, subtitlePath)

    def onMetadataReceive(self, playable):

        self.ui.quality_combo.clear()
        self.ui.subtitle_combo.clear()

        drawable = playable.getPoster()
        description = playable.getDescription()

        self.enableMovieInfo()

        try:

            if drawable is not None:
                self.ui.poster.setPixmap(playable.getPoster())
            if description is not None and len(description) != 0:
                self.ui.description.setText(playable.getDescription())
        except BaseException as e:
            print(str(e))


        self.streams = playable.getDataStreams()
        self.subtitles = playable.getSubtitleStreams()

        for stream in self.streams:
            self.ui.quality_combo.addItem(stream.getLabel())

        self.ui.subtitle_combo.addItem("Disabled")
        self.ui.subtitle_combo.addItem("Custom (from file)")

        for subtitle in self.subtitles:
            self.ui.subtitle_combo.addItem(subtitle.getLabel())

        # HACK: self.item comes from onMovieDoubleClick to avoid all
        # the QTreeWidget crap

        movieLength = playable.getPlayableLength()
        movieLengthString = "Unknown"

        if movieLength == -1:
            movieLengthString = "LIVE"
        elif movieLength != 0:
            movieLengthString = str("{} min".format(floor(movieLength / 60)))

        self.item.setText(self.COL_LEN, movieLengthString)

    def onMovieDoubleClick(self, item, id_):

        self.item = item

        if item.playable.isFetched():
            self.onMetadataReceive(item.playable)
            return


        self.disableMovieInfo()
        self.ui.movie_title.setText(item.playable.getTitle())

        self.metadataWorker.setPlayable(item.playable)
        self.metadataWorker.start()

    def onSearchReturnPressed(self):

        self.ui.movie_tree.clear()
        self.workers.clear()

        self.ui.centralwidget.setEnabled(False)
        self.ui.status_bar.setText("SEARCHING...")

        count = 0

        for plugin in self.plugins:

            if not plugin.isActive():
                continue

            worker = SearchWorker()
            worker.addToTree.connect(self.displaySearchResults)
            worker.searchError.connect(self.showError)
            self.workers.append(worker)

            worker.setQuery(self.ui.search_bar.text())
            worker.setPlugin(plugin)
            worker.start()

        if len(self.workers) == 0:
            self.ui.status_bar.setText("READY")
            self.ui.centralwidget.setEnabled(True)

    @pyqtSlot(dict, name="tree")
    def displaySearchResults(self, results):

        try:

            worker = self.workers.pop()
            worker.wait()

        except IndexError:
            return

        if len(self.workers) == 0:
            self.ui.status_bar.setText("READY")
            self.ui.centralwidget.setEnabled(True)

        for i in range(len(results)):

            parentId = results[i].getParentPluginId()
            plugin = "Unknown"

            for plugin in self.plugins:

                if parentId == plugin.getPluginId():
                    plugin = plugin.getPluginName()
                    break

            item = QTreeWidgetItem()
            item.setText(self.COL_TITLE, " {}".format(results[i].getTitle()))
            item.setText(self.COL_PLUGIN, plugin)
            item.setText(self.COL_LEN, "Unknown")
            item.id = i
            item.playable = results[i]

            brush = item.background(0)
            brush.setColor(QColor("#ffff0000"))
            item.setBackground(0, brush)

            self.ui.movie_tree.addTopLevelItem(item)

    def showError(self, message):

        for worker in self.workers:
            worker.terminate()

        self.workers.clear()

        self.showErrorDialog(message)
        self.ui.movie_tree.clear()
        self.ui.status_bar.setText("ERROR")
        self.ui.centralwidget.setEnabled(True)
        self.enableMovieInfo()

    def showErrorDialog(self, message):
        self.error = QMessageBox()
        self.error.setIcon(QMessageBox.Critical)
        self.error.setWindowTitle("Search error")
        self.error.setWindowIcon(self.icon)
        self.error.setText(message)
        self.menu.constructMenu(self.ui.menuPlugins)
        self.error.show()

    def fetchMetadata(self, url, siteurl):
        self.metadataWorker.setURL(url, siteurl)
        self.metadataWorker.start()

    def disableMovieInfo(self):
        self.ui.poster.setEnabled(False)
        self.ui.quality_combo.setEnabled(False)
        self.ui.play_button.setEnabled(False)
        self.ui.subtitle_combo.setEnabled(False)
        self.ui.movie_title.setEnabled(False)
        self.ui.description.setEnabled(False)

    def enableMovieInfo(self):
        self.ui.poster.setEnabled(True)
        self.ui.quality_combo.setEnabled(True)
        self.ui.play_button.setEnabled(True)
        self.ui.subtitle_combo.setEnabled(True)
        self.ui.movie_title.setEnabled(True)
        self.ui.description.setEnabled(True)

    def showWarning(self, message):

        self.warning = QMessageBox()
        self.warning.setIcon(QMessageBox.Warning)
        self.warning.setWindowIcon(self.icon)
        self.warning.setText(message)
        self.warning.setWindowTitle("No streams found")
        self.warning.show()


