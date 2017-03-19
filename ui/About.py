from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog

from ui.Ui_AboutDialog import Ui_AboutDialog
from core.Constants import *

class About(QDialog):

    def __init__(self, flags, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("ui/res/icon.png"))
        self.ui.bg.setPixmap(QPixmap("ui/res/logo.png"))
        self.ui.version_string.setText(PCS_VERSION_STRING)
