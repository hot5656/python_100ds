# 使用 scikit-learn LinearRegression 建立線性回歸模型
# 繪製身高與體重資料圖表
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# reshape(-1,1) 將一維陣列轉為二維陣列
height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

plt.plot(height, weight, "ko")
plt.axis([1.5, 1.85, 50, 90])
plt.title("身高 vs 體重")
plt.xlabel("身高")
plt.ylabel("體重")

print(f"height={height}")

print(f"height[:,0]={height[:,0]}")
# 建立線性迴歸模型係數
coef = np.polyfit(height[:,0], weight, 1)
# 建立線性迴線函數
reg = np.poly1d(coef)
print(f"reg(height[:,0]) = {reg(height[:,0])}")

# 建立線性回歸模型
model = LinearRegression()
# 數據擬合模型 model.fit(X=height, y=weight) 做數據擬合, X必需為二維陣列
model.fit(X=height, y=weight)
# y_pred = model.predict(X),執行數據預測 X必需為二維陣列
y_pred = model.predict(height)
plt.plot(height, y_pred, c='r')
print(f"y_pred={y_pred}")

# np.polyfit() 與 LinearRegression() 結果是一樣
# height=[[1.6 ]
#  [1.63]
#  [1.71]
#  [1.73]
#  [1.83]]
# height[:,0]=[1.6  1.63 1.71 1.73 1.83]
# reg(height[:,0]) = [55.37073171 57.4195122  62.88292683 64.24878049 71.07804878]
# y_pred=[55.37073171 57.4195122  62.88292683 64.24878049 71.07804878]

plt.grid()
plt.show()