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

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=5)

# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier(random_state=5)
dtc.fit(X_train, y_train)
# 進行預測
y_pred = dtc.predict(X_test)

# 準確率
print(f"準確率 : {accuracy_score(y_test, y_pred):.3f}")

# 準確率 : 0.809