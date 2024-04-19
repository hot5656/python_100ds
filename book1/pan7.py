# 數值處理 - NaN 空值
import pandas as pd

# NaN 表 空值
# isnull() : check NaN
# fillna(value, method): NaN 填入指定值
# dropna(): NaN 刪除
df = pd.read_csv('customer.csv')
print(df)
print('column NaN 統計:', df.isnull().sum())
print('index 有 NaN 的筆數', df.isnull().any(axis=1).sum())
print('column 有 NaN 的筆數', df.isnull().any(axis=0).sum())
print('age NaN 的紀錄:',df[df['age'].isnull()])
#          id name  gender   age    area         job
# 0   1700001  李國發    Male  21.0  新北市三重區   金融業 和房地產
# 1   1700002  吳俊諺     NaN   NaN  臺北市文山區     金融業和房地產
# 2   1700003  蔡俊毅     NaN   NaN  臺北市文山區    教育體育  文化
# 3   1700004  姚鈺迪  Female  34.0  基隆市中正區    住宿 和 餐飲業
# 4   1700004  姚鈺迪  Female  34.0  基隆市中正區      住宿和餐飲業
# 5   1700005  袁劭彥    Male  42.0  臺北市文山區     金融業和房地產
# 6   1700006  蔡登意     NaN   NaN     NaN     金融業和房地產
# 7   1700007  吳景翔     NaN  39.0     NaN       農林牧漁業
# 8   1700008  邱孝信     NaN  39.0     NaN     金融業和房地產
# 9   1700009  陳明輝     NaN  57.0  基隆市中正區     金融業和房地產
# 10  1700010  彭郁翔     NaN  55.0  基隆市中正區      住宿和餐飲業
# 11  1700011  許合蓉  Female  61.0  新北市三重區      住宿和餐飲業
# 12  1700012  武家豪    Male  53.0  新北市三重區       農林牧漁業
# 13  1700013  郭信邦     NaN  48.0  新北市三重區      教育體育文化
# 14  1700014  周聿綠  Female  57.0  基隆市中正區     金融業和房地產
# column NaN 統計:
# id        0
# name      0
# gender    8
# age       3
# area      3
# job       0
# dtype: int64
# index 有 NaN 的筆數 8
# column 有 NaN 的筆數 3
# age NaN 的紀錄:         id name gender  age    area       job
# 1  1700002  吳俊諺    NaN  NaN  臺北市文山區   金融業和房地產
# 2  1700003  蔡俊毅    NaN  NaN  臺北市文山區  教育體育  文化
# 6  1700006  蔡登意    NaN  NaN     NaN   金融業和房地產

# put NaN to 0
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=0)
print('-- fillna 0 --')
print(df_sample.head())
#         id name  gender   age    area         job
# 0  1700001  李國發    Male  21.0  新北市三重區   金融業 和房地產
# 1  1700002  吳俊諺     NaN   0.0  臺北市文山區     金融業和房地產
# 2  1700003  蔡俊毅     NaN   0.0  臺北市文山區    教育體育  文化
# 3  1700004  姚鈺迪  Female  34.0  基隆市中正區    住宿 和 餐飲業
# 4  1700004  姚鈺迪  Female  34.0  基隆市中正區      住宿和餐飲業

# put NaN to value
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=df_sample['age'].mean())
print('-- fillna mean() --')
print(df_sample.head())
#         id name  gender   age    area         job
# 0  1700001  李國發    Male  21.0  新北市三重區   金融業 和房地產
# 1  1700002  吳俊諺     NaN  45.0  臺北市文山區     金融業和房地產
# 2  1700003  蔡俊毅     NaN  45.0  臺北市文山區    教育體育  文化
# 3  1700004  姚鈺迪  Female  34.0  基隆市中正區    住宿 和 餐飲業
# 4  1700004  姚鈺迪  Female  34.0  基隆市中正區      住宿和餐飲業

# put NaN as forward/back
df_sample = df.copy()
df_sample['age'] = df_sample['age'].ffill()
df_sample['gender'] = df_sample['gender'].bfill()
print('-- fillna forward-fill:fffill/back-fill:bfill --')
print(df_sample.head())
#         id name  gender   age    area         job
# 0  1700001  李國發    Male  21.0  新北市三重區   金融業 和房地產
# 1  1700002  吳俊諺  Female  21.0  臺北市文山區     金融業和房地產
# 2  1700003  蔡俊毅  Female  21.0  臺北市文山區    教育體育  文化
# 3  1700004  姚鈺迪  Female  34.0  基隆市中正區    住宿 和 餐飲業
# 4  1700004  姚鈺迪  Female  34.0  基隆市中正區      住宿和餐飲業

# delete NaN record
df_sample = df.copy()
df_sample = df_sample.dropna()
print('-- dropna --' )
print(df_sample)
#          id name  gender   age    area         job
# 0   1700001  李國發    Male  21.0  新北市三重區   金融業 和房地產
# 3   1700004  姚鈺迪  Female  34.0  基隆市中正區    住宿 和 餐飲業
# 4   1700004  姚鈺迪  Female  34.0  基隆市中正區      住宿和餐飲業
# 5   1700005  袁劭彥    Male  42.0  臺北市文山區     金融業和房地產
# 11  1700011  許合蓉  Female  61.0  新北市三重區      住宿和餐飲業
# 12  1700012  武家豪    Male  53.0  新北市三重區       農林牧漁業
# 14  1700014  周聿綠  Female  57.0  基隆市中正區     金融業和房地產