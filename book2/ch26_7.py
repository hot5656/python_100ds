# 特徵之重要性
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

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
    train_test_split(X, y, test_size=0.2, random_state=42)

# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier(random_state=5)
dtc.fit(X_train, y_train)
# 進行預測
y_pred = dtc.predict(X_test)

# 輸出特徵重要性
importances = dtc.feature_importances_
for feat, importance in zip(X.columns, importances):
    print(f"特徵 : {feat:20s} 重要性 : {importance}" )

feature_imp = pd.Series(dtc.feature_importances_,
                index=X.columns).sort_values(ascending=False)
feature_imp.plot(kind='bar')
plt.show()

# 特徵 : age                  重要性 : 0.11978703368273183
# 特徵 : workclass            重要性 : 0.032764901917090215
# 特徵 : fnlwgt               重要性 : 0.2056924305712409
# 特徵 : education            重要性 : 0.0129702048255056
# 特徵 : educational-num      重要性 : 0.11355184888333343
# 特徵 : marital-status       重要性 : 0.006535999243215993
# 特徵 : occupation           重要性 : 0.0539721412011748
# 特徵 : relationship         重要性 : 0.1987225583756099
# 特徵 : race                 重要性 : 0.013271473606213178
# 特徵 : gender               重要性 : 0.0021772976656923393
# 特徵 : capital-gain         重要性 : 0.11284501812585948
# 特徵 : capital-loss         重要性 : 0.04032376245073732
# 特徵 : hours-per-week       重要性 : 0.07132449271050804
# 特徵 : native-country       重要性 : 0.0160608367410867