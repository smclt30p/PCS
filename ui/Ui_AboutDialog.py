# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\about.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutDialog.resize(683, 443)
        AboutDialog.setMinimumSize(QtCore.QSize(300, 0))
        AboutDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(AboutDialog)
        self.frame.setStyleSheet("#frame { background: white; }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.bg = QtWidgets.QLabel(self.frame)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("../res/logo.png"))
        self.bg.setObjectName("bg")
        self.gridLayout.addWidget(self.bg, 0, 0, 5, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(363, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 3, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.version_string = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.version_string.setFont(font)
        self.version_string.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.version_string.setObjectName("version_string")
        self.gridLayout.addWidget(self.version_string, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(AboutDialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(185)
        self.treeWidget.header().setMinimumSectionSize(60)
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 90)

        self.retranslateUi(AboutDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "PCS - About"))
        self.label.setText(_translate("AboutDialog", "Putlocker Client System"))
        self.label_3.setText(_translate("AboutDialog", "Copyright © 2017 Ognjen Galić"))
        self.version_string.setText(_translate("AboutDialog", "Version v1.1-STABLE"))
        self.textBrowser.setHtml(_translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:25px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fcfcfc;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:8pt; color:#2b2b2b; background-color:#fcfcfc;\">Copyright 2017 Ognjen Galić</span><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:8pt; color:#2b2b2b;\"><br /><br /></span><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:8pt; color:#2b2b2b; background-color:#fcfcfc;\">Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:<br /><br />1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.<br /><br />2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.<br /><br />THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AboutDialog", "License"))
        self.treeWidget.headerItem().setText(0, _translate("AboutDialog", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("AboutDialog", "Author"))
        self.treeWidget.headerItem().setText(2, _translate("AboutDialog", "License"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("AboutDialog", "Qt 5"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("AboutDialog", "The Qt Company"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("AboutDialog", "GNU GPL 2.0/3.0/LGPL 3.0"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("AboutDialog", "Python 3"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("AboutDialog", "Python Software Foundation"))
        self.treeWidget.topLevelItem(1).setText(2, _translate("AboutDialog", "Python Software Foundation License"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("AboutDialog", "requests"))
        self.treeWidget.topLevelItem(2).setText(1, _translate("AboutDialog", "Kenneth Reitz"))
        self.treeWidget.topLevelItem(2).setText(2, _translate("AboutDialog", "Apache 2"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("AboutDialog", "demjson"))
        self.treeWidget.topLevelItem(3).setText(1, _translate("AboutDialog", "Deron Meranda"))
        self.treeWidget.topLevelItem(3).setText(2, _translate("AboutDialog", "GNU LGPL 3.0"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("AboutDialog", "lxml"))
        self.treeWidget.topLevelItem(4).setText(1, _translate("AboutDialog", "lxml dev team"))
        self.treeWidget.topLevelItem(4).setText(2, _translate("AboutDialog", "BSD/MIT License (version specific)"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("AboutDialog", "bs4"))
        self.treeWidget.topLevelItem(5).setText(1, _translate("AboutDialog", "Leonard Richardson"))
        self.treeWidget.topLevelItem(5).setText(2, _translate("AboutDialog", "MIT License"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("AboutDialog", "pyqt5"))
        self.treeWidget.topLevelItem(6).setText(1, _translate("AboutDialog", "Riverbank Computing Limited"))
        self.treeWidget.topLevelItem(6).setText(2, _translate("AboutDialog", "GNU GPL v3"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AboutDialog", "3rd Party Software"))

