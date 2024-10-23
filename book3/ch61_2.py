# 單股單月每日資料
# https://www.twse.com.tw/pcversion/zh/exchangeReport/FMSRFK?response=json&date=19950101&stockNo=9921

import pandas as pd
import numpy as np
import json
import requests

# 上市 月日報
def Get_StockPrice(Symbol, Date):

    url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={Date}&stockNo={Symbol}'

    data = requests.get(url).text
    json_data = json.loads(data)

    Stock_data = json_data['data']

    StockPrice = pd.DataFrame(Stock_data, columns = ['Date','Volume','Volume_Cash','Open','High','Low','Close','Change','Order'])

    StockPrice['Date'] = StockPrice['Date'].str.replace('/','').astype(int) + 19110000
    StockPrice['Date'] = pd.to_datetime(StockPrice['Date'].astype(str))
    StockPrice['Volume'] = StockPrice['Volume'].str.replace(',','').astype(float)/1000
    StockPrice['Volume_Cash'] = StockPrice['Volume_Cash'].str.replace(',','').astype(float)
    StockPrice['Order'] = StockPrice['Order'].str.replace(',','').astype(float)

    StockPrice['Open'] = StockPrice['Open'].str.replace(',','').astype(float)
    StockPrice['High'] = StockPrice['High'].str.replace(',','').astype(float)
    StockPrice['Low'] = StockPrice['Low'].str.replace(',','').astype(float)
    StockPrice['Close'] = StockPrice['Close'].str.replace(',','').astype(float)

    StockPrice = StockPrice.set_index('Date', drop = True)


    StockPrice = StockPrice[['Open','High','Low','Close','Volume']]
    print(StockPrice)

    # 計算本月的最高價、最低價和平均收盤價
    highest_price = StockPrice['Close'].max()
    lowest_price = StockPrice['Low'].min()
    average_close_price = round(StockPrice['Close'].mean(), 2)

    print(f"本月最高價: {highest_price}")
    print(f"本月最低價: {lowest_price}")
    print(f"本月平均收盤價: {average_close_price}")
    return StockPrice

# OTC 月日報
def Get_OTcPrice(Symbol):
    # 定義股票代號和查詢日期範圍
    stock_id = Symbol  # 例如 "2330"
    year = "2023"
    month = "09"

    # 組合 URL 來抓取資料
    # url = f"https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43_result.php?l=zh-tw&d={year}/{month}&stkno={stock_id}"
    url = f"https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43_result.php?l=zh-tw&d=113/10/01&stkno=00679B"

    # 使用 pandas 讀取 JSON 格式資料
    df = pd.read_json(url)

    # 取出 'aaData' 的每日交易資料
    daily_data = df['aaData']

    # 先將 daily_data 轉換為 list
    daily_data_list = list(daily_data)


    # print(df['aaData'])

    # 定義欄位名稱
    columns = ['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌', '成交筆數']

    # 將資料轉換為 DataFrame 並指定欄位
    price_df = pd.DataFrame(daily_data_list, columns=columns)

    # 將數字格式的欄位（如成交股數、成交金額等）去除千位分隔符號並轉換為數字型別
    price_df['成交股數'] = price_df['成交股數'].str.replace(',', '').astype(float)
    price_df['成交金額'] = price_df['成交金額'].str.replace(',', '').astype(float)
    price_df['開盤價'] = price_df['開盤價'].astype(float)
    price_df['最高價'] = price_df['最高價'].astype(float)
    price_df['最低價'] = price_df['最低價'].astype(float)
    price_df['收盤價'] = price_df['收盤價'].astype(float)
    price_df['漲跌'] = price_df['漲跌'].astype(float)
    price_df['成交筆數'] = price_df['成交筆數'].str.replace(',', '').astype(float)

    print(price_df)

    # 計算本月的最高價、最低價和平均收盤價
    highest_price = price_df['收盤價'].max()
    lowest_price = price_df['收盤價'].min()
    average_close_price = round(price_df['收盤價'].mean(), 2)

    print(f"本月最高價: {highest_price}")
    print(f"本月最低價: {lowest_price}")
    print(f"本月平均收盤價: {average_close_price}")
    return price_df

    # # 打印資料
    # print(df['aaData'])
    # for item in df['aaData']:
    #     print(type)
    #     print(item)

if __name__ == '__main__':
    # data = Get_StockPrice('9921','20230101')
    # data = Get_StockPrice('0056','20241001')
    # data = Get_OTcPrice('00679B')
    data = Get_StockPrice('00915','20240101')
    data = Get_StockPrice('00915','20240201')
    data = Get_StockPrice('00915','20240301')
    data = Get_StockPrice('00915','20240401')
    data = Get_StockPrice('00915','20240501')
    data = Get_StockPrice('00915','20240601')
    data = Get_StockPrice('00915','20240701')
    data = Get_StockPrice('00915','20240801')
    data = Get_StockPrice('00915','20240901')
    data = Get_StockPrice('00915','20241001')
