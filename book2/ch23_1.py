import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'height' : [162, 160, 167, 180, 177, 168, 189, 182, 176, 169],
    'waist'  : [ 71,  81,  70,  90,  95,  80,  78, 100,  84,  80],
    'weight' : [ 53,  62,  58,  71,  72,  69,  80,  91,  78,  70],
}

df = pd.DataFrame(data)
# print(df)

X = df[['height', 'waist']]
y = df['weight']
# print(X)
# print(y)

# 建立線性迴歸模型及擬合數據
model = LinearRegression()
model.fit(X, y)

intercept = model.intercept_
coefficients = model.coef_
print(f"y截距(b0)  : {intercept:.3f}")
print(f"斜率(b1,b2): {coefficients.round(3)}")

# 組合線性迴歸方程式
formula = f"y = {intercept:.3f}"
for i, coef in enumerate(coefficients):
    formula += f" + ({coef:.3f})*x{i+1}"
print("線性迴歸方程式:")
print(formula)

# 輸入身高和腰圍
h = eval(input("請輸入身高:"))
w = eval(input("請輸入腰圍:"))
# 輸入轉成陣列
new_weight = pd.DataFrame(np.array([[h,w]]), columns=["height", "waist"])
print(new_weight)

predicted = model.predict(new_weight)
print(f"預測體重:{predicted[0]:.2f}")
# y截距(b0)  : -90.625
# 斜率(b1,b2): [0.689 0.504]
# 線性迴歸方程式:
# y = -90.625 + (0.689)*x1 + (0.504)*x2
# 請輸入身高:170
# 請輸入腰圍:80
#    height  waist
# 0     170     80
# 預測體重:66.87

# 繪製 3D 散點圖
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['height'], df['waist'], df['weight'], color='blue')

# 創建網格以顯示平面
x_surf, y_surf = np.meshgrid(np.linspace(df['height'].min(), df['height'].max(), 100),
                             np.linspace(df['waist'].min(), df['waist'].max(), 100))
z_surf = intercept + coefficients[0] * x_surf + coefficients[1] * y_surf

# 繪製擬合平面
ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.5)

# 標籤
ax.set_xlabel('Height')
ax.set_ylabel('Waist')
ax.set_zlabel('Weight')
plt.show()