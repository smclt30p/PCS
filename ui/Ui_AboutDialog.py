# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\src\about.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(300, 151)
        AboutDialog.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(AboutDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Dialog"))
        self.label.setText(_translate("AboutDialog", "PCS - Putlocker Client System"))
        self.label_2.setText(_translate("AboutDialog", "Version 1.0.0"))
        self.label_3.setText(_translate("AboutDialog", "Copyright (C) 2016 Ognjen Galic"))

