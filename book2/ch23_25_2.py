# 二元二次多項式模型
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from joblib import dump
import matplotlib.pyplot as plt

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns=['LSTAT', 'RM'])
y = boston['MEDV']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# 使用 PolynomialFeatures 生成二元二次特徵
degree = 2
poly = PolynomialFeatures(degree)
X_train_poly = poly.fit_transform(X_train)
# # correct
# X_test_poly = poly.transform(X_test)
# not correct
# X_test_poly = poly.fit_transform(X_test)

# 建立二元二次多項式迴歸模型
model = LinearRegression()
model.fit(X_train_poly, y_train)

# y_pred = model.predict(X_test_poly)
# print(f"實際房價\n{np.array(y_test.tolist())}")
# print("-"*70)
# print(f"預估房價\n{y_pred.round(1)}")

# 查看模型截距與係數
intercept = model.intercept_
coeff = model.coef_

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
ax1.scatter(boston['LSTAT'], boston['RM'], boston['MEDV'], color='b')

# 繪製擬合平面
x = np.arange(0, 40, 1)    # 低收入比例
y = np.arange(0, 10, 1)    # 房間數
x_surf1, y_surf1 = np.meshgrid(x, y)
z = lambda x, y: (model.intercept_ + \
                  model.coef_[1]*x + \
                  model.coef_[2]*y + \
                  model.coef_[3]*x**2 + \
                  model.coef_[4]*x*y + \
                  model.coef_[5]*y**2 )
ax1.plot_surface(x_surf1, y_surf1, z(x_surf1, y_surf1), color='None', alpha=0.2)

# set title
ax1.set_title('真實房價vs預估房價', fontsize=16, color='b')
# set label
ax1.set_xlabel('低收入比例', color='g')
ax1.set_ylabel('房間數', color='g')
ax1.set_zlabel('房價', color='g')

# ax2
# 繪製 3D 圖
ax2.scatter(boston['LSTAT'], boston['RM'], boston['MEDV'], color='b')

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

plt.show()