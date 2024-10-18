# libary

import requests
from bs4 import BeautifulSoup
import unicodedata
from datetime import datetime, timedelta
import json
import re

# 計算字符實際寬度，處理中英文字符
def get_display_width(text):
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in 'WF':  # 全寬或寬字符
            width += 2
        else:
            width += 1
    return width

# 自定義的 ljust，用來正確對齊中文和英文
def custom_ljust(text, width):
    display_width = get_display_width(text)
    return text + ' ' * (width - display_width)

def get_dividend_list(symbol):
    div_url = f'https://www.moneydj.com/ETF/X/Basic/Basic0004.xdjhtm?etfid={symbol}.TW'
    r = requests.get(div_url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    results = soup.select("table tr")
    index=1
    for item in results:
        # print(f'({index}) {item}')
        index += 1

    # print(f'data11 ---> {results[11]}')
    info = {}
    info['code']=symbol
    info['名稱']= results[4].select("td")[0].text
    info['成立']= results[7].select("td")[0].text
    info['規模']= results[8].select("td")[0].text
    today = datetime.now().strftime('%m/%d')
    current_price = Current_stock_Price_yahoo(symbol)
    text_price = results[9].select("td")[1].text
    pre_price = float(text_price.split('（')[0])
    # print(f'pre_price={pre_price}')
    info['當日價']= f'{current_price} ({today}):{(float(current_price)/pre_price-1)*100:.2}%'
    info['市價']= text_price
    info['淨值']= results[10].select("td")[1].text
    info['折溢價']= results[11].select("td")[1].text
    return info

def Current_Index_Google():
    stock_url = 'https://www.google.com/finance/quote/IX0001:TPE'
    web = requests.get(stock_url)
    soup = BeautifulSoup(web.text, "html.parser")

    # 爬取即時指數
    index = soup.select("div[class*='YMlKec fxKbKc']")[0].get_text().replace(",", "")
    return float(index)

def Current_stock_Price_yahoo(stock_code):
    stock_url = f'https://tw.stock.yahoo.com/quote/{stock_code}'
    web = requests.get(stock_url)
    soup = BeautifulSoup(web.text, "html.parser")

    # 爬取股票名稱和即時價格
    price = soup.select("span[class*='Fz(32px)']")[0].get_text()
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

def Get_Pre_IndexPrice():
    days = 1
    value = 0

    while(days<10):
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
        index_value = Get_IndexPrice(yesterday)
        if len(index_value) != 0:
            # print(f' days={days}, {index_value}')
            # print(f'{(datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")} index : {index_value[1]}')
            value = float(index_value[1])
            break
        days += 1
    return value, (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')

if __name__ == '__main__':
    stock_code = "0050"
    key_length = [6, 20, 24, 36, 24, 20, 20, 20]
    info = get_dividend_list(stock_code)
    keys = list(info.keys())
    # print(keys)
    # print(info)

    # print key
    for index in range(len(keys)):
        print(f'{custom_ljust(keys[index], key_length[index])}', end=' ')
    # print info
    print("")
    for index, (key, value) in enumerate(info.items()):
        print(f'{custom_ljust(value, key_length[index])}', end=' ')
    # print compare string
    # print("")
    # for index in range(len(keys)):
    #     print(f'{"*"*key_length[index]}', end=' ')
    print("")

    today = datetime.now().strftime('%Y%m%d')
    index = Current_Index_Google()
    stock_price = Current_stock_Price_yahoo(stock_code)
    print(f"{today} index={index}, {stock_code} price={stock_price}")
    pre_index, pre_date = Get_Pre_IndexPrice()
    print(f'pre index = {pre_index} {pre_date}')