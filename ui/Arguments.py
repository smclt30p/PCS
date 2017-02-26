from PyQt5.QtCore import QDir
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTreeWidgetItem

from core.Constants import *
from core.Settings import Settings, SettingsUtil
from ui.Ui_Arguments import Ui_Arguments


class Arguments(QDialog):

    PRESETS = ["None",
               "VLC Media Player",
               "Windows Media Player",
               "Media Player Classic - Home Cinema (K-Lite)",
               "mpv"]

    PRESET_NONE = 0
    PRESET_VLC = 1
    PRESET_WMP = 2
    PRESET_MPC = 3
    PRESET_MPV = 4

    PRESET_VLC_DATA = ["%URL%", "--sub-file=%SUB%"]
    PRESET_WMP_DATA = ["%URL%"]
    PRESET_MPC_DATA = ["%URL%", "/sub", "%SUB%"]
    PRESET_MPV_DATA = ["%URL%", "--sub-file=%SUB%"]

    def __init__(self, flags, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        self.ui = Ui_Arguments()
        self.ui.setupUi(self)

        self.setWindowTitle(REF_ARGS_TITLE)
        self.setWindowIcon(QIcon(RES_SETTINGS_ICON))

        self.ui.button_add.clicked.connect(self.insertIntoTree)
        self.ui.button_remove.clicked.connect(self.removeItemFromTree)
        self.ui.button_remove_all.clicked.connect(self.clearTree)
        self.ui.button_save.clicked.connect(self.flushArguments)
        self.ui.treeWidget.itemDelegate().closeEditor.connect(self.editorClosed)
        self.ui.preset_combo.currentIndexChanged.connect(self.setPresetData)

        for preset in self.PRESETS:
            self.ui.preset_combo.addItem(preset)

        self.settings = Settings.getInstance()

        self.args = SettingsUtil.readList(self.settings, ARR_ARGS)

        self.updateTreeFromData()

    def updateTreeFromData(self):

        self.ui.treeWidget.clear()

        for arg in self.args:
            item = QTreeWidgetItem()
            item.setText(0, arg)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.treeWidget.addTopLevelItem(item)

        self.updateResultString()

    def clearTree(self):
        self.ui.treeWidget.clear()
        self.updateResultString()

    def editorClosed(self, editor):
        self.updateResultString()

    def insertIntoTree(self):
        item = QTreeWidgetItem()
        item.setText(0, "Empty")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        currIndex = self.ui.treeWidget.currentIndex().row()
        if currIndex == -1:
            self.ui.treeWidget.addTopLevelItem(item)
        else:
            self.ui.treeWidget.insertTopLevelItem(currIndex + 1, item)

        self.updateResultString()

    def removeItemFromTree(self):
        self.ui.treeWidget.takeTopLevelItem(self.ui.treeWidget.currentIndex().row())
        self.updateResultString()

    def flushArguments(self):

        args = []
        size = self.ui.treeWidget.topLevelItemCount()

        for i in range(size):
           args.append(self.ui.treeWidget.topLevelItem(i).text(0))

        SettingsUtil.writeList(self.settings, args, ARR_ARGS)

        self.close()

    def updateResultString(self):

        res = QDir.toNativeSeparators(self.settings.value(SETT_PATH, "[player]")).split(QDir.separator())[-1]

        for i in range(self.ui.treeWidget.topLevelItemCount()):
            text = self.ui.treeWidget.topLevelItem(i).text(0)
            res = res + " " + text

        self.ui.result.setText(res)

    def setPresetData(self, index):

        if index == 0: return

        if index == self.PRESET_VLC:
            self.args = self.PRESET_VLC_DATA
            self.updateTreeFromData()

        if index == self.PRESET_WMP:
            self.args = self.PRESET_WMP_DATA
            self.updateTreeFromData()

        if index == self.PRESET_MPC:
            self.args = self.PRESET_MPC_DATA
            self.updateTreeFromData()

        if index == self.PRESET_MPV:
            self.args = self.PRESET_MPV_DATA
            self.updateTreeFromData()

