import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
# from sklearn.metrics import confusion_matrix
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
    train_test_split(df[selected_features], df[target], test_size=0.2, random_state=1)

# 設定調整參數
params = {'max_depth': [3, 4, 5, 6, 7, 10, 15, 20]}
# 建立決策樹模型
clf = GridSearchCV(DecisionTreeClassifier(), params, cv=5)
clf.fit(X_train, y_train)
# 顯示最佳參數
print(f"Best parameters:{clf.best_params_}")
print("-"*70)
# 進行預測
y_pred = clf.predict(X_test)
# 準確率
print(f"準確率 : {accuracy_score(y_test, y_pred)}")
print("-"*70)
# 生成分類報告
# 測試報告
print(classification_report(y_test, y_pred))

# Best parameters:{'max_depth': 5}
# ----------------------------------------------------------------------
# 準確率 : 0.8090844570617459
# ----------------------------------------------------------------------
#               precision    recall  f1-score   support
#            0       0.85      0.91      0.88      1061
#            1       0.64      0.51      0.57       348
#     accuracy                           0.81      1409
#    macro avg       0.75      0.71      0.72      1409
# weighted avg       0.80      0.81      0.80      1409