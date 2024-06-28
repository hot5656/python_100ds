# 獲得 R平方判定係數,截距與係數
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from joblib import dump

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns=['LSTAT', 'RM'])
y = boston['MEDV']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# 建立線性迴歸模型及擬合數據
model = LinearRegression()
model.fit(X_train, y_train)

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

# 算預測值
y_pred = model.predict(X_test)
# 計算 R 平方數
print(f"R2_Score:{r2_score(y_test, y_pred):.3f}")

# 儲存模型
dump(model, 'boston_model.joblib')

# y截距(b0)  : 2.493
# 斜率(b1,b2): [-0.659  4.539]
# 線性迴歸方程式:
# y = 2.493 + (-0.659)*x1 + (4.539)*x2
# R2_Score:0.675