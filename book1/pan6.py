# write data
# to_csv():.csv
# to_json():.json
# to_excel():xlsx
# to_html():.html
# to_sql() :SQLite
import pandas as pd

df = pd.DataFrame([[65,92,78,83,70],
                   [90,72,76,93,56],
                   [81,85,91,89,77],
                   [79,53,47,94,80]],
                  index=['大明','小王','李四','張山'],
                  columns=['英文','國文','數學','社會','生活'])
df.to_csv('scores2.csv')
df.to_excel('scores2.xlsx')
df.to_json('scores2.json')
df.to_html('scores2.html')