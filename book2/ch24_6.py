# 用最全部特徵,設計邏輯迴歸模型
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# 讀取數據
data = pd.read_csv('UCI_Credit_Card.csv')

# 定義特徵和目標變數
X = data.drop(["ID", "default.payment.next.month"], axis=1)
y = data["default.payment.next.month"]

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=10)

# 特徵縮放(標準化)
# fit_transform 用於訓練數據：
#     fit 計算訓練數據的均值和方差
#     transform 使用這些計算出的均值和方差對訓練數據進行標準化
# transform 用於測試數據：
#     只使用訓練數據計算出的均值和方差來標準化測試數據，不會重新計算均值和方差
# 這樣做是為了避免數據洩漏，確保測試數據的標準化過程不受訓練數據的影響，同時保持測試數據的獨立性和真實性
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 建立邏輯迴歸模型 + 使用訓練集訓練模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 在訓練集進行預測並計算準確率
train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, train_pred)
print(f"訓練集數據準確率 Accuracy: {train_accuracy*100:.2f}%")

test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_pred)
print(f"測試集數據準確率 Accuracy: {test_accuracy*100:.2f}%")

# 訓練集數據準確率 Accuracy: 81.01%
# 測試集數據準確率 Accuracy: 81.30%
