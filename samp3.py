from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import export_graphviz
import pandas as pd
col_names = ['p1low','p1high','p2low','p2high','availability']
# load dataset
lels = pd.read_csv("levels.csv", header=None, names=col_names)
#split dataset in features and target variable
feature_cols = ['p1low','p1high','p2low','p2high']
X = lels[feature_cols] # Features
y = lels.availability # Target variable
clf = tree.DecisionTreeClassifier(criterion="gini")
clf = clf.fit(X, y)
export_graphviz(clf, out_file="levelstree1.dot")

#Command to generate the tree in a .pdf: dot -Tpdf tree1.dot -o tree1.pdf


