import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 讀取 csv
data = pd.read_csv('adult.csv')

# 將 ? 轉成 np.nan
data = data.replace('?', np.nan)

# 將類別轉成數字
le = LabelEncoder()
categorical_features = [i for i in data.columns if data.dtypes[i]=='object' ]
for col in categorical_features:
    data[col] = le.fit_transform(data[col])

# 特徵值及目標值
X = data.drop('income', axis=1)
y = data['income']

# 使用所有特徵訓練決策樹並計算特徵重要性
dtc = DecisionTreeClassifier(random_state=5)
dtc.fit(X, y)
importances = dtc.feature_importances_
features = X.columns

# 獲得最重要7個特徵
# p.argsort 取出由小到大 array's index
indices = np.argsort(importances)[-7:]
# top 7 features' name
top_features = [features[i] for i in indices]

X = data[top_features]
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=5)

# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier(random_state=5)
dtc.fit(X_train, y_train)
# 進行預測
y_pred = dtc.predict(X_test)

# 準確率
print(f"準確率 : {accuracy_score(y_test, y_pred):.3f}")

# 準確率 : 0.803
