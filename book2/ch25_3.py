from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

# load 葡萄酒數據
wine = load_wine()
# 取前兩個特徵
X = wine.data[:,:2]

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, wine.target, test_size=0.2, random_state=9)

# 建立決策樹模型並進行訓練(max_depth=1)
dtc1 = DecisionTreeClassifier(max_depth=1)
dtc1.fit(X_train, y_train)
# 進行預測
y_pred = dtc1.predict(X_test)
# 預測結果比較
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"測試的目標分類\n{y_pred}")
print("-"*70)
print(f"max_depth=1 測試數據準確率 : {dtc1.score(X_test, y_test):.2f}")
print("="*70)

# 建立決策樹模型並進行訓練(max_depth=3)
dtc3 = DecisionTreeClassifier(max_depth=3)
dtc3.fit(X_train, y_train)
# 進行預測
y_pred = dtc3.predict(X_test)
# 預測結果比較
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"測試的目標分類\n{y_pred}")
print("-"*70)
print(f"max_depth=1 測試數據準確率 : {dtc3.score(X_test, y_test):.2f}")
print("="*70)

# 儲存公式
# add feature name and class_names
feature_names = ['alcohol','malic_acid']
class_names = ['Barolo','Grignolino','Barbera']
dump((dtc3, feature_names, class_names), 'dtc3.joblib')

# 儲存公式
# default feature name, no class name
# dump(dtc3, 'dtc3.joblib')

# 測試的真實分類
# [0 0 0 2 0 0 2 2 2 1 2 0 2 1 1 0 1 1 0 0 0 0 0 0 0 2 1 1 0 1 0 1 1 0 1 2]
# ----------------------------------------------------------------------
# 測試的目標分類
# [0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 0 1 1 0 0 0 0 0 0 0 0 1 1 0 1 0 1 1 0 1 0]
# ----------------------------------------------------------------------
# max_depth=1 測試數據準確率 : 0.78
# ======================================================================
# 測試的真實分類
# [0 0 0 2 0 0 2 2 2 1 2 0 2 1 1 0 1 1 0 0 0 0 0 0 0 2 1 1 0 1 0 1 1 0 1 2]
# ----------------------------------------------------------------------
# 測試的目標分類
# [0 0 0 2 0 0 0 2 1 1 1 0 1 1 1 0 1 1 0 0 0 0 0 0 0 2 1 1 0 1 0 1 1 0 1 2]
# ----------------------------------------------------------------------
# max_depth=1 測試數據準確率 : 0.89
# ======================================================================

