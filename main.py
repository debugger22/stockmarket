"""
This module is the main entry module of the software package

Author: Sudhanshu Mishra
"""


from __future__ import division, print_function

import sys
from PyQt4 import QtGui, QtCore, Qt, uic
from datalink import DatabaseConnection


class MyWindow(QtGui.QDialog):

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('uifiles/login.ui', self)
        self.show()
        self.init_ui()

    def key_pressed_event(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def init_ui(self):
        self.connect(self.cmdLogin, Qt.SIGNAL("clicked()"), self.login)

    def login(self):
    	"""
    	This function is called when login button is called
    	"""
        lbl_status = self.lblStatus
        if(self.txtUserId.text() == "" or self.txtPassword.text() == ""):
            lbl_status.setText(
                "<font color='red'>Please enter user Id and password</font>")
            return
        else:
        	lbl_status.setText("")
        if(conn.check_login(self.txtUserId.text(), self.txtPassword.text())):
            lbl_status.setText("<font color='green'>Login successful!</font>")


if __name__ == '__main__':
    conn = DatabaseConnection(
            "localhost",
            "sudhanshu",
            "mypassword",
            "stockmarket"
        )
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
