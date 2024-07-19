import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, roc_auc_score

# 讀取糖尿病數據
df = pd.read_csv('new_diabetes.csv')

# 定義特徵及目標變數
X = df.drop(["Outcome"], axis=1)
y = df["Outcome"]

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=5)

# 特徵縮放(標準化)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 建立邏輯迴歸模型 + 使用訓練集訓練模型
model = LogisticRegression()
model.fit(X_train, y_train)

# # 訓練集進行預測並計算準確率
# train_pred = model.predict(X_train)
# train_accuracy = accuracy_score(y_train, train_pred)
# print(f"訓練集數據準確率 Accuracy: {train_accuracy*100:.2f}%")
# # 測試集進行預測並計算準確率
# test_pred = model.predict(X_test)
# test_accuracy = accuracy_score(y_test, test_pred)
# print(f"測試集數據準確率 Accuracy: {test_accuracy*100:.2f}%")

# 測試集進行預測並計算準確率
y_pred = model.predict(X_test)
# Series 轉成 array
print(f"測試真實分類\n{y_test.to_numpy()}")
print("-"*70)
print(f"測試預測分類\n{y_pred}")
print("="*70)

# 列印準確率
print(f"Accuracy: {accuracy_score(y_test, y_pred):.5f}")
print("="*70)

# 計算混淆矩陣並輸出
# 測試準確對照表
conf_mat = confusion_matrix(y_test, y_pred)
print(f"混淆矩陣(Confusion Matix):\n{conf_mat}")
print("="*70)

# 預測採集樣本為正類的機率
# AUC-ROC（Area Under the Receiver Operating Characteristic Curve）分數
# 是一種評估二分類模型性能的指標。它表示模型區分正類和負類的能力，範圍從0.0到
# 1.0，1.0表示完美區分，0.5表示隨機猜測。
# model.predict_proba(X_test)[:,0]表為0的機率, model.predict_proba(X_test)[:,1]表為1的機率
y_pred_prob = model.predict_proba(X_test)[:,1]
print(f"AOC-ROC: {roc_auc_score(y_test, y_pred_prob):.5f}")

# 測試真實分類
# [0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0
#  1 0 0 1 0 0 0 0 1 1 0 0 1 1 0 1 1 0 1 0 0 0 0 1 0 1 0 1 0 0 1 0 1 1 0 0 1
#  1 0 0 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 1 1 0 1 0 0 1 0 0
#  1 0 0 0 0 0 1 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 1 0 1 0 0 1 1 1 0 0 1 1
#  0 0 1 0 0 0]
# ----------------------------------------------------------------------
# 測試預測分類
# [0 0 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0
#  0 0 0 0 0 0 1 0 1 1 0 0 0 1 0 1 0 0 1 0 0 0 0 1 1 1 0 1 0 0 0 1 0 1 0 0 1
#  1 0 0 1 1 0 0 1 1 1 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 0 1 1 0 1 0 0 1 0 0
#  1 0 0 0 0 0 1 0 0 1 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 1 0 1 0 0 0 0
#  0 0 1 0 0 1]
# ======================================================================
# Accuracy: 0.82468
# ======================================================================
# 混淆矩陣(Confusion Matix):
# [[91  9]
#  [18 36]]
# ======================================================================
# AOC-ROC: 0.87019

