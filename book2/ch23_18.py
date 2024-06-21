import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns=['LSTAT', 'RM'])
y = boston['MEDV']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# 建立線性迴歸模型及擬合數據
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"真實房價\n {y_test.tolist()}")
print("-"*70)
print(f"預測房價\n {y_pred.round(1)}")

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 多單張圖
fig = plt.figure(figsize= (10, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# ax1
# 繪製 3D 圖
ax1.scatter(boston['LSTAT'], boston['RM'], boston['MEDV'], color='b')  # 散佈圖

# 繪製擬合平面
x = np.arange(0, 40, 1)    # 低收入比例
y = np.arange(0, 10, 1)    # 房間數
x_surf1, y_surf1 = np.meshgrid(x, y)
z = lambda x, y: (model.intercept_ + model.coef_[0]*x + model.coef_[1]*y)
ax1.plot_surface(x_surf1, y_surf1, z(x_surf1, y_surf1), color='None', alpha=0.2)

# set title
ax1.set_title('真實房價vs預估房價', fontsize=16, color='b')
# set label
ax1.set_xlabel('低收入比例', color='g')
ax1.set_ylabel('房間數', color='g')
ax1.set_zlabel('房價', color='g')

# ax2
# 繪製 3D 圖
ax2.scatter(boston['LSTAT'], boston['RM'], boston['MEDV'], color='b')  # 散佈圖

# 繪製擬合平面
ax2.plot_surface(x_surf1, y_surf1, z(x_surf1, y_surf1), color='None', alpha=0.2)

# set title
ax2.set_title('真實房價vs預估房價', fontsize=16, color='b')
# set label
ax2.set_xlabel('低收入比例', color='g')
ax2.set_ylabel('房間數', color='g')
ax2.set_zlabel('房價', color='g')

# 更改視角
ax2.view_init(elev=30, azim=45)
# 在 z 軸方向上抬高 30 度，同時在 xy 平面內旋轉 45 度。也就是說，觀察者的視角是在 z 軸上方 30 度，並且從 x 軸方向向 y 軸方向旋轉了 45 度。
# elev (elevation)：高度角，表示從 xy 平面向上的角度。這個參數控制視角在 z 軸方向上的旋轉。
#     當 elev=0 時，視角與 xy 平面平行。
#     當 elev=90 時，視角在 z 軸的正上方。
# azim (azimuth)：方位角，表示從 x 軸方向開始在 xy 平面內的旋轉角度。這個參數控制視角在 xy 平面內的旋轉。
#     當 azim=0 時，視角沿著 x 軸正方向。
#     當 azim=90 時，視角沿著 y 軸正方向。
#     當 azim=45 時，視角位於 x 軸和 y 軸之間的 45 度角處。
plt.show()