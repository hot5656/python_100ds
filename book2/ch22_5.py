from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, n_classes=2, random_state=1)

plt.scatter(X[:,0], X[:,1], marker='o', c=y, s=25, edgecolors='k' )
plt.show()