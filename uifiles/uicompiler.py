import sys
from PyQt4.uic import compileUi

with open('main_window.ui', 'rb') as ui_file:
    with open('ui_main_window.py', 'wb') as out_file:
        compileUi(ui_file, out_file)

with open('login.ui', 'rb') as ui_file:
    with open('ui_login.py', 'wb') as out_file:
        compileUi(ui_file, out_file)