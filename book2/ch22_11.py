# 模型儲存 - joblib(scikit-learn建議)
from joblib import dump
from sklearn.linear_model import LinearRegression
import numpy as np

# reshape(-1,1) 將一維陣列轉為二維陣列
height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

# 建立線性回歸模型
model = LinearRegression()
# model.fit(X=height, y=weight) 做數據擬合, X必需為二維陣列
model.fit(X=height, y=weight)

# 模型儲存
dump(model, "model_ch22_11.joblib")