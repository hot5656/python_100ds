# 年度偏移百分比,每月的偏移百分比
import pandas as pd
import numpy as np
import json
import requests

# 上市 年月報(不含當月)
def Get_StockPrice(Symbol, Date):
    url = f'https://www.twse.com.tw/pcversion/zh/exchangeReport/FMSRFK?response=json&date={Date}&stockNo={Symbol}'

    data = requests.get(url).text
    json_data = json.loads(data)

    Stock_data = json_data['data']

    StockPrice = pd.DataFrame(Stock_data, columns=['Year', 'Month', 'High', 'Low', 'Average', 'Order', 'Volume_Cash', 'Volume', 'TurnoverRate'])

    StockPrice['Volume'] = StockPrice['Volume'].str.replace(',', '').astype(float) / 1000
    StockPrice['Volume_Cash'] = StockPrice['Volume_Cash'].str.replace(',', '').astype(float)
    StockPrice['Order'] = StockPrice['Order'].str.replace(',', '').astype(float)

    StockPrice['High'] = StockPrice['High'].str.replace(',', '').astype(float)
    StockPrice['Low'] = StockPrice['Low'].str.replace(',', '').astype(float)
    StockPrice['Average'] = StockPrice['Average'].str.replace(',', '').astype(float)

    StockPrice = StockPrice.set_index('Month', drop=True)

    StockPrice = StockPrice[['High', 'Low', 'Average', 'Volume']]
    print(StockPrice)

    # 計算年度平均值和標準差
    annual_mean = StockPrice['Average'].mean()
    annual_std = StockPrice['Average'].std()

    # 計算年度偏移百分比
    annual_deviation_percentage = (annual_std / annual_mean) * 100

    # 計算每月偏移百分比
    StockPrice['Positive Deviation %'] = ((StockPrice['Average'] - annual_mean) / annual_mean) * 100

    # 如果偏移百分比為負的情況
    StockPrice['Negative Deviation %'] = ((annual_mean - StockPrice['Average']) / annual_mean) * 100

    print(f"年度平均值: {annual_mean:.2f}")
    print(f"年度標準差: {annual_std:.2f}")
    print(f"年度偏移百分比: {annual_deviation_percentage:.2f} %")
    print("每月的偏移百分比:")
    print(StockPrice[['Positive Deviation %', 'Negative Deviation %']])

    return StockPrice, annual_deviation_percentage

if __name__ == '__main__':
    # data, annual_deviation_percentage = Get_StockPrice('9921', '20230101')
    data, annual_deviation_percentage = Get_StockPrice('0056', '20230101')
    data, annual_deviation_percentage = Get_StockPrice('0056', '20240101')