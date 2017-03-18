# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\src\about.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(300, 187)
        AboutDialog.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bg = QtWidgets.QLabel(AboutDialog)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("../res/logo.png"))
        self.bg.setObjectName("bg")
        self.verticalLayout_2.addWidget(self.bg)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(6, 6, 6, 16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.version_string = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.version_string.setFont(font)
        self.version_string.setText("")
        self.version_string.setAlignment(QtCore.Qt.AlignCenter)
        self.version_string.setObjectName("version_string")
        self.verticalLayout.addWidget(self.version_string)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(AboutDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "PCS - About"))
        self.label.setText(_translate("AboutDialog", "PCS - Putlocker Client System"))
        self.label_3.setText(_translate("AboutDialog", "Copyright (C) 2017 Ognjen Galic"))

