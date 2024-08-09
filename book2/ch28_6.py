import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from joblib import dump

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 建立10個點,5個為分類A,5個為分類B
X = np.array([[1, 2.5], [0.5, 2], [2, 2], [1.5, 1], [2.5, 1.3],
              [3, 3.5], [4.5, 3.5], [4, 4], [2.5, 4.5], [3.5, 3] ])
y = np.array(['A','A','A','A','A','B','B','B','B','B',])

# 繪製點,A 'o', B '*'
for i, marker in zip(['A', 'B'], ['o', '*']):
    plt.scatter(X[y==i, 0], X[y==i, 1], marker=marker, label=i )

# 建立 linear svc+耦合
svc = svm.SVC(kernel='linear')
svc.fit(X, y)


ax = plt.gca()

# 建立格點評估模型
xx = np.linspace(0, 5)
yy = np.linspace(0, 5)
XX, YY = np.meshgrid(xx, yy)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svc.decision_function(xy).reshape(XX.shape)

# 繪製決策邊和間隔
ax.contour(XX, YY, Z, colors='b', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])

# 用圓圈繪製支援向量
# s=100 設置每個散點的大小
# facecolors='none', 'none' 表示點沒有填充顏色
# edgecolors='k', 設置點的邊界顏色 'k' 是黑色的縮寫
plt.scatter(svc.support_vectors_[:,0], svc.support_vectors_[:,1],
            s=100, facecolors='none', edgecolors='k')

plt.title('支援向量機-繪製超平面及決策邊界')
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.legend()
plt.show()