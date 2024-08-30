# 繪製3維超平面
from sklearn.datasets import make_circles
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

# 生成數據
X, y = make_circles(n_samples=300, noise=0.05, random_state=10)
z = X[:,0]**2 + X[:,1]**2

features = np.concatenate((X, z.reshape(-1,1)), axis=1)
svc = svm.SVC(kernel='linear')
svc.fit(features, y)

# print(f"權重係數  :{svc.coef_}")
# print(f"截距(篇置):{svc.intercept_}")

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 3D 繪圖
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 繪製數據點,分類A使用圓圈, 分類B使用星型, 加入 Label 參數
for i, marker in zip([0, 1], ['o', '*'] ):
    ax.scatter(X[y == i, 0], X[y == i, 1], z[y==i], marker=marker, label=i)

# 更改視角
# ax.view_init(elev=30, azim=-60) # default
# elev: -90 ~ 90, azim: -180 ~ 180
# ax.view_init(elev=10, azim=-60)
ax.view_init(elev=20, azim=-120)
# 在 z 軸方向上抬高 10 度，同時在 xy 平面內旋轉 -60 度。也就是說，
# 觀察者的視角是在 z 軸上方 10 度，並且從 x 軸方向向 y 軸方向旋轉了 -60 度。

features = np.concatenate((X, z.reshape(-1,1)), axis=1)
svc = svm.SVC(kernel='linear')
svc.fit(features, y)

# 計算x3公式
x3 = lambda x, y : (-svc.intercept_[0] - svc.coef_[0][0] *
                    x - svc.coef_[0][1] *y ) / svc.coef_[0][2]

grid = np.linspace(-1.5, 1.5)
xx, yy = np.meshgrid(grid, grid)
ax.plot_surface(xx, yy, x3(xx, yy), color='r', alpha=0.3)

plt.title("支援向量機-繪製3D超平面")
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
# label 位置
plt.legend()
plt.show()