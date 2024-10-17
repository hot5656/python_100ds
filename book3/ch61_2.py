# 單股單月每日資料
# https://www.twse.com.tw/pcversion/zh/exchangeReport/FMSRFK?response=json&date=19950101&stockNo=9921

import pandas as pd
import numpy as np
import json
import requests

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
    return StockPrice

def Get_IndexPrice(Date):
    url = f'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={Date}&type=ALL'

    data = requests.get(url).text
    json_data = json.loads(data)

    # print(json_data)

    # 打印出完整的 json_data 以檢查響應
    print(json_data)

    Index_data = json_data['data']

    # 假設我們只需要大盤指數的相關欄位
    IndexPrice = pd.DataFrame(Index_data, columns=['Date', 'Index', 'Change', 'Volume'])

    IndexPrice['Date'] = IndexPrice['Date'].str.replace('/', '').astype(int) + 19110000
    IndexPrice['Date'] = pd.to_datetime(IndexPrice['Date'].astype(str))

    # 轉換數據類型
    IndexPrice['Index'] = IndexPrice['Index'].str.replace(',', '').astype(float)
    IndexPrice['Change'] = IndexPrice['Change'].str.replace(',', '').astype(float)
    IndexPrice['Volume'] = IndexPrice['Volume'].str.replace(',', '').astype(float)

    IndexPrice = IndexPrice.set_index('Date', drop=True)

    print(IndexPrice)
    return IndexPrice
    # return 1

if __name__ == '__main__':
    # data = Get_StockPrice('9921','20230101')
    # data = Get_StockPrice('9921','20241001')
    data = Get_StockPrice('9921','20241016')
    data = Get_IndexPrice('20241001')
