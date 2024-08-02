import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 生成線性數據
X, y = make_regression(n_features=1, noise=20, random_state=10)

# 建立 X 區間含 300 點
xx = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)

k_values = [2, 3, 4, 5]
fig, axs = plt.subplots(2, 2, figsize=(10,10))

for k, ax in zip(k_values, axs.ravel()):
    # 建立模型, 擬合模型
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, y)

    # 計算平方係數
    r2 = knn.score(X, y)
    print(f"k = {k}, R平方係數: {r2:.3f}")

    # 繪製迴歸線
    yy = knn.predict(xx)
    ax.plot(xx, yy)

    # 繪製散點圖
    ax.scatter(X, y, c='y', edgecolors='b')
    ax.set_title(f"KNN-Regression k={k} R 平方係數={r2:.3f}")

# 調整子圖間距
plt.subplots_adjust(wspace=0.2, hspace=0.2)
plt.show()

# k = 2, R平方係數: 0.871(最好模型)
# k = 3, R平方係數: 0.838
# k = 4, R平方係數: 0.800
# k = 5, R平方係數: 0.788