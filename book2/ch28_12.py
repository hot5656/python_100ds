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

# 繪製子圖,每個 gamma 值一張圖
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
ax = np.ravel(ax)

gammas = [0.1, 0.5, 1.0, 10.0]
for i, gamma in enumerate(gammas):
    # 建立一個RBF SVM 模型
    svc = svm.SVC(kernel='rbf', gamma=gamma)
    svc.fit(X, y)

    # 繪製數據點,分類0使用圓圈,分類1使用星型
    for j, marker in zip([0, 1], ['o', '*'] ):
        ax[i].scatter(X[y == j, 0], X[y == j, 1], marker=marker, label=str(j))

    xlim = ax[i].get_xlim()
    ylim = ax[i].get_ylim()

    # 建立格點來評估模型
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    XX, YY = np.meshgrid(xx, yy)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = svc.decision_function(xy).reshape(XX.shape)

    # 繪製決策邊和超平面
    # 繪製 2D 等高線, -1 , 0, 1
    ax[i].contour(XX, YY, Z, colors='b', levels=[-1, 0, 1], alpha=0.5,
            linestyles=['--', '-', '--'])

    # 用圓圈繪製支援向量
    # s=100 設置每個散點的大小
    # facecolors='none', 'none' 表示點沒有填充顏色
    # edgecolors='k', 設置點的邊界顏色 'k' 是黑色的縮寫
    ax[i].scatter(svc.support_vectors_[:,0], svc.support_vectors_[:,1],
                s=100, facecolors='none', edgecolors='k')

    ax[i].set_title(f"支援向量機 - kernel='rbf', gamma={gamma}")
    ax[i].legend()

# 調整子圖間的間距
plt.subplots_adjust(wspace=0.2, hspace=0.4)
plt.show()