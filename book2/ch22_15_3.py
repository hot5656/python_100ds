# F1 分數:精確率(precision)和召回率(recall)的平均數
from sklearn.metrics import f1_score

y_true = [1, 1, 0, 0, 1, 1]
y_pred = [1, 0, 0, 0, 1, 1]
print(f"F1 Score : {f1_score(y_true, y_pred)}")
# F1 Score : 0.8571428571428571