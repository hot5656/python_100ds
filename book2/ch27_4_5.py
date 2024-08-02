from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np

# 生成數據
X, y = make_blobs(n_samples=500, centers=5, random_state=8)

# 建立模型,進行訓練
# n_neighbors=3 取最近 3 點
k = 3
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(X, y)

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 產生所有平面座標(這些陣列是二維的)
# xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
#                      np.arange(y_min, y_max, 0.01))
# more quickly
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# ravel() 方法將二維陣列壓平成一維陣列
# np.c_ 按列合併多個一維陣列，生成一個新的二維陣
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
# Z 的 shape same as xx
Z = Z.reshape(xx.shape)

# 繪製等高線圖（Filled Contour Plot）
plt.contourf(xx, yy, Z, alpha=0.3)

# 顯示散點圖
plt.scatter(X[:,0], X[:,1], c=y, edgecolor='b')

# 顯示準確度
y_pred = knn.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"準確率 : {accuracy}")

plt.show()

# 準確率 : 0.952