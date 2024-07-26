from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

X = boston.drop('MEDV', axis=1)
y = boston['MEDV']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)


# 建立森林隨機模型
# n_estimators 設計隨機森林有機棵樹,更多的樹可能會有更好的性能
#              但也同時增加訓練時間及模型的大小(default 100)
rt = RandomForestRegressor(n_estimators=100, random_state=42)

# 訓練模型
rt.fit(X_train, y_train)

#進行預測
y_pred = rt.predict(X_test)

# 計算評估指標
r2 = r2_score(y_test, y_pred)
print(f"R-squared : {r2:.3f}")
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error : {mse:.3f}")

# R-squared : 0.914
# Mean Squared Error : 8.523