# 資料篩選,分組運算
import pandas as pd

df = pd.read_csv('customer.csv')
print(df)
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

# 欄位條件
print('-- 欄位條件 --')
print(df[df['gender'] == 'Female'])
#          id name  gender   age    area        job
# 3   1700004  姚鈺迪  Female  34.0  基隆市中正區   住宿 和 餐飲業
# 4   1700004  姚鈺迪  Female  34.0  基隆市中正區     住宿和餐飲業
# 11  1700011  許合蓉  Female  61.0  新北市三重區     住宿和餐飲業
# 14  1700014  周聿綠  Female  57.0  基隆市中正區    金融業和房地產

# 欄位多條件
print('-- 欄位多條件 --')
print(df[(df['gender'] == 'Male') & (df['age'] > 50)])
#          id name gender   age    area    job
# 12  1700012  武家豪   Male  53.0  新北市三重區  農林牧漁業

# 分組運算欄
print("-- gender's age mean --")
print(df.groupby('gender')['age'].mean())
# gender
# Female    46.500000
# Male      38.666667
# Name: age, dtype: float64

# 彙總統計
print("-- gender's age mean, min, max --")
print(df.groupby('gender')['age'].agg(['mean', 'min', 'max']))
#              mean   min   max
# gender
# Female  46.500000  34.0  61.0
# Male    38.666667  21.0  53.0
