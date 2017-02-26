# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\settings.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(536, 490)
        self.gridLayout_2 = QtWidgets.QGridLayout(Settings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(434, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.save = QtWidgets.QPushButton(Settings)
        self.save.setObjectName("save")
        self.gridLayout_2.addWidget(self.save, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Settings)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_executable = QtWidgets.QLabel(self.tab_2)
        self.label_executable.setObjectName("label_executable")
        self.verticalLayout.addWidget(self.label_executable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path = QtWidgets.QLineEdit(self.tab_2)
        self.path.setEnabled(True)
        self.path.setObjectName("path")
        self.horizontalLayout.addWidget(self.path)
        self.browse = QtWidgets.QPushButton(self.tab_2)
        self.browse.setMaximumSize(QtCore.QSize(32, 16777215))
        self.browse.setObjectName("browse")
        self.horizontalLayout.addWidget(self.browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unsupported_check = QtWidgets.QCheckBox(self.tab_2)
        self.unsupported_check.setObjectName("unsupported_check")
        self.horizontalLayout_2.addWidget(self.unsupported_check)
        self.button_settings = QtWidgets.QPushButton(self.tab_2)
        self.button_settings.setObjectName("button_settings")
        self.horizontalLayout_2.addWidget(self.button_settings)
        self.horizontalLayout_2.setStretch(0, 80)
        self.horizontalLayout_2.setStretch(1, 20)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.unsupported_disable = QtWidgets.QVBoxLayout()
        self.unsupported_disable.setObjectName("unsupported_disable")
        self.desc = QtWidgets.QLabel(self.tab_2)
        self.desc.setObjectName("desc")
        self.unsupported_disable.addWidget(self.desc)
        self.verticalLayout.addLayout(self.unsupported_disable)
        spacerItem1 = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 2)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Dialog"))
        self.save.setText(_translate("Settings", "Save"))
        self.label_executable.setText(_translate("Settings", "Executable"))
        self.path.setPlaceholderText(_translate("Settings", "Path to executable"))
        self.browse.setText(_translate("Settings", "..."))
        self.unsupported_check.setText(_translate("Settings", "Use unsupported player"))
        self.button_settings.setText(_translate("Settings", "Settings"))
        self.desc.setText(_translate("Settings", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Only VLC Media Player is supported officially.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Settings", "Player"))

