import requests
from PyQt5.QtCore import QDir
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

from core.plugins.Plugin import Playable, PluginException
from core.plugins.PluginLoader import PluginLoader


class SearchWorker(QThread):

    addToTree = pyqtSignal(list, name="tree")
    searchError = pyqtSignal(str, name="error")

    plugins = PluginLoader.getLoadedPlugins()

    def setQuery(self, query):
        self.query = query

    def setPlugin(self, plugin):
        self.plugin = plugin

    def run(self):

        results = []

        try:

            for playable in self.plugin.search(self.query):
                results.append(playable)

            self.addToTree.emit(results)

        except PluginException as e:
            self.searchError.emit(str(e))


class MetadataWorker(QThread):

    done = pyqtSignal(Playable)
    fetchError = pyqtSignal(str, name="error")

    plugins = PluginLoader.getLoadedPlugins()

    def setPlayable(self, playable):
        self.playable = playable

    def run(self):

        try:

            parentId = self.playable.getParentPluginId()

            for plugin in self.plugins:
                if plugin.getPluginId() == parentId:
                    plugin.fetchPlayableMetadata(self.playable)

            # load poster pixmap

            if self.playable.getPoster() != None:
                drawable = requests.get(self.playable.getPoster())
                pixmap = QPixmap()
                if pixmap.loadFromData(drawable.content):
                    self.playable.setPoster(pixmap)

            self.playable.setFetched(True)
            self.done.emit(self.playable)

        except BaseException as e:
            self.fetchError.emit(str(e))

class SubtitleWorker(QThread):

    startPlayerCallback = pyqtSignal(str)

    def setUrl(self, url):
        self.url = url

    def run(self):

        try:
            subPath = QDir.tempPath() + "/pcs_sub.srt"
            response = requests.get(self.url)

            if response.status_code != 200:
                print("failed to fetch titles, running")

            file = open(subPath, "wb")
            file.truncate()
            file.write(response.content)
            file.close()

            # hotfix: VLC does NOT like forward slashes in paths
            self.startPlayerCallback.emit(QDir.toNativeSeparators(subPath))

        except BaseException as e:
            print(str(e))
            self.startPlayerCallback.emit(None)