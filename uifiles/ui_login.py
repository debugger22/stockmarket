# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Tue Mar 25 21:33:27 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 199)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 381, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblUserId = QtGui.QLabel(self.gridLayoutWidget)
        self.lblUserId.setObjectName(_fromUtf8("lblUserId"))
        self.gridLayout.addWidget(self.lblUserId, 0, 0, 1, 1)
        self.lblPassword = QtGui.QLabel(self.gridLayoutWidget)
        self.lblPassword.setObjectName(_fromUtf8("lblPassword"))
        self.gridLayout.addWidget(self.lblPassword, 1, 0, 1, 1)
        self.txtUserId = QtGui.QTextEdit(self.gridLayoutWidget)
        self.txtUserId.setObjectName(_fromUtf8("txtUserId"))
        self.gridLayout.addWidget(self.txtUserId, 0, 1, 1, 1)
        self.txtPassword = QtGui.QTextEdit(self.gridLayoutWidget)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.gridLayout.addWidget(self.txtPassword, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblUserId.setText(_translate("Dialog", "User Id:", None))
        self.lblPassword.setText(_translate("Dialog", "Password", None))

