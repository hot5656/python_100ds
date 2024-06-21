from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
import numpy as np

#定義特徵
features =[['晴','熱','弱'],
           ['晴','熱','強'],
           ['陰','熱','弱'],
           ['雨','涼','弱'],
           ['雨','冷','弱'],
           ['雨','冷','強'],
           ['陰','冷','強']]

# 將特徵轉為數字編碼
features_encoded = []
for i in range(len(features[0])):
    # 創建 LabelEncoder 物件
    le = LabelEncoder()
    # fit_transform 轉為數值
    feature_encoded = le.fit_transform([row[i] for row in features])
    features_encoded.append(feature_encoded)
# 3*7 陣列,轉成 7*3 陣列
features_encoded = np.array(features_encoded).T
print(f"特徵標籤編碼\n{features_encoded}")
# 特徵標籤編碼
# [[0 2 0]
#  [0 2 1]
#  [1 2 0]
#  [2 1 0]
#  [2 0 0]
#  [2 0 1]
#  [1 0 1]]