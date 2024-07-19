import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 讀取數據
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# remove field ID
df = df.drop(['customerID'], axis=1)

# 標籤轉成數值
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        if column != 'TotalCharges':
            # 列出原符號和對應的數值
            label_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
            print(f"{column} {label_mapping}")

# show 數據統計資料及檢查資料缺失
print(df.isnull().info())
print(df.isnull().sum())

# 刪除缺失值,處理缺失數據(本例其實不需要)
df= df.dropna()

# show 數據統計資料及檢查資料缺失
# print(df.isnull().info())
# print(df.isnull().sum())

# show 5 records
print(df.head())


# gender {'Female': 0, 'Male': 1}
# Partner {'No': 0, 'Yes': 1}
# Dependents {'No': 0, 'Yes': 1}
# PhoneService {'No': 0, 'Yes': 1}
# MultipleLines {'No': 0, 'No phone service': 1, 'Yes': 2}
# InternetService {'DSL': 0, 'Fiber optic': 1, 'No': 2}
# OnlineSecurity {'No': 0, 'No internet service': 1, 'Yes': 2}
# OnlineBackup {'No': 0, 'No internet service': 1, 'Yes': 2}
# DeviceProtection {'No': 0, 'No internet service': 1, 'Yes': 2}
# TechSupport {'No': 0, 'No internet service': 1, 'Yes': 2}
# StreamingTV {'No': 0, 'No internet service': 1, 'Yes': 2}
# StreamingMovies {'No': 0, 'No internet service': 1, 'Yes': 2}
# Contract {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
# PaperlessBilling {'No': 0, 'Yes': 1}
# PaymentMethod {'Bank transfer (automatic)': 0, 'Credit card (automatic)': 1, 'Electronic check': 2, 'Mailed check': 3}
# Churn {'No': 0, 'Yes': 1}
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7043 entries, 0 to 7042
# Data columns (total 20 columns):
#  #   Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
#  0   gender            7043 non-null   bool
#  1   SeniorCitizen     7043 non-null   bool
#  2   Partner           7043 non-null   bool
#  3   Dependents        7043 non-null   bool
#  4   tenure            7043 non-null   bool
#  5   PhoneService      7043 non-null   bool
#  6   MultipleLines     7043 non-null   bool
#  7   InternetService   7043 non-null   bool
#  8   OnlineSecurity    7043 non-null   bool
#  9   OnlineBackup      7043 non-null   bool
#  10  DeviceProtection  7043 non-null   bool
#  11  TechSupport       7043 non-null   bool
#  12  StreamingTV       7043 non-null   bool
#  13  StreamingMovies   7043 non-null   bool
#  14  Contract          7043 non-null   bool
#  15  PaperlessBilling  7043 non-null   bool
#  16  PaymentMethod     7043 non-null   bool
#  17  MonthlyCharges    7043 non-null   bool
#  18  TotalCharges      7043 non-null   bool
#  19  Churn             7043 non-null   bool
# dtypes: bool(20)
# memory usage: 137.7 KB
# None
# gender              0
# SeniorCitizen       0
# Partner             0
# Dependents          0
# tenure              0
# PhoneService        0
# MultipleLines       0
# InternetService     0
# OnlineSecurity      0
# OnlineBackup        0
# DeviceProtection    0
# TechSupport         0
# StreamingTV         0
# StreamingMovies     0
# Contract            0
# PaperlessBilling    0
# PaymentMethod       0
# MonthlyCharges      0
# TotalCharges        0
# Churn               0
# dtype: int64
#    gender  SeniorCitizen  Partner  Dependents  ...  PaymentMethod  MonthlyCharges  TotalCharges  Churn
# 0       0              0        1           0  ...              2           29.85          2505      0
# 1       1              0        0           0  ...              3           56.95          1466      0
# 2       1              0        0           0  ...              3           53.85           157      1
# 3       1              0        0           0  ...              0           42.30          1400      0
# 4       0              0        0           0  ...              2           70.70           925      1