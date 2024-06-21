from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

X, y = make_regression(n_features=1, noise=20, random_state=10)

plt.axis([-3, 3, -150, 150])
plt.scatter(X,y)
plt.show()