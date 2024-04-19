# 數值處理 - 調整
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


# 去除重複
df_sample = df.copy()
# subset 判斷欄位
# keep first第一筆, last最後一筆
# inplace True : 原資料更新
df_sample.drop_duplicates(subset='id', keep='first', inplace=True)
print('-- delete duplicate --')
print(df_sample)
#          id name  gender   age    area         job
# 0   1700001  李國發    Male  21.0  新北市三重區   金融業 和房地產
# 1   1700002  吳俊諺     NaN   NaN  臺北市文山區     金融業和房地產
# 2   1700003  蔡俊毅     NaN   NaN  臺北市文山區    教育體育  文化
# 3   1700004  姚鈺迪  Female  34.0  基隆市中正區    住宿 和 餐飲業
# 5   1700005  袁劭彥    Male  42.0  臺北市文山區     金融業和房地產
# 6   1700006  蔡登意     NaN   NaN     NaN     金融業和房地產

# 資料內容置換
# df.str.strip 去除左右空白
# df.str.lstrip 去除左邊空白
# df.str.rstrip 去除右邊空白
# df.str.replace(old,new) 替換文字
print('-- strip + replace --')
df_sample = df.copy()
df_sample['job'] = df_sample['job'].str.strip()
df_sample['job'] = df_sample['job'].str.replace(' ', '')
print(df_sample.head())
        # id name  gender   age    area      job
# 0  1700001  李國發    Male  21.0  新北市三重區  金融業和房地產
# 1  1700002  吳俊諺     NaN   NaN  臺北市文山區  金融業和房地產
# 2  1700003  蔡俊毅     NaN   NaN  臺北市文山區   教育體育文化
# 3  1700004  姚鈺迪  Female  34.0  基隆市中正區   住宿和餐飲業
# 4  1700004  姚鈺迪  Female  34.0  基隆市中正區   住宿和餐飲業

# 欄位格式調整
print('-- age type to int32 --')
# Cannot convert non-finite values (NA or inf) to integer
df_sample['age'] = df_sample['age'].ffill()
print("df_sample['age'] type)", type(df_sample['age'].dtype) )
df_sample['age'] = df_sample['age'].astype('int32')
print("df_sample['age'] type)", type(df_sample['age'].dtype) )
print(df_sample.head())
# df_sample['age'] type) <class 'numpy.dtypes.Float64DType'>
# df_sample['age'] type) <class 'numpy.dtypes.Int32DType'>
#         id name  gender  age    area      job
# 0  1700001  李國發    Male   21  新北市三重區  金融業和房地產
# 1  1700002  吳俊諺     NaN   21  臺北市文山區  金融業和房地產
# 2  1700003  蔡俊毅     NaN   21  臺北市文山區   教育體育文化
# 3  1700004  姚鈺迪  Female   34  基隆市中正區   住宿和餐飲業
# 4  1700004  姚鈺迪  Female   34  基隆市中正區   住宿和餐飲業