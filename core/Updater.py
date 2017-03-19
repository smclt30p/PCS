import demjson
import requests
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

from core.Constants import *

class Updater(QThread):

    updateAvailable = pyqtSignal(int)

    def run(self):

        request = requests.get(PCS_UPDATE_DEFAULT_ENDPOINT)

        if request.status_code != 200:
            return

        json = demjson.JSON()
        data = json.decode(request.text)

        if data["last_version"] > PCS_VERSION or data["last_version"] < PCS_VERSION:
            self.updateAvailable.emit(data["last_version"])

