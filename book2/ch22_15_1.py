# 精確度
from sklearn.metrics import accuracy_score

y_true = [1, 1, 2, 2, 3, 3]
y_pred = [1, 1, 2, 2, 3, 2]

print(f"Accuacy Score : {accuracy_score(y_true, y_pred)}")
# Accuacy Score : 0.8333333333333334