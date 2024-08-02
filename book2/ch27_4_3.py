from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

# 生成數據
X, y = make_blobs(n_samples=200, centers=2, random_state=30)

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 產生所有平面座標(這些陣列是二維的)
# xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
#                      np.arange(y_min, y_max, 0.01))
# more quickly
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

k_values = [1, 3, 5, 7]

# 建立四個子圖
fig, axs = plt.subplots(2, 2, figsize=(10,10))

for k, ax in zip(k_values, axs.ravel()):
    # 建立模型,進行訓練
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X, y)

    # ravel() 方法將二維陣列壓平成一維陣列
    # np.c_ 按列合併多個一維陣列，生成一個新的二維陣
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    # Z 的 shape same as xx
    Z = Z.reshape(xx.shape)

    # 繪製等高線圖
    ax.contourf(xx, yy, Z, alpha=0.3)

    # 顯示散點圖
    ax.scatter(X[:,0], X[:,1], c=y, edgecolor='b')
    ax.set_title(f"KNN, random_state=30, k={k}")

k_values = [5, 7, 29, 49]

# 建立四個子圖
fig, axs = plt.subplots(2, 2, figsize=(10,10))

for k, ax in zip(k_values, axs.ravel()):
    # 建立模型,進行訓練
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X, y)

    # ravel() 方法將二維陣列壓平成一維陣列
    # np.c_ 按列合併多個一維陣列，生成一個新的二維陣
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    # Z 的 shape same as xx
    Z = Z.reshape(xx.shape)

    # 繪製等高線圖
    ax.contourf(xx, yy, Z, alpha=0.3)

    # 顯示散點圖
    ax.scatter(X[:,0], X[:,1], c=y, edgecolor='b')
    ax.set_title(f"KNN, random_state=30, k={k}")

# 調整子圖距離
plt.subplots_adjust(wspace=0.2, hspace=0.4)
plt.show()