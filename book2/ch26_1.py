# 簡單數據執行隨機森林(迴歸應用)
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# 建立一個小型數據集
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# 建立森林隨機模型
# n_estimators 設計隨機森林有機棵樹,更多的樹可能會有更好的性能
#              但也同時增加訓練時間及模型的大小(default 100)
estimators = 100
rt = RandomForestRegressor(n_estimators=estimators, random_state=42)

# 訓練模型
rt.fit(X, y)

#進行預測
X_new = np.array([[5.5], [6.5], [7.5]])
predictions = rt.predict(X_new)
print(f"estimators = {estimators}")
print(f"預測結果:{predictions}")

# estimators = 100
# 預測結果:[10.46 12.56 14.4 ]
# estimators = 1000
# 預測結果:[10.414 12.45  14.404]





