from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

#  windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# load 鳶尾花數據
iris = datasets.load_iris()
X = iris.data[: , :2]
y = iris.target

# 建立模型,進行訓練
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 產生所有平面座標
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

fig, axs = plt.subplots(2, 2, figsize=(10,10))
k_values = [3, 5, 19, 49]

for k, ax in zip(k_values, axs.ravel()):
    # 將 xx, yy 先扁平化再組成二維陣列,然後預估分類
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3)

    # 顯示散點圖
    scatter = ax.scatter(X[:,0], X[:,1], c=y, edgecolors='b')

    # 增加圖例
    handle, labels = scatter.legend_elements()
    ax.legend(handle, iris.target_names, title='鳶尾花品種')

    ax.set_title(f'KNN for 鳶尾花Iris, k={k}')
    ax.set_xlabel('花萼長度sepal length')
    ax.set_ylabel('花萼寬度sepal width')

plt.subplots_adjust(wspace=0.2, hspace=0.2)
plt.show()