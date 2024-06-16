from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

X, y = make_circles(n_samples=100, noise=0.05, random_state=0)

plt.scatter(X[:,0],  X[:,1], c=y)
plt.show()
