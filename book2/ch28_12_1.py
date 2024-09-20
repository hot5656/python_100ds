from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 生成 make_moons 數據
X,y = make_moons(n_samples=200, noise=0.1, random_state=0)

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 0.2, X[:,0].max() + 0.2
y_min, y_max = X[:,1].min() - 0.2, X[:,1].max() + 0.2

# 產生所有平面座標點
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

degrees = [2, 3, 4 ,5]
titles = ['Poly核函數 degree=2', 'Poly核函數 degree=3',
          'Poly核函數 degree=4', 'Poly核函數 degree=5']

fig, sub = plt.subplots(2, 2, figsize=(10, 10))
# 調整子圖空間
plt.subplots_adjust(wspace=0.4, hspace=0.4)
# 將子圖的陣列進行扁平化處理(原sub 為2*2)
sub = sub.flatten()


for degree, title, ax in zip(degrees, titles, sub):
    model = SVC(kernel='poly', degree=degree, gamma='scale')
    model.fit(X, y)

    # 將 xx, yy 先扁平化再組成為二維陣列,然後再預測分類
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # 繪製填充等高線
    ax.contourf(xx, yy, Z, alpha=0.3)
    # cmap='viridis',

    # 顯示散點圖,標籤0使用點,標籤1使用星型
    scatter = ax.scatter(X[:,0][y == 0], X[:,1][y == 0], c='b')
    scatter = ax.scatter(X[:,0][y == 1], X[:,1][y == 1], c='r', marker='*')

    ax.set_title(title + f"準確率({accuracy_score(y, model.predict(X)):.2f})")

plt.show()

