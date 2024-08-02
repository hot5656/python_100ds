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
print()
X = iris.data[: , :2]
y = iris.target

# 建立模型,進行訓練
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 產生所有平面座標
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# 將 xx, yy 先扁平化再組成二維陣列,然後預估分類
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3)

# 顯示散點圖
scatter = plt.scatter(X[:,0], X[:,1], c=y, edgecolors='b')

# 增加圖例
handle, labels = scatter.legend_elements()
plt.legend(handle, iris.target_names, title='鳶尾花品種')

plt.title('KNN for 鳶尾花Iris, k=1')
plt.xlabel('花萼長度sepal length')
plt.ylabel('花萼寬度sepal width')
plt.show()