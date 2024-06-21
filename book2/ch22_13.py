# 使用 scikit-learn LinearRegression 建立線性回歸模型
# 繪製身高與體中資料圖表
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# reshape(-1,1) 將一維陣列轉為二維陣列
height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

plt.plot(height, weight, "ko")
plt.axis([0, 1.9, -150, 150])
plt.title("身高 vs 體重")
plt.xlabel("身高")
plt.ylabel("體重")

# 建立線性回歸模型
model = LinearRegression()
# model.fit(X=height, y=weight) 做數據擬合, X必需為二維陣列
model.fit(X=height, y=weight)

x_line = np.array([0, 1.9]).reshape(-1,1)
# y_pred = model.predict(X),執行數據預測 X必需為二維陣列
y_pred = model.predict(x_line)
plt.plot(x_line, y_pred, c='r')

# 截距與斜率
print(f"y截距 : {model.intercept_:.2f}")
print(f"斜率  : {model.coef_[0]:.2f}")

plt.grid()
plt.show()

# y截距 : -53.90
# 斜率  : 68.29
# 所以方程式為 : weight = 68.29*height - 53.9