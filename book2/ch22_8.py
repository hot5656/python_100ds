# 資料預測
from sklearn.linear_model import LinearRegression
import numpy as np

# reshape(-1,1) 將一維陣列轉為二維陣列
height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

# 建立線性回歸模型
model = LinearRegression()
# model.fit(X=height, y=weight) 做數據擬合, X必需為二維陣列
model.fit(X=height, y=weight)
# y_pred = model.predict(X),執行數據預測 X必需為二維陣列
# y_pred = model.predict(height)
h = int(input("輸入身高(cm):"))
h /= 100
weight_pred = model.predict([[h]])
print(weight_pred)
print(f"預測體重: {weight_pred[0]:.2f} 公斤")
# 輸入身高(cm):175
# [65.61463415]
# 預測體重: 65.61 公斤