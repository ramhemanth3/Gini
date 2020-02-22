import sys
from river import *
from PyQt5 import QtWidgets, QtGui, QtCore

#import pymysql
#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='rivgin1')
import sqlite3
con = sqlite3.connect('heart1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)

  def insertvalues(self):
    with con:
     cur = con.cursor()
     name = str(self.ui.lineEdit_3.text())
     ncity = str(self.ui.lineEdit_7.text())
     dist = str(self.ui.lineEdit_4.text())
     distbp = str(self.ui.lineEdit_5.text())
     distp1 = str(self.ui.lineEdit_6.text())	
     distp2 = str(self.ui.lineEdit.text())
     country = str(self.ui.lineEdit_2.text())
     cur.execute('INSERT INTO river VALUES(%s,%s,%s,%s,%s,%s,%s)',(name,ncity,dist,distbp,distp1,distp2,country))
     con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
