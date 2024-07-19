# 繪出特徵值
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 讀取數據
data = pd.read_csv('UCI_Credit_Card.csv')

# # 顯示所有 columns
# pd.set_option('display.max_columns', None)
# # 設定顯示每 row 長度
# pd.set_option('display.width', 300)
# print(data.head())

# 定義特徵和目標變數
features = data.drop(["ID", "default.payment.next.month"], axis=1)
X = features
y = data["default.payment.next.month"]

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=10)

# 特徵縮放(標準化)
# fit_transform 用於訓練數據：
#     fit 計算訓練數據的均值和方差
#     transform 使用這些計算出的均值和方差對訓練數據進行標準化
# transform 用於測試數據：
#     只使用訓練數據計算出的均值和方差來標準化測試數據，不會重新計算均值和方差
# 這樣做是為了避免數據洩漏，確保測試數據的標準化過程不受訓練數據的影響，同時保持測試數據的獨立性和真實性
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 建立邏輯迴歸模型 + 使用訓練集訓練模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 獲取特徵重要性
importance = model.coef_[0]

# 總結特徵重要性
for i, score in enumerate(importance):
    print(f"特徵: {features.columns[i]:10s}, 分數: {score:.5f}")

# 繪製特徵重要性
plt.figure(figsize=(10,6))
plt.bar([x for x in range(len(importance))], importance)
# plt.xticks([x for x in range(len(importance))], features, rotation='vertical')
plt.xticks([x for x in range(len(importance))], features, rotation=90)
plt.xticks()
plt.title('UCI_Credit_Card.csv')
plt.show()

# 特徵: LIMIT_BAL , 分數: -0.09251
# 特徵: SEX       , 分數: -0.05675
# 特徵: EDUCATION , 分數: -0.07002
# 特徵: MARRIAGE  , 分數: -0.08346
# 特徵: AGE       , 分數: 0.06998
# 特徵: PAY_0     , 分數: 0.63988
# 特徵: PAY_2     , 分數: 0.10731
# 特徵: PAY_3     , 分數: 0.09626
# 特徵: PAY_4     , 分數: 0.01599
# 特徵: PAY_5     , 分數: 0.03251
# 特徵: PAY_6     , 分數: 0.02136
# 特徵: BILL_AMT1 , 分數: -0.41557
# 特徵: BILL_AMT2 , 分數: 0.20846
# 特徵: BILL_AMT3 , 分數: 0.08524
# 特徵: BILL_AMT4 , 分數: 0.03273
# 特徵: BILL_AMT5 , 分數: -0.05235
# 特徵: BILL_AMT6 , 分數: 0.04633
# 特徵: PAY_AMT1  , 分數: -0.24341
# 特徵: PAY_AMT2  , 分數: -0.19772
# 特徵: PAY_AMT3  , 分數: -0.05722
# 特徵: PAY_AMT4  , 分數: -0.07154
# 特徵: PAY_AMT5  , 分數: -0.04787
# 特徵: PAY_AMT6  , 分數: -0.02067