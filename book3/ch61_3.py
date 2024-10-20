# 單股單年每月資料
# https://www.twse.com.tw/pcversion/zh/exchangeReport/FMSRFK?response=json&date=19950101&stockNo=9921

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

    StockPrice = pd.DataFrame(Stock_data, columns = ['Year','Month','High','Low','Average','Order', 'Volume_Cash','Volume', 'TurnoverRate'])

    StockPrice['Volume'] = StockPrice['Volume'].str.replace(',','').astype(float)/1000
    StockPrice['Volume_Cash'] = StockPrice['Volume_Cash'].str.replace(',','').astype(float)
    StockPrice['Order'] = StockPrice['Order'].str.replace(',','').astype(float)

    StockPrice['High'] = StockPrice['High'].str.replace(',','').astype(float)
    StockPrice['Low'] = StockPrice['Low'].str.replace(',','').astype(float)
    StockPrice['Average'] = StockPrice['Average'].str.replace(',','').astype(float)

    StockPrice = StockPrice.set_index('Month', drop = True)

    StockPrice = StockPrice[['High','Low','Average','Volume']]
    print(StockPrice)
    return StockPrice

if __name__ == '__main__':
    # data = Get_StockPrice('9921','20230101')
    data = Get_StockPrice('0056','20241001')
