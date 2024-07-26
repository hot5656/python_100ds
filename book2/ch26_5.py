import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 讀取 csv
data = pd.read_csv('adult.csv')

# 顯示所有 columns
pd.set_option('display.max_columns', None)
# 設定顯示每 row 長度
pd.set_option('display.width', 300)

# 將 ? 轉成 np.nan
data = data.replace('?', np.nan)
# show 檢查資料缺失
# size 48842,max nan 2809
# print(data.info())
# print(data.isnull().sum())
# 刪除包含缺失
data = data.dropna()
# show 檢查資料缺失
# size 45222
# print(data.info())
# print(data.isnull().sum())
# 列出前五筆
print(data.head())
print("-"*180)

# 將類別轉成數字
le = LabelEncoder()
categorical_features = [i for i in data.columns if data.dtypes[i]=='object' ]
for col in categorical_features:
    data[col] = le.fit_transform(data[col])
print(data.head())

#    age  workclass  fnlwgt     education  educational-num      marital-status         occupation   relationship   race gender  capital-gain  capital-loss  hours-per-week native-country income
# 0   25    Private  226802          11th                7       Never-married  Machine-op-inspct      Own-child  Black   Male             0             0              40  United-States  <=50K
# 1   38    Private   89814       HS-grad                9  Married-civ-spouse    Farming-fishing        Husband  White   Male             0             0              50  United-States  <=50K
# 2   28  Local-gov  336951    Assoc-acdm               12  Married-civ-spouse    Protective-serv        Husband  White   Male             0             0              40  United-States   >50K
# 3   44    Private  160323  Some-college               10  Married-civ-spouse  Machine-op-inspct        Husband  Black   Male          7688             0              40  United-States   >50K
# 5   34    Private  198693          10th                6       Never-married      Other-service  Not-in-family  White   Male             0             0              30  United-States  <=50K
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#    age  workclass  fnlwgt  education  educational-num  marital-status  occupation  relationship  race  gender  capital-gain  capital-loss  hours-per-week  native-country  income
# 0   25          2  226802          1                7               4           6             3     2       1             0             0              40              38       0
# 1   38          2   89814         11                9               2           4             0     4       1             0             0              50              38       0
# 2   28          1  336951          7               12               2          10             0     4       1             0             0              40              38       1
# 3   44          2  160323         15               10               2           6             0     2       1          7688             0              40              38       1
# 5   34          2  198693          0                6               4           7             1     4       1             0             0              30              38       0



