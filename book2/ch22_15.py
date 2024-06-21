from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score


# reshape(-1,1) 將一維陣列轉為二維陣列
height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

# 建立線性回歸模型
model = LinearRegression()
# model.fit(X=height, y=weight) 做數據擬合, X必需為二維陣列
model.fit(X=height, y=weight)

# 手工計算 RSS
# np.ravel 將原陣列降為一維,若修改會影響原值
# np.flatten 將原陣列降為一維,若修改不會影響原值
RSS = np.sum((weight - np.ravel(model.predict(height))) ** 2)
print(f"RSS : {RSS:.2f}")

# 手工計算 TSS
mean_weight = np.mean(weight)
TSS = np.sum((weight - mean_weight) ** 2)
print(f"TSS : {TSS:.2f}")

# 手工計算 R平方係數
R_quare = 1 - (RSS/TSS)
print(f"手工計算 R平方係數 : {R_quare:.2f}")

# 函數計算 R平方係數
# LinearRegression 內含 R平方係數函數,不可使用 sklearn.metrics - r2_score
R_score = model.score(height, weight)
print(f"函數計算 R平方係數 : {R_score:.2f}")
# RSS : 1.82
# TSS : 154.80
# 手工計算 R平方係數 : 0.99
# 函數計算 R平方係數 : 0.99