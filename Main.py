 # -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:02:41 2019

@author: wl181
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from C1 import Ui_wnd_main
    
app = QtWidgets.QApplication([])
qt_app = Ui_wnd_main()
qt_app.show()
app.exec_()