# 繪製決策樹
# pip install Graphviz
from joblib import load
from sklearn import tree
from graphviz import Source

# dtc3.joblib include feature name and class_names

# default feature name, no class name
dtc, feature_names, class_names = load('dtc3.joblib')

# add feature name and class_names
# feature_names = ['alcohol','malic_acid']
# class_names = ['Barolo','Grignolino','Barbera']
grpah = Source(tree.export_graphviz(dtc, out_file=None, feature_names=feature_names, class_names=class_names, filled=True))

# default feature name, no class name
# grpah = Source(tree.export_graphviz(dtc, out_file=None))
grpah.format = 'png'
grpah.render(filename='dtc_tree', view=True)
