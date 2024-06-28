# 用所有參數預估房價
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from joblib import dump
import matplotlib.pyplot as plt

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

# X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns=['LSTAT', 'RM'])
X = boston.drop('MEDV', axis=1)
y = boston['MEDV']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# 建立線性迴歸模型並擬合訓練數據
model = LinearRegression()
model.fit(X_train, y_train)

# 進行預測
y_pred = model.predict(X_test)

# 計算模型性能指標
r2 = r2_score(y_test, y_pred)
print(f"R score : {r2.round(3)}")
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error(MSE) : {mse.round(3)}")

# 查看模型截距與係數
intercept =  model.intercept_
coeff = model.coef_
print(f"截距 : {intercept:.3f}")
# 多項式特徵
# print(poly.get_feature_names_out())
print(f"係數 : {coeff.round(3)}")
print("-"*70)
print(f"實際房價\n{np.array(y_test.tolist())}")
print("-"*70)
print(f"預估房價\n{y_pred.round(1)}")

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 繪製實際房價與預測房價圖表
plt.scatter(y_test, y_pred)
# 繪製對角線
plt.plot([min(y_test),max(y_test)], [min(y_test),max(y_test)], color='red', linestyle='--', lw=2)
plt.title("實際房價vs預測房價")
plt.xlabel("實際房價")
plt.ylabel("預測房價")
plt.show()

# R score : 0.763
# Mean Squared Error(MSE) : 23.441
# 截距 : 42.031
# 係數 : [ 5.0000e-02  5.3000e-02  2.4000e-02  2.3010e+00 -1.8746e+01  3.1110e+00
#   5.0000e-03 -1.4020e+00  2.3000e-01 -1.1000e-02 -9.7900e-01  8.0000e-03
#  -5.7700e-01]
# ----------------------------------------------------------------------
# 實際房價
# [28.2 23.9 16.6 22.  20.8 23.  27.9 14.5 21.5 22.6 23.7 31.2 19.3 19.4
#  19.4 27.9 13.9 50.  24.1 14.6 16.2 15.6 23.8 25.  23.5  8.3 13.5 17.5
#  43.1 11.5 24.1 18.5 50.  12.6 19.8 24.5 14.9 36.2 11.9 19.1 22.6 20.7
#  30.1 13.3 14.6  8.4 50.  12.7 25.  18.6 29.8 22.2 28.7 23.8  8.1 22.2
#   6.3 22.1 17.5 48.3 16.7 26.6  8.5 14.5 23.7 37.2 41.7 16.5 21.7 22.7
#  23.  10.5 21.9 21.  20.4 21.8 50.  22.  23.3 37.3 18.  19.2 34.9 13.4
#  22.9 22.5 13.  24.6 18.3 18.1 23.9 50.  13.6 22.9 10.9 18.9 22.4 22.9
#  44.8 21.7 10.2 15.4]
# ----------------------------------------------------------------------
# 預估房價
# [32.2 28.  18.  21.6 18.1 20.  32.2 18.3 24.2 27.1 26.7 28.8 20.9 26.5
#  23.3 20.5 17.4 38.1 30.4  8.5 20.9 16.3 25.3 25.  31.3 10.6 13.7 17.1
#  36.4 14.2 21.5 13.7 42.9 18.1 21.9 20.3 17.  27.6  9.9 19.3 24.5 21.5
#  29.4 15.4 18.8 13.9 39.9 18.2 26.2 20.  24.5 24.3 25.4 26.8  4.  24.1
#  10.4 27.1 16.9 35.8 19.3 27.7 16.1 18.2 10.5 32.5 36.8 22.4 24.7 25.4
#  23.7  7.8 15.6 20.6 20.5 20.7 33.8 28.1 25.6 34.5 18.6 23.8 34.5 12.7
#  21.3 30.  16.6 24.6 19.  16.9 27.3 41.8 14.  23.2 17.4 21.9 23.2 29.
#  37.  20.3 16.9 17.7]
