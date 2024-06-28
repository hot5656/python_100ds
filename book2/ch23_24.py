# 二元二次多項式模型 - 計算預估房價
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
# correct
X_test_poly = poly.transform(X_test)
# not correct
# X_test_poly = poly.fit_transform(X_test)

# 建立二元二次多項式迴歸模型
model = LinearRegression()
model.fit(X_train_poly, y_train)

y_pred = model.predict(X_test_poly)
print(f"實際房價\n{np.array(y_test.tolist())}")
print("-"*70)
print(f"預估房價\n{y_pred.round(1)}")

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

plt.scatter(y_test, y_pred)
line_x = np.linspace(0, 50, 100)
plt.plot(line_x, line_x, color='red')
plt.title("實際房價vs預測房價")
plt.xlabel("實際房價")
plt.ylabel("預測房價")
plt.show()

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
# [28.4 27.8 15.4 23.4 20.9 22.4 30.  19.8 16.  24.7 27.6 31.8 18.8 21.4
#  20.8 19.7 13.2 50.7 24.9 12.6 20.3 16.6 25.  27.3 28.1 11.9 14.4 21.7
#  33.7 14.4 28.9 15.5 44.7 17.5 23.4 19.1 16.7 33.  18.6 18.4 25.8 26.2
#  26.9 12.  16.2 14.  43.4 17.  22.6 23.  24.9 22.3 28.3 22.2 11.7 26.9
#   9.1 26.1 18.4 45.6 19.1 28.1 14.6 16.8 10.5 32.  48.9 25.5 21.8 20.4
#  26.8 14.4 18.7 22.9 19.1 21.2 34.7 25.5 26.6 35.1 18.9 21.9 33.2 13.1
#  27.9 28.1 15.7 28.5 18.5 17.3 31.3 49.7 15.9 20.2 19.  19.5 24.7 25.5
#  45.6 20.2 17.4 16.2]