# 計算年度 1月指數 及 12月指數 平均值
from ch61_lib import *

year = 2000
while year <= 2024:
    taiex_data = fetch_taiex_monthly(year)
    if taiex_data:
        start = round(taiex_data[0]['Close'],2)
        end = round(taiex_data[-1]['Close'],2)
        print(f'{year} 指數: {start:10} --> {end:10} {round(((end/start)-1)*100,2):6}%')
    year += 1