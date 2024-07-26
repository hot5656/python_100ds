import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 選擇特及目標變數
selected_features = ['Contract','tenure','OnlineSecurity',
                     'InternetService','MonthlyCharges']
target = 'Churn'

# 標籤轉成數值
for column in selected_features:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
# 目標變數轉成數值
labsel_encoder_target = LabelEncoder()
df[target] = labsel_encoder_target.fit_transform(df[target])

X_train, X_test, y_train, y_test = \
    train_test_split(df[selected_features], df[target], test_size=0.2, random_state=1)


# 建立模型
# n_estimators 設計隨機森林有機棵樹,更多的樹可能會有更好的性能
#              但也同時增加訓練時間及模型的大小(default 100)
# max_depth=5
dtc = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
dtc.fit(X_train, y_train)
# 進行預測
y_pred = dtc.predict(X_test)

# 準確率
print(f"準確率 : {dtc.score(X_test, y_test)}")

# 生成分類報告
# 測試報告
report = classification_report(y_test, y_pred)
print(f"分類報告(Classification Report)\n{report}")

# 準確率 : 0.8062455642299503
# 分類報告(Classification Report)
#               precision    recall  f1-score   support
#            0       0.85      0.91      0.88      1061
#            1       0.64      0.49      0.56       348
#     accuracy                           0.81      1409
#    macro avg       0.74      0.70      0.72      1409
# weighted avg       0.79      0.81      0.80      1409
