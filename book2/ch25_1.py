from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# 定義特徵和目標變數
features = [['晴','熱','弱'],['晴','熱','強'],['陰','熱','弱'],
            ['雨','涼','弱'],['雨','冷','弱'],['雨','冷','強'],
            ['陰','冷','強']]
labels = ['是','否','是','是','否','否','是']

label_encoders = []
features_encoded = []
# 將特徵變數轉為數字編碼
for i in range(len(features[0])):
    # 特徵編碼
    le = LabelEncoder()
    feature_encoded = le.fit_transform([row[i] for row in features])
    features_encoded.append(feature_encoded)
    # 紀錄文字轉數字公式(1)
    label_encoders.append(le)
# 3*7 array 轉成 7*3
features_encoded = np.array(features_encoded).T
print(f"特徵標籤編碼:\n{features_encoded}")

# 將目標變數轉為數字編碼
label_encoder_label = LabelEncoder()
labels_encoded = label_encoder_label.fit_transform(labels)
print(f"目標變數編碼:\n{labels_encoded}")

# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier()
dtc.fit(features_encoded, labels_encoded)

# 用新的觀察值來進行預測
test_features = [['晴','涼','弱']]
# 建立二維 0 矩陣
test_features_encoded = np.zeros((1, len(test_features[0])))
# print(test_features_encoded)

for i in range(len(test_features[0])):
    # 利用 文字轉數字公式(1) 設定對應值
    test_features_encoded[0, i] = label_encoders[i].transform([test_features[0][i]])[0]
print(f'測試數據編碼\n{test_features_encoded}')

# 輸出預測數字標籤
pred = dtc.predict(test_features_encoded)
print(f'預測結果 : {pred}')

# 轉換輸出數字為文字
print(f'預測結果 : {label_encoder_label.inverse_transform(pred)[0]}')

# 特徵標籤編碼:
# [[0 2 0]
#  [0 2 1]
#  [1 2 0]
#  [2 1 0]
#  [2 0 0]
#  [2 0 1]
#  [1 0 1]]
# 目標變數編碼:
# [1 0 1 1 0 0 1]
# 測試數據編碼
# [[0. 1. 0.]]
# 預測結果 : [1]
# 預測結果 : 是