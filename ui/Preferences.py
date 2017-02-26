from PyQt5.QtCore import QSysInfo
from PyQt5.QtCore import Q_FLAGS
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog

from core.Constants import *
from core.Settings import Settings, SettingsUtil
from ui.Arguments import Arguments
from ui.Ui_Settings import Ui_Settings


class PlayerSettings(QDialog):

    def __init__(self, flags, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        self.ui = Ui_Settings()

        # setup basic window decoration

        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(RES_PREF_IC))
        self.setWindowTitle(RES_PREF_TITLE)

        # qt connects

        self.ui.browse.clicked.connect(self.open_browse)
        self.ui.save.clicked.connect(self.saveAndClose)
        self.ui.unsupported_check.toggled.connect(self.toggle_support)
        self.ui.button_settings.clicked.connect(self.openArgumentSettings)

        # get the settings instance
        self.settings = Settings.getInstance()

        # populate class members
        self.path = self.settings.value(SETT_PATH, SETT_DEFAULT)
        self.argumentsMain = self.settings.value(SETT_ARGS_MAIN, ARGS_VLC_DEF)
        self.argumentsSubtitle = self.settings.value(SETT_ARGS_SUB, ARGS_SUB_VLC_DEF)

        # set support flag, 1 is off, 2 is on
        support = self.settings.value(SETT_UNSUP, "1")
        self.otherPlayerSupport = "1" not in support

        # populate the UI
        self.ui.path.setText(self.path)
        self.ui.unsupported_check.setChecked(self.otherPlayerSupport)

        # toggle settings edibility on the UI
        # according to the support flag
        self.toggle_support(self.otherPlayerSupport)

    def openArgumentSettings(self):
        self.save_settings(False)
        self.args = Arguments(flags=Q_FLAGS())
        self.args.show()

    def toggle_support(self, state):

        # update the UI according the config file

        self.otherPlayerSupport = state
        self.updateUiWithStates()

    def updateUiWithStates(self):
        self.ui.unsupported_check.setChecked(self.otherPlayerSupport)
        self.ui.desc.setEnabled(self.otherPlayerSupport)
        self.ui.button_settings.setEnabled(self.otherPlayerSupport)

    def save_settings(self, close=True):

        # if we support 3rd party players,
        # set all the parameters from the
        # config file
        if self.otherPlayerSupport:
            self.settings.setValue(SETT_UNSUP, "2")
            self.settings.setValue(SETT_PATH, self.path)
            if close: self.close()
        # else, hard reset to defaults,
        # but leave the path intact
        else:
            self.settings.setValue(SETT_PATH, self.path)
            self.writeDefaults()
            if close: self.close()

    def open_browse(self):
        if "windows" in QSysInfo.productType():
            self.path = QFileDialog.getOpenFileName(options=QFileDialog.ReadOnly, filter="Players (*.exe)")[0]
        else:
            self.path = QFileDialog.getOpenFileName(options=QFileDialog.ReadOnly, filter="Players (*.*)")[0]
        self.ui.path.setText(self.path)

    def writeDefaults(self):
        SettingsUtil.writeList(self.settings, ARR_ARGS_DEF, ARR_ARGS)

    def saveAndClose(self):
        self.save_settings(True)


