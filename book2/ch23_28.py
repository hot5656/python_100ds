# 梯度下降迴歸
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

X = boston.drop('MEDV', axis=1)
y = boston['MEDV']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# SGDRegressor 對特徵的尺度敏感,先進行標準化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 建立線性迴歸模型並進行擬合訓練數據
sgd_regressor = SGDRegressor(max_iter=1000, random_state=1)
sgd_regressor.fit(X_train, y_train)

# 使用測試集即進行預測
y_pred = sgd_regressor.predict(X_test)

# 計算訓練數據的R平方係數
y_train_pred = sgd_regressor.predict(X_train)
r2_train = r2_score(y_train, y_train_pred)
print(f"訓練數據的R平方係數 : {r2_train.round(3)}")

# 計算測試數據的R平方係數
r2_test = r2_score(y_test, y_pred)
print(f"測試數據的R平方係數 : {r2_test.round(3)}")

# 計算模型的性能指標
mse = mean_squared_error(y_test, y_pred)
print(f"模型的性能指標(MSE) : {mse.round(3)}")

# 訓練數據的R平方係數 : 0.719
# 測試數據的R平方係數 : 0.762
# 模型的性能指標(MSE) : 23.499