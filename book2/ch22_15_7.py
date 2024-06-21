import pandas as pd

df = pd.read_csv("個人資料.csv")
# column 對齊資料
pd.set_option('display.unicode.ambiguous_as_wide', True)
# 若含有中英文資料可以對齊
pd.set_option('display.unicode.east_asian_width', True)

print(df)
print(df.columns)
columns = {
    "編號":"ID",
    "學歷":"Education"
}

df.rename(columns=columns, inplace=True)
print(df.head())
#    編號         學歷
# 0   101         高中
# 1   102         大學
# 2   103         碩士
# 3   104         博士
# 4   105  high_school
# Index(['編號', '學歷'], dtype='object')
#     ID    Education
# 0  101         高中
# 1  102         大學
# 2  103         碩士
# 3  104         博士
# 4  105  high_school
