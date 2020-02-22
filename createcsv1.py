import sys
import csv
import os
#import pymysql
#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='heart1')
import sqlite3
con = sqlite3.connect('heart1')

cur = con.cursor()
cur.execute('SELECT * FROM lsfacts;')
rows = cur.fetchall()
fp = open('lsfacts1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
print('lsfacts1.csv file successfully created')
con.commit()

