# read data
# read_csv():.csv
# read_json():.json
# read_excel():xlsx
# read_html():.html
# read_sql() :SQLite

import pandas as pd
# sep : 分隔號, default ','
# encoding : 編碼
df1 = pd.read_csv('covid19.csv')
print('csv', df1)
df2 = pd.read_json('./covid19.json')
print('json',df2)
# read_excel need install openpyxl : pip install openpyxl
df3 = pd.read_excel('./covid19.xlsx')
print('excel',df3)
# read_html need install lxml :
# keep_default_na  是否去除空値
url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, keep_default_na=False)
# print(tables)
print('html',tables[0].head(10))

