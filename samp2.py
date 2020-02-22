import pandas as pd
import math
col_names = ['p1low','p1high','p2low','p2high','availability']
# load dataset
lels = pd.read_csv("levels.csv", header=None, names=col_names)
#split dataset in features and target variable
feature_cols = ['p1low','p1high','p2low','p2high']

#trcnt stands for total rows using availability count
trcnt1 = len(lels[lels['availability'] == 0])
trcnt2 = len(lels[lels['availability'] == 1])
trcnt3 = len(lels[lels['availability'] == 2])
trcnt = trcnt1 + trcnt2 + trcnt3 
giniroot = 1.0 - (float(trcnt1)/float(trcnt))**2 - (float(trcnt2)/float(trcnt))**2 - (float(trcnt3)/float(trcnt))**2
#p2high1 stands for no.of rows with point 2 high <= 5.85
p2high1 = len(lels[(lels.p2high >= 0) &(lels.p2high <= 5.85)])
p2high2 = len(lels[(lels.p2high >= 5.86) &(lels.p2high <= 7.05)])
p2high3 = len(lels[(lels.p2high >= 7.06)])
#tnor stands for total no.of rows
tnor = p2high1 + p2high2 + p2high3
#cp2high1 stands for count of p2high1 rows with availability '0'
cp2high11 = len(lels[(lels.availability == 0) &(lels.p2high >= 0) &(lels.p2high <= 5.85)])
cp2high12 = len(lels[(lels.availability == 1) &(lels.p2high >= 0) &(lels.p2high <= 5.85)])
cp2high13 = len(lels[(lels.availability == 2) &(lels.p2high >= 0) &(lels.p2high <= 5.85)])
cp2high1 = cp2high11 + cp2high12 + cp2high13
#print("No.of p2high1 rows with different availabilityerities are:",cp2high11,cp2high12,cp2high13)
#cp2high21 stands for count of p2high2 rows with availability '0'
cp2high21 = len(lels[(lels.availability == 0) &(lels.p2high >= 5.86) &(lels.p2high <= 7.05)])
cp2high22 = len(lels[(lels.availability == 1) &(lels.p2high >= 5.86) &(lels.p2high <= 7.05)])
cp2high23 = len(lels[(lels.availability == 2) &(lels.p2high >= 5.86) &(lels.p2high <= 7.05)])
cp2high2 = cp2high21 +  cp2high22 + cp2high23
#print("No.of p2high2 rows with different availabilityerities are:",cp2high21,cp2high22,cp2high23)
#cp2high31 stands for count of p2high3 rows with availability '0'
cp2high31 = len(lels[(lels.availability == 0) &(lels.p2high >= 7.55)])
cp2high32 = len(lels[(lels.availability == 1) &(lels.p2high >= 7.55)])
cp2high33 = len(lels[(lels.availability == 2) &(lels.p2high >= 7.55)])
cp2high3 = cp2high31 + cp2high32 + cp2high33
#gp2hterm1 stands for Gini Index term1 for Point2 high
gp2hterm1= (cp2high1/tnor)*(1.0 - ((cp2high11)/(cp2high1))**2 - ((cp2high12)/(cp2high1))**2 - ((cp2high13)/(cp2high1))**2 )
gp2hterm2= (cp2high2/tnor)*(1.0 - ((cp2high21)/(cp2high2))**2 - ((cp2high22)/(cp2high2))**2 - ((cp2high23)/(cp2high2))**2 )
gp2hterm3= (cp2high3/tnor)*(1.0 - ((cp2high31)/(cp2high3))**2 - ((cp2high32)/(cp2high3))**2 - ((cp2high33)/(cp2high3))**2 )
#gp2hterm3= (float(cp2high3)/float(tnor))(1.0 - (float(cp2high31)/float(cp2high3))**2 - (float(cp2high32)/float(cp2high3))**2 - (float(cp2high33)/float(cp2high3))**2 )
#gp2h stands for Gini Index for the attribute 'Point2 high'
gp2h = gp2hterm1 + gp2hterm2 + gp2hterm3
#print("Gini Index for the attribute 'Point2 high' is:",gp2h)
print('Gini Index at root node is:',giniroot)
