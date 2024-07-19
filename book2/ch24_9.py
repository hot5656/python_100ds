import pandas as pd

# 讀取糖尿病數據
df = pd.read_csv('diabetes.csv')

# 顯示所有 columns
pd.set_option('display.max_columns', None)
# 設定顯示每 row 長度
pd.set_option('display.width', 200)
print(df.head())
print("-"*70)

# 設定輸出到第二位小數
pd.set_option('display.float_format', '{:.2f}'.format)
print('輸出數據統計資訊')
print(df.describe())

# 檢查是否有缺失值
print(df.isnull().sum())

#    Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFuncti
# 0            6      148             72             35        0  33.6                     0.6
# 1            1       85             66             29        0  26.6                     0.3
# 2            8      183             64              0        0  23.3                     0.6
# 3            1       89             66             23       94  28.1                     0.1
# 4            0      137             40             35      168  43.1                     2.2
# ----------------------------------------------------------------------
# 輸出數據統計資訊
#        Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin    BMI  DiabetesPedigreeF
# count       768.00   768.00         768.00         768.00   768.00 768.00
# mean          3.85   120.89          69.11          20.54    79.80  31.99
# 50%           3.00   117.00          72.00          23.00    30.50  32.00                      0.37  29.00     0.00
# 75%           6.00   140.25          80.00          32.00   127.25  36.60                      0.63  41.00     1.00
# max          17.00   199.00         122.00          99.00   846.00  67.10                      2.42  81.00     1.00
# Pregnancies                 0
# Glucose                     0
# BloodPressure               0
# SkinThickness               0
# Insulin                     0
# BMI                         0
# DiabetesPedigreeFunction    0
# Age                         0
# Outcome                     0
# dtype: int64
