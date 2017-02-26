import subprocess

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

from core.Constants import *
from core.Settings import Settings, SettingsUtil


class MediaPlayer(QThread):

    playerClosed = pyqtSignal()
    playerError = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.settings = Settings.getInstance()

    def play(self, link, subtitle=None):
        self.link = link
        self.subtitle = subtitle
        self.start()

    def run(self):

        playerPath = self.settings.value(SETT_PATH, SETT_DEFAULT)

        if len(playerPath) is 0:

            self.playerError.emit("The player has not been configured. Please do that now. (Edit > Preferences)")
            self.playerClosed.emit()
            return

        args = [playerPath]
        temp = SettingsUtil.readList(self.settings, ARR_ARGS)

        for i in range(len(temp)):
            if CONST_SUB_PARAM in temp[i] and self.subtitle is None:
                continue
            args.append(temp[i])

        for i in range(len(args)):

            if CONST_SUB_PARAM in args[i]:
                args[i] = args[i].replace(CONST_SUB_PARAM, self.subtitle)
            if CONST_URL_PARAM in args[i]:
                args[i] = args[i].replace(CONST_URL_PARAM, self.link)

        subprocess.run(args)
        self.playerClosed.emit()