# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updater.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Updater(object):
    def setupUi(self, Updater):
        Updater.setObjectName("Updater")
        Updater.resize(316, 119)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Updater)
        self.verticalLayout_2.setContentsMargins(16, 9, 9, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(Updater)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.step1 = QtWidgets.QLabel(Updater)
        self.step1.setObjectName("step1")
        self.verticalLayout.addWidget(self.step1)
        self.step2 = QtWidgets.QLabel(Updater)
        self.step2.setObjectName("step2")
        self.verticalLayout.addWidget(self.step2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Updater)
        QtCore.QMetaObject.connectSlotsByName(Updater)

    def retranslateUi(self, Updater):
        _translate = QtCore.QCoreApplication.translate
        Updater.setWindowTitle(_translate("Updater", "Dialog"))
        self.title.setText(_translate("Updater", "Updating PCS to v1.0"))
        self.step1.setText(_translate("Updater", "1. Downloading package"))
        self.step2.setText(_translate("Updater", "2. Installing package"))

