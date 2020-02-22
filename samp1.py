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
print("Following are the data file statistics:")
print("Total No.of seasons: ",trcnt)
print("No.of seasons with low availability: ",trcnt1)
print("No.of seasons with medium availability: ",trcnt2)
print("No.of seasons with high availability: ",trcnt3)

