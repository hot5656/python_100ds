import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

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
    train_test_split(X, y, test_size=0.3, random_state=5)

# 建立決策樹模型並進行訓練
# max_depth=5
print("max_depth=5")
dtc = DecisionTreeClassifier(max_depth=5)
dtc.fit(X_train, y_train)

# 輸出特徵重要性
importances = dtc.feature_importances_
for feat, importance in zip(X.columns, importances):
    print(f"特徵 : {feat:20s} 重要性 : {importance}" )

feature_imp = pd.Series(dtc.feature_importances_,
                index=X.columns).sort_values(ascending=False)
feature_imp.plot(kind='bar')
plt.show()

# max_depth=5
# 特徵 : customerID           重要性 : 0.00910320798378901
# 特徵 : gender               重要性 : 0.0
# 特徵 : SeniorCitizen        重要性 : 0.0
# 特徵 : Partner              重要性 : 0.0
# 特徵 : Dependents           重要性 : 0.0
# 特徵 : tenure               重要性 : 0.1548386776499358
# 特徵 : PhoneService         重要性 : 0.0
# 特徵 : MultipleLines        重要性 : 0.0
# 特徵 : InternetService      重要性 : 0.08820670934335376
# 特徵 : OnlineSecurity       重要性 : 0.15018233747881019
# 特徵 : OnlineBackup         重要性 : 0.0
# 特徵 : DeviceProtection     重要性 : 0.0
# 特徵 : TechSupport          重要性 : 0.0
# 特徵 : StreamingTV          重要性 : 0.00531089171150569
# 特徵 : StreamingMovies      重要性 : 0.0
# 特徵 : Contract             重要性 : 0.5228059535911008
# 特徵 : PaperlessBilling     重要性 : 0.006369190962804586
# 特徵 : PaymentMethod        重要性 : 0.0
# 特徵 : MonthlyCharges       重要性 : 0.05825142168000398
# 特徵 : TotalCharges         重要性 : 0.004931609598696093
