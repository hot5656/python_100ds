# libary
# https://www.twse.com.tw/zh/trading/historical/stock-day-avg.html

import requests
from bs4 import BeautifulSoup
import unicodedata
from datetime import datetime, timedelta
import json
import re
import pandas as pd
from io import StringIO
import yfinance as yf
import inspect

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

# get 單股基本資料
def get_dividend_list(symbol, Show=False):
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
    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock={symbol}')
        for key, value in info.items():
            print(f'{key}: {value}')
    return info

# get 及時指數
def Current_Index_Google(Show=False):
    stock_url = 'https://www.google.com/finance/quote/IX0001:TPE'
    web = requests.get(stock_url)
    soup = BeautifulSoup(web.text, "html.parser")

    # 爬取即時指數
    index = soup.select("div[class*='YMlKec fxKbKc']")[0].get_text().replace(",", "")
    index_value = float(index)

    if Show :
        print(f'{inspect.currentframe().f_code.co_name} index={index_value}')

    return index_value

# get 單股 及時股價
def Current_stock_Price_yahoo(stock_code, Show=False):
    stock_url = f'https://tw.stock.yahoo.com/quote/{stock_code}'
    web = requests.get(stock_url)
    soup = BeautifulSoup(web.text, "html.parser")

    # 爬取股票名稱和即時價格
    price = soup.select("span[class*='Fz(32px)']")[0].get_text()

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock_code={stock_code} price={price}')

    return price

def clean_html(raw_html):
    clean_text = re.sub('<.*?>', '', raw_html)  # 用正則表達式替換掉 HTML 標籤
    return clean_text

# get 指定日期指數
def Get_IndexPrice(Date, Show=False):
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
        index_info = Index_data_cleaned
        # return Index_data_cleaned
    except :
        index_info = []

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} date={Date}')
        print(index_info)

    return index_info

# get 前一天指數及日期
def Get_Pre_IndexPrice(Show=False):
    days = 1
    value = 0

    while(days<10):
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
        index_value = Get_IndexPrice(yesterday)
        if len(index_value) != 0:
            value = float(index_value[1])
            break
        days += 1
    date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
    if Show:
        print(f'{inspect.currentframe().f_code.co_name} date={date} value={value}')

    return value, date

# get 單股股利資訊
# support 處理年配
def getAllInfo(stock, Show=False):
    # 定義目標網站的 URL (Yahoo 財經台股例子)
    url = f'https://tw.stock.yahoo.com/quote/{stock}/dividend'

    # 發送 GET 請求到網站
    response = requests.get(url)

    # 如果請求成功，則繼續處理
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析網頁內容
        soup = BeautifulSoup(response.text, 'html.parser')

        header =  soup.select("div[class*='table-header']")

        # data_elements = soup.select("li.List(n) div.table-row")
        results = soup.select("li[class*='List'] div.table-row")


        columns = [col.get_text(strip=True) for col in header[0].select('div')]
        # remove 多餘欄位
        columns.pop(0)

        # 打印表頭的欄位數量和內容
        # print(f"表頭欄位數量: {len(columns)}")
        # print(f"-表頭內容: {columns}-")

        # 解析 results: 提取每一行的數據
        data = []
        for row in results:
            # 提取每行的每個欄位值
            row_data = [col.get_text(strip=True) for col in row.select('div')]
            data.append(row_data)

        # 將表頭與數據結合到 Pandas DataFrame
        df_init = pd.DataFrame(data, columns=columns)

        # 反轉資料順序
        df = df_init[::-1].reset_index(drop=True)
    else:
        # print("無法抓取資料，請確認網址是否正確。")
        df = pd.DataFrame()

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock={stock}')
        print(df)

    return df

# get 單股股利資訊
# support 處理季或月配
def getAllInfo2(stock, Show=False):
    # 定義目標網站的 URL (Yahoo 財經台股例子)
    url = f"https://tw.stock.yahoo.com/quote/{stock}/dividend"

    # 發送 GET 請求到網站
    response = requests.get(url)

    # 如果請求成功，則繼續處理
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析網頁內容
        soup = BeautifulSoup(response.text, 'html.parser')

        header =  soup.select("div[class*='table-header']")

        # data_elements = soup.select("li.List(n) div.table-row")
        results = soup.select("li[class*='List'] div.table-row")

        columns = [col.get_text(strip=True) for col in header[0].select('div')]
        # remove 多餘欄位
        columns.pop(0)

        # 解析 results: 提取每一行的數據
        data = []
        for row in results:
            # 提取每行的每個欄位值
            row_data = [col.get_text(strip=True) for col in row.select('div')]
            data.append(row_data)

        # 將表頭與數據結合到 Pandas DataFrame
        df_init = pd.DataFrame(data, columns=columns)

        # 反轉資料順序
        df = df_init[::-1].reset_index(drop=True)

        # 移除明細配息
        for index, row in df.iterrows():
            # the code have error
            if row.values[0] == '':
                # print(f"移除行: {index}, 發放期間為空: {row['發放期間']}")
                df = df.drop(index)

        # 重設索引以確保連續性（可選）
        df.reset_index(drop=True, inplace=True)

    else:
        # print("無法抓取資料，請確認網址是否正確。")
        df = pd.DataFrame()

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock={stock}')
        print(df)

    return df

# OTC 年月報(含當月)
def Get_Month_StockPrice_OTC(Symbol, Year, Show=False):
    # 設定目標 URL (POST 請求的地址)
    url = 'https://www.tpex.org.tw/web/stock/statistics/monthly/st44.php?l=zh-tw'

    # 設定表單資料，這裡模擬提交年份和股票代號 (以 113 年與 00679B 為例)
    payload = {
        'yy': Year,  # '2024' 民國 113 年
        'input_stock_code': Symbol  # 股票代碼
    }

    # 發送 POST 請求
    response = requests.post(url, data=payload)

    # 檢查請求是否成功
    if response.status_code == 200:
        # 嘗試將 HTML 轉換成 pandas DataFrame
        try:
            # 使用 StringIO 包裝 response.text
            html_content = StringIO(response.text)

            tables = pd.read_html(html_content)

            # 假設我們要的是第一個表格 (根據網頁結構調整)
            StockPrice = tables[2]

            StockPrice = StockPrice.rename(columns={'年': 'Year'})
            StockPrice = StockPrice.rename(columns={'月': 'Month'})
            StockPrice = StockPrice.rename(columns={'收市最高價': 'High'})
            StockPrice = StockPrice.rename(columns={'收市最低價': 'Low'})
            StockPrice = StockPrice.rename(columns={'收市平均價': 'Average'})
            StockPrice = StockPrice.rename(columns={'成交筆數': 'Volume'})
            # print(StockPrice.columns)
        except:
             StockPrice = pd.DataFrame()
    else :
         StockPrice = pd.DataFrame()

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock_code={Symbol} year={Year}')
        print(StockPrice)
    return StockPrice

# 上市 年月報(不含當月)
def Get_Month_StockPrice(Symbol, Date, Show=False):
    url = f'https://www.twse.com.tw/pcversion/zh/exchangeReport/FMSRFK?response=json&date={Date}&stockNo={Symbol}'
    data = requests.get(url).text

    try:
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
    except:
        StockPrice = pd.DataFrame()
    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock_code={Symbol} date={Date}')
        print(StockPrice)
    return StockPrice

# 上市 年月報(含當月)
def Get_Month_StockPrice_AddCurrent(Symbol, Date, Show=False):
    year_start = Date
    today = datetime.now().strftime('%Y%m%d')
    month_data_stock = Get_Month_StockPrice(Symbol, Date, False)
    month_price = Get_Month_analyze_StockPrice(Symbol, today, False)

    # 構造一個新的DataFrame來保存本月的數據
    current_month = today[:6]  # 獲取當前年月
    new_row = pd.DataFrame({
        'High': [month_price['High']],
        'Low': [month_price['Low']],
        'Average': [month_price['AverageLevel']],
        'Volume': [month_price.get('Volume', 0)]  # 假設 Volume 存在於 month_price
    }, index=[int(today[4:6])])  # 使用當前月份作為索引

    # 將當月數據加入到 `month_data_stock` 中
    month_data_stock = month_data_stock._append(new_row)

    # 打印合併後的結果
    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock_code={Symbol} date={Date}')
        print(month_data_stock)
    return month_data_stock

# 單股 上市 當月統計(最高,最低 及 平均)
def Get_Month_analyze_StockPrice(Symbol, Date, Show=False):
    month_total = {}
    url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={Date}&stockNo={Symbol}'

    data = requests.get(url).text
    json_data = json.loads(data)

    Stock_data = json_data['data']
    StockPrice = pd.DataFrame(Stock_data, columns = ['Date','Volume','Volume_Cash','Open','High','Low','Close','Change','Order'])

    # print(StockPrice)
    # 移除 'Open' 欄位中為 '--' 的行
    #      Date   Volume Volume_Cash   Open   High    Low  Close Change Order
    # 9   113/10/17      557      19,643     --     --     --     --   0.00    91
    StockPrice = StockPrice[StockPrice['Open'] != '--']

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
    StockPrice = StockPrice[['Open','High','Low','Close','Volume','Volume_Cash']]

    # 計算本月的最高價、最低價和平均收盤價
    highest_price = StockPrice['Close'].max()
    lowest_price = StockPrice['Low'].min()
    average_close_price = round(StockPrice['Close'].mean(), 2)
    average_level_price = round(StockPrice['Volume_Cash'].sum()/(StockPrice['Volume'].sum()*1000),2)

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock_code={Symbol} date={Date}')
        print(StockPrice)
        print(f"本月最高價: {highest_price}")
        print(f"本月最低價: {lowest_price}")
        print(f"本月平均收盤價: {average_close_price}")
        print(f"加權平均價 :{average_level_price}")

    month_total['High'] = highest_price
    month_total['Low'] = lowest_price
    month_total['Average'] = average_close_price
    month_total['AverageLevel'] = average_level_price
    return month_total

# 單股 上市 月日報
def Get_StockPrice(Symbol, Date, Show=False):

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
    # StockPrice['AvPrice'] = round(StockPrice['Volume_Cash']/(StockPrice['Volume']*1000),2)

    # StockPrice['AvPrice'] = StockPrice['Volume_Cash']/StockPrice['Volume']


    StockPrice['Open'] = StockPrice['Open'].str.replace(',','').astype(float)
    StockPrice['High'] = StockPrice['High'].str.replace(',','').astype(float)
    StockPrice['Low'] = StockPrice['Low'].str.replace(',','').astype(float)
    StockPrice['Close'] = StockPrice['Close'].str.replace(',','').astype(float)

    StockPrice = StockPrice.set_index('Date', drop = True)


    StockPrice = StockPrice[['Open','High','Low','Close','Volume','Volume_Cash']]

    # 計算本月的最高價、最低價和平均收盤價
    highest_price = StockPrice['High'].max()
    lowest_price = StockPrice['Low'].min()
    average_close_price = round(StockPrice['Close'].mean(), 2)
    # average_level_price = round(round(StockPrice['AvPrice'].mean()/1000,2), 2)
    average_level_price = round(StockPrice['Volume_Cash'].sum()/(StockPrice['Volume'].sum()*1000),2)

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} stock={Symbol} date={Date}')
        print(StockPrice)
        print(f"本月最高價: {highest_price}")
        print(f"本月最低價: {lowest_price}")
        print(f"本月平均收盤價: {average_close_price}")
        print(f"加權平均價 : {average_level_price}")
    return StockPrice

# 取得年度月份指數統計
def fetch_taiex_monthly(year, Show=False):
    # 'TWII.TW' is the symbol for Taiwan Stock Exchange Index on Yahoo Finance
    taiex = yf.Ticker('^TWII')

    # Define the start and end dates for the given year
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'

    # Fetch historical data for the specific year (on a daily basis)
    historical_data = taiex.history(start=start_date, end=end_date, interval='1d')

    # Resample the data to monthly frequency, taking the average closing price of each month
    monthly_data = historical_data['Close'].resample('ME').mean().reset_index().round(2)

    # Extract the year and month
    monthly_data['Year'] = monthly_data['Date'].dt.year
    monthly_data['Month'] = monthly_data['Date'].dt.month

    # Organize the data into a list of dictionaries
    index_values = monthly_data[['Year', 'Month', 'Close']].to_dict('records')

    if Show:
        print(f'{inspect.currentframe().f_code.co_name} year={year}')
        for item in index_values:
            print(item)
    return index_values

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