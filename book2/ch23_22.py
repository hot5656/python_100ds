import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('data23_19.csv')
X = pd.DataFrame(df.x)
y = df.y

# 使用 PolynomialFeatures 生成一元二次特徵
# degree = 2
# degree = 3
degree = 5
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

# 建立一元二次多項式迴歸模型
model = LinearRegression()
model.fit(X_poly, y)
y_poly_pred = model.predict(X_poly)

# 輸出 R 平方係數
print(f"R2 score = {model.score(X_poly, y):.2f}")

# 截距與斜率
intercept =  model.intercept_
coeff = model.coef_
print(f"截距 : {intercept:.3f}")
print(f"係數  : {coeff.round(3)}")

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 建立兩個子圖畫布
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
# 繪第1個子圖
axs[0].scatter(X, y)
axs[0].scatter(X, y_poly_pred, color='r')
axs[0].plot(X, y_poly_pred)
# axs[0].set_title("一元二次迴歸模型 - 點的連線")
# axs[0].set_title("一元三次迴歸模型 - 點的連線")
axs[0].set_title("一元五次迴歸模型 - 點的連線")
# 繪第2個子圖
xx = np.linspace(1, 6, 100)
# y_curf = lambda x: (intercept + coeff[1]*x + coeff[2]*x*x)
# y_curf = lambda x: (intercept + coeff[1]*x + coeff[2]*x*x + coeff[3]*x**3)
y_curf = lambda x: (intercept + coeff[1]*x + coeff[2]*x**2 + coeff[3]*x**3 + coeff[4]*x**4 + coeff[5]*x**5)
axs[1].plot(xx, y_curf(xx))
axs[1].scatter(X, y)
# axs[1].set_title("一元二次迴歸模型 - 曲線")
# axs[1].set_title("一元三次迴歸模型 - 曲線")
axs[1].set_title("一元五次迴歸模型 - 曲線")

plt.show()

# === 一元二次特徵 ====
# R2 score = 0.95
# 截距 : 0.020
# 係數  : [ 0.     1.751 -0.143]
# === 一元三次特徵 ====
# R2 score = 0.96
# 截距 : -1.333
# 係數  : [ 0.     3.454 -0.707  0.054]
# === 一元五次特徵 ====
# R2 score = 1.00
# 截距 : 16.700
# 係數  : [  0.    -34.842  27.696  -9.425   1.454  -0.083]

