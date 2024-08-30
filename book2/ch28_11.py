import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import svm

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 建立 50個點, 25個為分類0, 25個為分類1
X,y = make_blobs(n_samples=50, centers=2, random_state=12)

# 建立線性SVM模型
svc = svm.SVC(kernel='linear')
svc.fit(X, y)

# 繪製數據點,分類0使用圓圈, 分類1使用星型
for i, marker in zip([0, 1], ['o', '*'] ):
    plt.scatter(X[y == i, 0], X[y == i, 1], marker=marker, label=str(i))

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# 建立格點來評估模型
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
XX, YY = np.meshgrid(xx, yy)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svc.decision_function(xy).reshape(XX.shape)

# 繪製決策邊和超平面
# 繪製 2D 等高線, -1 , 0, 1
ax.contour(XX, YY, Z, colors='b', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])

# 用圓圈繪製支援向量
# s=100 設置每個散點的大小
# facecolors='none', 'none' 表示點沒有填充顏色
# edgecolors='k', 設置點的邊界顏色 'k' 是黑色的縮寫
plt.scatter(svc.support_vectors_[:,0], svc.support_vectors_[:,1],
            s=100, facecolors='none', edgecolors='k')

plt.title("支援向量機-kernel='linear'")
plt.legend()
plt.show()
