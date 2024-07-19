from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix

# load 葡萄酒數據
wine = load_wine()

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(wine.data, wine.target, test_size=0.2, random_state=9)

# 建立邏輯迴歸分類器,使用 OvR
# multi_class: ovr, multination and auto
# max_iter 最大迭代數,達到後將停止最佳化,default 100
log_reg = LogisticRegression(multi_class='ovr', max_iter=10000)

# 訓練分類器
log_reg.fit(X_train, y_train)

# 進行預測
y_pred = log_reg.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"測試的目標分類\n{y_pred}")
print("="*70)

# 計算準確度
acc = accuracy_score(y_test, y_pred)
print(f"準確度(Accuracy Score):{acc:.2f}")
print("-"*70)

# 計算混淆矩陣並輸出
# 測試準確對照表
conf_mat = confusion_matrix(y_test, y_pred)
print(f"混淆矩陣(Confusion Matix):\n{conf_mat}")
print("-"*70)

# 生成分類報告
# 測試報告
report = classification_report(y_test, y_pred)
print(f"分類報告(Classification Report)\n{report}")

# 測試的真實分類
# [0 0 0 2 0 0 2 2 2 1 2 0 2 1 1 0 1 1 0 0 0 0 0 0 0 2 1 1 0 1 0 1 1 0 1 2]
# ----------------------------------------------------------------------
# 測試的目標分類
# [0 0 0 2 0 0 2 2 2 1 2 0 2 1 1 0 1 1 0 0 0 0 0 0 0 2 1 1 0 1 0 1 1 0 1 2]
# ======================================================================
# 準確度(Accuracy Score):1.00
# ----------------------------------------------------------------------
# 混淆矩陣(Confusion Matix):
# [[17  0  0]
#  [ 0 11  0]
#  [ 0  0  8]]
# ----------------------------------------------------------------------
# 分類報告(Classification Report)
#               precision    recall  f1-score   support
#            0       1.00      1.00      1.00        17
#            1       1.00      1.00      1.00        11
#            2       1.00      1.00      1.00         8
#     accuracy                           1.00        36
#    macro avg       1.00      1.00      1.00        36
# weighted avg       1.00      1.00      1.00        36




