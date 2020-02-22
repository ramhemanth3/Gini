import sys
import os
#import xlsxwriter
from points import *
from PyQt5 import QtWidgets, QtGui, QtCore

#import pymysql
#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='rivgin1')
import sqlite3
con = sqlite3.connect('rivgin1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_4.clicked.connect(self.insertvalues)
     

  def insertvalues(self):
    with con:
      cur = con.cursor()
      rname = str(self.ui.lineEdit_3.text())
      p1low = str(self.ui.lineEdit_4.text())
      p2low = str(self.ui.lineEdit_6.text())
      p1high = str(self.ui.lineEdit_5.text())
      p2high = str(self.ui.lineEdit_7.text())
      avail = str(self.ui.lineEdit_8.text())
      cur.execute('INSERT INTO points VALUES(%s,%s,%s,%s,%s,%s)',(rname,p1low,p1high,p2low,p2high,avail))
      con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
