# 計算預估房價
from joblib import load
import pandas as pd
import numpy as np

# 載入模型
model = load('boston_model.joblib')
lstat = eval(input("請輸入低收入比例 : "))
rooms = eval(input("請輸入房間數     :"))

# 用 模型計算房價
data  = pd.DataFrame(np.c_[[lstat], [rooms]], columns =['LSTAT', 'RM'])
price_pred = model.predict(data)
print(f"用模型計算房價     : {price_pred[0]:.2f}")

# 用 迴歸公式計算房價
intercept = model.intercept_
coeff = model.coef_
price_cal = intercept + coeff[0] * lstat + coeff[1] * rooms
print(f"用迴歸公式計算房價 : {price_cal:.2f}")
# 請輸入低收入比例 : 4.98
# 請輸入房間數     :6
# 用模型計算房價     : 26.44
# 用迴歸公式計算房價 : 26.44
