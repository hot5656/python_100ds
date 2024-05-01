# 月交易折線圖 - 收盤價, 最低價, 最高價
import pandas as pd
import requests

import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
import os

# 中華民國日期 to 西元
def dateConvert(date_str):
    date_list = date_str.split('/')
    date_list[0] = str(int(date_list[0])+1911)
    return '-'.join(date_list)

def load_file(file_name) :
    day_url = 'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20240430&stockNo=2317&response=json&_=1714460309678'
    response = requests.get(day_url)
    month_records = response.json()

    df = pd.DataFrame(month_records['data'],
                    columns=month_records['fields'])
    #  save to csv file
    df.to_csv(file_name, encoding='utf-8', index=False)

# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

file_name = 'stock_2317_2024_04.csv'
if not os.path.isfile(file_name):
    load_file(file_name)

pd_stock = pd.read_csv(file_name, encoding='utf-8')
pd_stock.plot(kind='line', figsize=(12,6), x='日期',
              y=['收盤價', '最低價', '最高價'])

plt.show()
