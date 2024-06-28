# 殘差圖
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

# 計算殘差
residuals = y_test - y_pred

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 繪製殘差圖
plt.scatter(y_pred, residuals, alpha=0.5)
# 畫水平線
plt.axhline(y=0, color='r', linestyle='--')
plt.title("波士頓房價殘插圖")
plt.xlabel("預測房價")
plt.ylabel("殘差")
plt.show()