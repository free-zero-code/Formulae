# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_方程式 import Ui_MainWindow
from PyQt5.QtWidgets import *
from math import *

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_action1_triggered(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'帮助','一个方程式计算软件')

    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        a=float(self.lineEdit.text())
        b=float(self.lineEdit_2.text())
        c=float(self.lineEdit_18.text())
        if a==0:
            
            self.lineEdit_3.setText('无解')
        else:
            e=(c-b)/a
            self.lineEdit_3.setText(str(e))
        
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        a=float(self.lineEdit_5.text())
        b=float(self.lineEdit_6.text())
        c=float(self.lineEdit_4.text())
        f=b*b-4*a*c
        if f<0:
            self.lineEdit_10.setText('无解')
            self.lineEdit_9.setText('无解')
        else:
            x1=(-b+sqrt(f))/2*a
            x2=(-b-sqrt(f))/2*a
            self.lineEdit_10.setText(str(x1))
            self.lineEdit_9.setText(str(x2))
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        a1=float(self.lineEdit_13.text())
        b1=float(self.lineEdit_14.text())
        c1=float(self.lineEdit_7.text())
        a2=float(self.lineEdit_15.text())
        b2=float(self.lineEdit_16.text())
        c2=float(self.lineEdit_8.text())
        if (b1 * a2 - b2 * a1 != 0):
            x = (b1 * c2 - b2 * c1) / (b1 * a2 - b2 * a1)
            y = (c1 * a2 - c2 * a1) / (b1 * a2 - b2 * a1)
	   
            self.lineEdit_11.setText(str(x))
            self.lineEdit_17.setText(str(y))
        elif (b1 * a2 - b2 * a1 == 0 and c1 * a2 - c2 * a1==0):
            self.lineEdit_11.setText('无数解')
            self.lineEdit_17.setText('无数解')
        elif (b1 * a2 - b2 * a1 == 0 and c1 * a2 - c2 * a1!=0):
            
            self.lineEdit_11.setText('无解')
            self.lineEdit_17.setText('无解')

		

	   
            

          
		
		 
	 
			



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
