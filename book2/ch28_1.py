import numpy as np
import matplotlib.pyplot as plt

# 建立10個點,5個為分類A,5個為分類B
X = np.array([[1, 2.5], [0.5, 2], [2, 2], [1.5, 1], [2.5, 1.3],
              [3, 3.5], [4.5, 3.5], [4, 4], [2.5, 4.5], [3.5, 3] ])
y = np.array(['A','A','A','A','A','B','B','B','B','B',])

# 繪製點,A 'o', B '*'
for i, marker in zip(['A', 'B'], ['o', '*']):
    plt.scatter(X[y==i, 0], X[y==i, 1], marker=marker, label=i )

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.legend()
plt.show()