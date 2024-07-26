# 特徵之重要性
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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

# 建立模型
# n_estimators 設計隨機森林有機棵樹,更多的樹可能會有更好的性能
#              但也同時增加訓練時間及模型的大小(default 100)
# max_depth=5  深度設定
dtc = RandomForestClassifier(random_state=5)
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

# 特徵 : age                  重要性 : 0.14788601176311628
# 特徵 : workclass            重要性 : 0.039373980352075864
# 特徵 : fnlwgt               重要性 : 0.1767862474791546
# 特徵 : education            重要性 : 0.03347647561822924
# 特徵 : educational-num      重要性 : 0.08791872053411558
# 特徵 : marital-status       重要性 : 0.07155425751264902
# 特徵 : occupation           重要性 : 0.06447423433400915
# 特徵 : relationship         重要性 : 0.09680354514661552
# 特徵 : race                 重要性 : 0.014029502750118635
# 特徵 : gender               重要性 : 0.01437132602637792
# 特徵 : capital-gain         重要性 : 0.1133902372001231
# 特徵 : capital-loss         重要性 : 0.03873718364115498
# 特徵 : hours-per-week       重要性 : 0.08301042307861366
# 特徵 : native-country       重要性 : 0.018187854563646542