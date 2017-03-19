import subprocess
import sys
import tarfile

import demjson
import requests
from PyQt5.QtCore import QDir
from PyQt5.QtCore import QThread
from PyQt5.QtCore import Q_FLAGS
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from updater.Ui_Updater import Ui_Updater


def main():

    app = QApplication(sys.argv)

    window = MainWindow(app=app, flags=Q_FLAGS())
    window.show()



    exit(app.exec_())


class MainWindow(QDialog):

    def __init__(self, flags,app, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        self.ui = Ui_Updater()
        self.ui.setupUi(self)
        self.app = app

        self.ui.title.setText("Updating PCS to " + sys.argv[1])
        self.setWindowIcon(QIcon("ui/res/icon.png"))
        self.setWindowTitle("Standalone Updater - PCS")

        self.updater = Updater()

        self.updater.updateTitle.connect(self.updateTitle)
        self.updater.step1.connect(self.step1)
        self.updater.step2.connect(self.step2)
        self.updater.complete.connect(self.complete)

        self.updater.start()

        self.ui.step1.setEnabled(False)
        self.ui.step2.setEnabled(False)

    def updateTitle(self, title):
        self.ui.title.setText(title)

    def step1(self):
        self.ui.step1.setEnabled(True)
        self.ui.step2.setEnabled(False)

    def step2(self):
        self.ui.step1.setEnabled(False)
        self.ui.step2.setEnabled(True)

    def complete(self):

        self.ui.title.setText("Upgrade complete!")
        self.ui.step1.setEnabled(False)
        self.ui.step2.setEnabled(False)

        try:
            subprocess.Popen(["pythonw", "ui/Main.py"])
        except BaseException as e:
            box = QMessageBox()
            box.critical(self, "Failed to launch PCS!", "PCS Failed to launch, please launch manually!", QMessageBox.Close)

        sys.exit(0)


class Updater(QThread):

    UPDATE_URL = "https://raw.githubusercontent.com/smclt30p/pcs_update/latest-stable/{}_{}.tar.xz"
    PATHS_URL = "https://raw.githubusercontent.com/smclt30p/pcs_update/latest-stable/paths.json"

    updateTitle = pyqtSignal(str)
    step1 = pyqtSignal()
    step2 = pyqtSignal()
    complete = pyqtSignal()

    def run(self):

        try:

            # Enumerate current version
            # Find update path
            # update
            # if not latest, repeat, else complete

            self.updateTitle.emit("Fetching upgrade paths...")

            currentVersion = sys.argv[1]
            updatePaths = self.getUpdatePaths()

            nextVersion = None

            while True:

                for update in updatePaths:
                    if currentVersion in update:
                        nextVersion = update[currentVersion]

                if nextVersion is None:
                    self.complete.emit()
                    break

                self.updateTitle.emit("Updating from {} to {}".format(currentVersion, nextVersion))

                self.step1.emit()

                data = requests.get(self.UPDATE_URL.format(currentVersion, nextVersion))
                path = "{}/{}_{}.tar.xz".format(QDir.tempPath(), currentVersion, nextVersion)

                file = open(path, "wb+")

                file.write(data.content)
                file.close()

                self.step2.emit()

                tar = tarfile.open(path, "r:xz")
                tar.extractall(".")

                currentVersion = nextVersion
                nextVersion = None

            self.complete.emit()

        except BaseException as e:
            self.updateTitle.emit("UPDATE FAILED!")
            print("ERROR! " + str(e))

    def getUpdatePaths(self):
        # todo: handle no network
        data = requests.get(self.PATHS_URL)
        json = demjson.JSON()
        return json.decode(data.text)



if __name__ == "__main__":
    main()