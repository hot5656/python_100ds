import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# load 數據
titanic_data = sns.load_dataset('titanic')
# 選取有用特徵
titanic_data = titanic_data[['survived','pclass','sex','age','sibsp',
                 'parch','fare','embarked']]

# print(titanic_data)
# print(titanic_data['age'])
# 年齡補上中位數年齡
titanic_data['age'] = titanic_data['age'].fillna(titanic_data['age'].median())
# 登船港口用眾位數取代缺失值
# mode() 傳回的是一個包含眾數的 Series，因此需要取 [0] 來獲取第一個眾數
titanic_data['embarked'] = titanic_data['embarked'].fillna(titanic_data['embarked'].mode()[0])

# 對性別,登船港口 執行 on-hot 編碼
# get_dummies 是 Pandas 中的一個函數，用於將分類變數轉換為一個或多個虛擬變數（dummy variables）。
# 這些虛擬變數可以用於機器學習模型，因為大多數模型不能直接處理非數值型資料。
titanic_data = pd.get_dummies(titanic_data, columns=['sex', 'embarked'])

# 分割數據為訓練集及測試集
X = titanic_data.drop('survived', axis=1)
y = titanic_data['survived']
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=5)

print(titanic_data.head())

# 建立決策樹模型並進行訓練
dtc = DecisionTreeClassifier(random_state=5)
dtc.fit(X_train, y_train)

# 進行預測
y_pred = dtc.predict(X_test)

# 預測結果比較
print(f"測試的真實分類\n{y_test.to_numpy()}")
print("-"*70)
print(f"測試的目標分類\n{y_pred}")
print("="*70)

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

#    survived  pclass   age  sibsp  parch     fare  sex_female  sex_male  embarked_C  embarked_Q  embarked_S
# 0         0       3  22.0      1      0   7.2500       False      True       False       False        True
# 1         1       1  38.0      1      0  71.2833        True     False        True       False       False
# 2         1       3  26.0      0      0   7.9250        True     False       False       False        True
# 3         1       1  35.0      1      0  53.1000        True     False       False       False        True
# 4         0       3  35.0      0      0   8.0500       False      True       False       False        True
# 測試的真實分類
# [0 0 0 1 0 0 1 1 1 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0
#  1 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 0 0
#  0 0 0 0 1 1 0 0 0 0 1 1 0 1 0 1 0 0 1 0 1 0 1 0 0 0 1 0 0 0 1 1 0 0 0 1 0
#  0 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 1
#  0 1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 1 0 0 0 1 0 1 1 0 0 0 1 0]
# ----------------------------------------------------------------------
# 測試的目標分類
# [0 0 0 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 1 1 0 0 0 0 1 0 0 0 1 0 0 1 1 0
#  0 0 0 0 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 1 0
#  1 0 0 0 1 1 0 0 0 0 1 1 0 1 0 1 1 0 1 0 1 0 1 0 0 0 1 1 0 0 1 1 0 0 0 1 0
#  0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 1 1 1
#  0 0 1 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 1 0 1 1 0 0 0 1 0]
# ======================================================================
# 準確率 : 0.82
# 混淆矩陣(Confusion Matix):
# 111位沒有存活: 98正確 19錯誤
# 62位存活: 19正確 13錯誤
# [[98 13]
#  [19 49]]
# ----------------------------------------------------------------------
# 分類報告(Classification Report)
#               precision    recall  f1-score   support
#            0       0.84      0.88      0.86       111
#            1       0.79      0.72      0.75        68
#     accuracy                           0.82       179
#    macro avg       0.81      0.80      0.81       179
# weighted avg       0.82      0.82      0.82       179