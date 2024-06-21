# 召回率:計算正類別標籤正確比例
from sklearn.metrics import recall_score

y_true = [1, 1, 0, 0, 1, 1]
y_pred = [1, 0, 0, 0, 1, 1]
print(f"Recall Score : {recall_score(y_true, y_pred)}")
# 正類別標籤(1)有4個,正確預測3個
# Recall Score : 0.75
