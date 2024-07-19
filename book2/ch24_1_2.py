from joblib import dump
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# 20 個申請人年齡,年收入,已有債務
applicants = np.array([
    [25, 50000, 10000],
    [35, 60000,  8000],
    [45, 70000, 12000],
    [55, 80000, 00000],
    [65, 60000,  9000],
    [30, 40000, 12000],
    [40, 70000,  8000],
    [50, 80000, 10000],
    [60, 80000,  8000],
    [33, 50000, 11000],
    [26, 55000, 15000],
    [36, 65000,  7500],
    [46, 75000, 13000],
    [56, 85000, 10000],
    [66, 65000,  8500],
    [31, 45000, 11000],
    [41, 75000,  8500],
    [51, 65000,  9500],
    [61, 85000,  8500],
    [34, 55000, 12000]
])

# 違約紀錄 1:違約
defaults = np.array([1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1])

# 拆分訓練集及測試集
X_train, X_test, y_train, y_test = train_test_split(applicants,\
                        defaults, test_size=0.2, random_state=10)

# 建立邏輯迴歸模型
model = LogisticRegression()
# 使用訓練集訓練模型
model.fit(X_train, y_train)

# 使用模型進行測試
y_pred = model.predict(X_test)
# 計算準確度
print(f"準確度 : {accuracy_score(y_test, y_pred)}")
print(f"真實數據\n {y_test}")
print(f"估計數據\n {y_pred}")

dump(model, 'bank_ch24_1_2.joblib')
# 準確度 : 1.0
# 真實數據
#  [0 1 1 0]
# 估計數據
#  [0 1 1 0]