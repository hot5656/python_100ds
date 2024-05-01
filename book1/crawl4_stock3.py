# 年交易折線圖 - 收盤價, 最低價, 最高價
# https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20240430&stockNo=2317&response=json&_=1714460309678

import pandas as pd
import requests

import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
import os
import time

# 中華民國日期 to 西元
def dateConvert(date_str):
    date_list = date_str.split('/')
    date_list[0] = str(int(date_list[0])+1911)
    return '-'.join(date_list)

def load_file(file_name) :
    # Create an empty list to store DataFrames
    all_dataframes = []

    # json to DataFrame(include all 2024 data)
    day_url_head = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=2023"
    day_url_tail = "01&stockNo=2317&response=json&_=1714460309678"

    for index in range(0, 12):
        response = requests.get(day_url_head + '{:02d}'.format(index+1) + day_url_tail)
        month_records = response.json()

        if month_records['total'] == 0 :
            break

        df = pd.DataFrame(month_records['data'],
                        columns=month_records['fields'])

        # Convert the '日期' column
        df['日期'] = df['日期'].apply(dateConvert)

        # Append the DataFrame to the list
        all_dataframes.append(df)

        print(f"2023-{str(index+1)}")
        time.sleep(2)

    # Concatenate all DataFrames into one
    # ignore_index=True 索引重設
    final_dataframe = pd.concat(all_dataframes, ignore_index=True)

    # Print the final DataFrame
    print(final_dataframe)

    # save to csv file
    final_dataframe.to_csv(file_name, encoding='utf-8', index=False)


# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

file_name = 'stock_2317_2023.csv'
if not os.path.isfile(file_name):
    load_file(file_name)

pd_stock = pd.read_csv(file_name, encoding='utf-8')
pd_stock.plot(kind='line', figsize=(12,6), x='日期',
              y=['收盤價', '最低價', '最高價'])

plt.show()