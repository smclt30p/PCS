# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\arguments.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Arguments(object):
    def setupUi(self, Arguments):
        Arguments.setObjectName("Arguments")
        Arguments.resize(564, 424)
        self.gridLayout = QtWidgets.QGridLayout(Arguments)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Arguments)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preset_combo = QtWidgets.QComboBox(Arguments)
        self.preset_combo.setObjectName("preset_combo")
        self.horizontalLayout.addWidget(self.preset_combo)
        self.horizontalLayout.setStretch(0, 80)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.treeWidget = QtWidgets.QTreeWidget(Arguments)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_add = QtWidgets.QPushButton(Arguments)
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        self.button_remove = QtWidgets.QPushButton(Arguments)
        self.button_remove.setObjectName("button_remove")
        self.verticalLayout.addWidget(self.button_remove)
        self.button_remove_all = QtWidgets.QPushButton(Arguments)
        self.button_remove_all.setObjectName("button_remove_all")
        self.verticalLayout.addWidget(self.button_remove_all)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.button_save = QtWidgets.QPushButton(Arguments)
        self.button_save.setObjectName("button_save")
        self.verticalLayout.addWidget(self.button_save)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 3, 1)
        self.label_result = QtWidgets.QLabel(Arguments)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 3, 0, 1, 1)
        self.result = QtWidgets.QLabel(Arguments)
        self.result.setStyleSheet("#result {\n"
"font: 8pt \"Consolas\";\n"
"border: 1px solid #d2d2d2;\n"
"background: white;\n"
"padding: 3px;\n"
"}")
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 4, 0, 1, 1)

        self.retranslateUi(Arguments)
        QtCore.QMetaObject.connectSlotsByName(Arguments)

    def retranslateUi(self, Arguments):
        _translate = QtCore.QCoreApplication.translate
        Arguments.setWindowTitle(_translate("Arguments", "Dialog"))
        self.label.setText(_translate("Arguments", "Preset"))
        self.treeWidget.headerItem().setText(0, _translate("Arguments", "Argument"))
        self.button_add.setText(_translate("Arguments", "Insert"))
        self.button_remove.setText(_translate("Arguments", "Remove"))
        self.button_remove_all.setText(_translate("Arguments", "Remove All"))
        self.button_save.setText(_translate("Arguments", "Save"))
        self.label_result.setText(_translate("Arguments", "Result:"))

