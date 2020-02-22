import sys
import os
from rivgin import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.pdtls)
     self.ui.pushButton_3.clicked.connect(self.rdtls)
     self.ui.pushButton_5.clicked.connect(self.datafl)
     self.ui.pushButton_6.clicked.connect(self.dflstat)
     self.ui.pushButton_7.clicked.connect(self.ginr)
     self.ui.pushButton_8.clicked.connect(self.dtdot)
     self.ui.pushButton_9.clicked.connect(self.dtpdf)

  def rdtls(self):
    os.system("python river1.py")       

  def pdtls(self):
    os.system("python points1.py")

  def datafl(self):
    os.system("python datafile1.py")

  def dflstat(self):
    os.system("python samp1.py")
	
  def ginr(self):
    os.system("python samp2.py")
	
  def dtdot(self):
    os.system("python samp3.py")       

  def dtpdf(self):
    os.system("python samp5.py")
     
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
