import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# remove field ID
# df = df.drop(['customerID'], axis=1)

# 標籤轉成數值
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        # if column != 'TotalCharges':
        #     # 列出原符號和對應的數值
        #     label_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
        #     print(f"{column} {label_mapping}")

X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# 建立決策樹模型並進行訓練
# dtc = DecisionTreeClassifier()
# max_depth=5
print("max_depth=5")
dtc = DecisionTreeClassifier(max_depth=5)
dtc.fit(X_train, y_train)

# 進行預測
y_pred = dtc.predict(X_test)

# 準確率
print(f"準確率 : {dtc.score(X_test, y_test)}")

# 計算混淆矩陣並輸出
# 測試準確對照表
conf_mat = confusion_matrix(y_test, y_pred)
print(f"混淆矩陣(Confusion Matix):\n{conf_mat}")
print("-"*70)

# 生成分類報告
# 測試報告
report = classification_report(y_test, y_pred)
print(f"分類報告(Classification Report)\n{report}")

# 準確率 : 0.73
# 混淆矩陣(Confusion Matix):
# [[1267  277]
#  [ 287  282]]
# ----------------------------------------------------------------------
# 分類報告(Classification Report)
#               precision    recall  f1-score   support
#            0       0.82      0.82      0.82      1544 --> 預測顧客未流失精確度 0.82
#            1       0.50      0.50      0.50       569 --> 預測顧客流失精確度   0.5
#     accuracy                           0.73      2113
#    macro avg       0.66      0.66      0.66      2113
# weighted avg       0.73      0.73      0.73      2113

# max_depth=5
# 準確率 : 0.8048261178140526
# 混淆矩陣(Confusion Matix):
# [[953 108]
#  [167 181]]
# ----------------------------------------------------------------------
# 分類報告(Classification Report)
#               precision    recall  f1-score   support
#            0       0.85      0.90      0.87      1061
#            1       0.63      0.52      0.57       348
#     accuracy                           0.80      1409
#    macro avg       0.74      0.71      0.72      1409
# weighted avg       0.80      0.80      0.80      1409
