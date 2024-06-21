import pandas as pd

df = pd.read_csv("個人資料.csv")
# column 對齊資料
pd.set_option('display.unicode.ambiguous_as_wide', True)
# 若含有中英文資料可以對齊
pd.set_option('display.unicode.east_asian_width', True)

columns = {
    "編號":"ID",
    "學歷":"Education"
}
df.rename(columns=columns, inplace=True)

edu = {'高中':1, '大學':2, '碩士':3, '博士':4, 'high_school':99  }
df['Education'] = df['Education'].map(edu)

print(df.head())
#     ID  Education
# 0  101          1
# 1  102          2
# 2  103          3
# 3  104          4
# 4  105         99