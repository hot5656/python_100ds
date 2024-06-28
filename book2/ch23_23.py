# 二元二次多項式模型
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from joblib import dump

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

# 計算 R 平方數
print(f"R score : {model.score(X_test_poly, y_test)}")

# 查看模型截距與係數
intercept = model.intercept_
coeff = model.coef_
print(f"截距 : {intercept}")
# 多項式特徵
print(poly.get_feature_names_out())
print(f"係數 : {coeff}")

# R score : 0.8217783992497054
# 截距 : 62.51039478281932
# ['1' 'LSTAT' 'RM' 'LSTAT^2' 'LSTAT RM' 'RM^2']
# 係數 : [ 0.00000000e+00  3.28222887e-01 -1.54871817e+01  8.58456016e-03
#  -2.22945786e-01  1.71576436e+00]