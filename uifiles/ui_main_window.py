# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Mar 25 21:33:26 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stockTable = QtGui.QTableView(self.horizontalLayoutWidget)
        self.stockTable.setSortingEnabled(False)
        self.stockTable.setObjectName(_fromUtf8("stockTable"))
        self.horizontalLayout.addWidget(self.stockTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuHelp_2 = QtGui.QMenu(self.menubar)
        self.menuHelp_2.setObjectName(_fromUtf8("menuHelp_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionStop_sync = QtGui.QAction(MainWindow)
        self.actionStop_sync.setObjectName(_fromUtf8("actionStop_sync"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExport_PDF = QtGui.QAction(MainWindow)
        self.actionExport_PDF.setObjectName(_fromUtf8("actionExport_PDF"))
        self.actionHelp_Topics = QtGui.QAction(MainWindow)
        self.actionHelp_Topics.setObjectName(_fromUtf8("actionHelp_Topics"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExport_Companies_List = QtGui.QAction(MainWindow)
        self.actionExport_Companies_List.setObjectName(_fromUtf8("actionExport_Companies_List"))
        self.menuFile.addAction(self.actionStop_sync)
        self.menuFile.addAction(self.actionExport_PDF)
        self.menuFile.addAction(self.actionExport_Companies_List)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionEdit)
        self.menuHelp_2.addAction(self.actionHelp_Topics)
        self.menuHelp_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help", None))
        self.actionEdit.setText(_translate("MainWindow", "Preferences", None))
        self.actionStop_sync.setText(_translate("MainWindow", "Stop Sync", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExport_PDF.setText(_translate("MainWindow", "Export Current Data", None))
        self.actionHelp_Topics.setText(_translate("MainWindow", "Help Topics", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExport_Companies_List.setText(_translate("MainWindow", "Export List of Companies", None))

