# 載入模型 - joblib(scikit-learn建議)
from joblib import load

# 載入模型
model = load("model_ch22_11.joblib")

h = int(input("輸入身高(cm):"))
h /= 100
weight_pred = model.predict([[h]])
print(weight_pred)
print(f"預測體重: {weight_pred[0]:.2f} 公斤")
# 輸入身高(cm):175
# [65.61463415]
# 預測體重: 65.61 公斤