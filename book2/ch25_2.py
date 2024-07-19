from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# load 葡萄酒數據
wine = load_wine()

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(wine.data, wine.target, test_size=0.2, random_state=9)

# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

# 進行預測
y_pred = dtc.predict(X_test)

# 預測結果比較
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"測試的目標分類\n{y_pred}")
print("="*70)
print(f"測試第1個標籤         :{y_pred[0]}")
print(f"測試第1個標籤各分類機率:{dtc.predict_proba(X_test[:1])}")
print("="*70)

# 列印準確率
print(f"方法1 測試數據準確率 : {accuracy_score(y_test, y_pred)}")

# 另一方法準確率
print(f"方法2 訓練數據準確率 : {dtc.score(X_train, y_train)}")
print(f"方法2 測試數據準確率 : {dtc.score(X_test, y_test)}")

# 測試的真實分類
# [0 0 0 2 0 0 2 2 2 1 2 0 2 1 1 0 1 1 0 0 0 0 0 0 0 2 1 1 0 1 0 1 1 0 1 2]
# ----------------------------------------------------------------------
# 測試的目標分類
# [0 0 0 2 0 0 2 2 2 1 2 0 2 1 1 0 1 1 0 1 0 0 0 0 0 2 1 1 0 1 0 1 1 0 1 2]
# ======================================================================
# 測試第1個標籤         :0
# 測試第1個標籤各分類機率:[[1. 0. 0.]]
# ======================================================================
# 方法1 測試數據準確率 : 0.9722222222222222
# 方法2 訓練數據準確率 : 1.0
# 方法2 測試數據準確率 : 0.9722222222222222
