# 繪製3維超平面及類別0(找出錯誤分類)
from sklearn.datasets import make_circles
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

# 生成數據
X, y = make_circles(n_samples=300, noise=0.05, random_state=10)
z = X[:, 0]**2 + X[:, 1]**2

# 合併特徵
features = np.concatenate((X, z.reshape(-1, 1)), axis=1)

# 訓練 SVM 模型
svc = svm.SVC(kernel='linear')
svc.fit(features, y)

# 計算超平面
x3 = lambda x, y: (-svc.intercept_[0] - svc.coef_[0][0] *
                    x - svc.coef_[0][1] * y) / svc.coef_[0][2]

# 計算數據點到超平面的距離
distances = svc.decision_function(features)

# 設置顏色（在超平面上的距離為正數的顯示為紅色，為負數的顯示為藍色）
colors = np.where(distances > 0, 'red', 'blue')

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 3D 繪圖
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 繪製數據點，使用不同圖形和顏色區分
for i, marker in zip([0, 1], ['o', '*']):
    if (i == 0):
        mask = y == i
        ax.scatter(X[mask, 0], X[mask, 1], z[mask], c=colors[mask], marker=marker, label=f'Class {i}')

# 繪製超平面
grid = np.linspace(-1.5, 1.5)
xx, yy = np.meshgrid(grid, grid)
ax.plot_surface(xx, yy, x3(xx, yy), color='gray', alpha=0.5)

# 更改視角
ax.view_init(elev=20, azim=-120)

# 添加標題和標籤
plt.title("支援向量機-顯示平面上下的數據點")
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.legend()
plt.show()
