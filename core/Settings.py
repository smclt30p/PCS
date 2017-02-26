from PyQt5.QtCore import QSettings

from core.Constants import *


class Settings:

    instance = None

    def __init__(self):
        super().__init__()

    @staticmethod
    def getInstance():
        if Settings.instance is None:
            Settings.instance = QSettings(SETTINGS_FILE_NAME, QSettings.IniFormat)
        return Settings.instance

class SettingsUtil:

    @staticmethod
    def writeList(settings, data, dataName):

        settings.setValue(dataName + "_name", dataName)
        settings.setValue(dataName + "_len", len(data))

        for i in range(len(data)):
            settings.setValue(dataName + "_" + str(i), data[i])


    @staticmethod
    def readList(settings, name):

        data = []

        name = settings.value(name + "_name", "")
        if len(name) == 0: return data

        length = int(settings.value(name + "_len"))
        for i in range(length):
            data.append(settings.value(name + "_" + str(i)))

        return data
