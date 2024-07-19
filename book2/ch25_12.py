import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

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
    train_test_split(df[selected_features], df[target], test_size=0.3, random_state=5)

# 建立決策樹模型並進行訓練
# dtc = DecisionTreeClassifier()
# max_depth=5
print("max_depth=5")
dtc = DecisionTreeClassifier(max_depth=5)
dtc.fit(X_train, y_train)

# 進行預測
y_pred = dtc.predict(X_test)

# 準確率
print(f"準確率 : {dtc.score(X_test, y_test):.2f}")

# 計算混淆矩陣並輸出
# 測試準確對照表
conf_mat = confusion_matrix(y_test, y_pred)
print(f"混淆矩陣(Confusion Matix):\n{conf_mat}")
print("-"*70)

# 生成分類報告
# 測試報告
report = classification_report(y_test, y_pred)
print(f"分類報告(Classification Report)\n{report}")

# max_depth=5
# 準確率 : 0.79
# 混淆矩陣(Confusion Matix):
# [[1337  207]
#  [ 234  335]]
# ----------------------------------------------------------------------
# 分類報告(Classification Report)
#               precision    recall  f1-score   support
#            0       0.85      0.87      0.86      1544
#            1       0.62      0.59      0.60       569
#     accuracy                           0.79      2113
#    macro avg       0.73      0.73      0.73      2113
# weighted avg       0.79      0.79      0.79      2113