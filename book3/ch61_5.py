# get 當天指數,股價 + 前一天股價

import yfinance as yf
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import re

def Current_Index():
    # 台灣加權股價指數的代碼 '^TWII'
    ticker = '^TWII'
    data = yf.Ticker(ticker)
    # 抓取最新的行情數據
    today_data = data.history(period='1d')
    closing_value = today_data['Close'].values[0]

    # print(f'index : {round(closing_value,2)}')
    # print(f"hist_data={today_data}")
    return round(closing_value,2)

def Current_Index2():
    stock_url = 'https://www.google.com/finance/quote/IX0001:TPE'
    web = requests.get(stock_url)
    soup = BeautifulSoup(web.text, "html.parser")

    # 爬取即時指數
    index = soup.select("div[class*='YMlKec fxKbKc']")[0].get_text().replace(",", "")
    print(index)
    return index


def Current_stock_Price(stock_code):
    # 9921 巨大集團在 Yahoo Finance 的代碼是 "9921.TW"
    ticker = stock_code + '.TW'
    data = yf.Ticker(ticker)

    # 抓取即時的行情數據
    today_data = data.history(period='1d')
    current_price = today_data['Close'].values[0]

    # print(f'{stock_code} price : {current_price}')
    return current_price

def Current_stock_Price2(stock_code):
    stock_url = f'https://tw.stock.yahoo.com/quote/{stock_code}'
    web = requests.get(stock_url)
    soup = BeautifulSoup(web.text, "html.parser")

    # 爬取股票名稱和即時價格
    title = soup.find('h1').get_text()
    price = soup.select("span[class*='Fz(32px)']")[0].get_text()
    # print(f'{stock_code} price2 : {price}')；
    return price


def clean_html(raw_html):
    clean_text = re.sub('<.*?>', '', raw_html)  # 用正則表達式替換掉 HTML 標籤
    return clean_text

def Get_IndexPrice(Date):
    url = f'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={Date}&type=IND'

    data = requests.get(url).text
    json_data = json.loads(data)

    # print("Keys in JSON response:")
    # for key in json_data.keys():
    #     print(f"- {key}")

    try :
        Index_data = json_data['data1'][1]
        Index_data_cleaned = [clean_html(item) if isinstance(item, str) else item for item in Index_data]
        Index_data_cleaned[1] = float(Index_data_cleaned[1].replace(',', ''))
        Index_data_cleaned[3] = float(Index_data_cleaned[3])
        Index_data_cleaned[4] = float(Index_data_cleaned[4])
        # print(Index_data_cleaned)
        # print(f"yesterday index = {Index_data_cleaned[1]}")
        return Index_data_cleaned
    except :
        return []

# 上市 月日報
def Get_Day_StockPrice(Symbol, Date):

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

stock_code = '9921'
stock_code = '0056'
today = datetime.now().strftime('%Y%m%d')
index = Current_Index()
index2 = Current_Index2()
stock_price = Current_stock_Price(stock_code)
stock_price2 = Current_stock_Price2(stock_code)

print(f"{today} index={index} {index2}, {stock_code} price={stock_price} {stock_price2}")

days = 1

while(days<10):
    yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
    index_value = Get_IndexPrice(yesterday)
    print(f'({days}) {index_value}')
    if len(index_value) != 0:
        # print(f' days={days}, {index_value}')
        print(f'{(datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")} index : {index_value[1]}')
        break
    days += 1


stock_price = Get_Day_StockPrice(stock_code, today)
# print(f"today={today}")
# print(stock_price)
# print(stock_price.index[-1].strftime('%Y-%m-%d'), stock_price['Close'].iloc[-1])
if (stock_price.index[-1].strftime('%Y-%m-%d') != today):
    yesterday_date = stock_price.index[-1].strftime('%Y-%m-%d')
    yesterday_price = stock_price['Close'].iloc[-1]
else:
    yesterday_date = stock_price.index[-2].strftime('%Y-%m-%d')
    yesterday_price = stock_price['Close'].iloc[-2]
print(f'{yesterday_date} {stock_code} price : {yesterday_price}')

