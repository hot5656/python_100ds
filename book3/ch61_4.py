# 年配值利率
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from io import StringIO
from datetime import datetime

def getAllInfo(stock):
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

        # print('*'*20)
        # print(header[0])
        # print('*'*20)
        # print(results[0])

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

        # 顯示結果
        # print(df)

        # 反轉資料順序
        df = df_init[::-1].reset_index(drop=True)
        # print(df_reversed)
    else:
        # print("無法抓取資料，請確認網址是否正確。")
        df = pd.DataFrame()

    return df

# 處理季或月配
def getAllInfo2(stock):
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
        print("==== 原資料 ====")
        print(df)

        # 移除明細配息
        for index, row in df.iterrows():
            # the code have error
            # if row['發放期間'] == '' or pd.isna(row['發放期間']):
            if row.values[0] == '':
                # print(f"移除行: {index}, 發放期間為空: {row['發放期間']}")
                df = df.drop(index)

        # 重設索引以確保連續性（可選）
        df.reset_index(drop=True, inplace=True)

        # 顯示結果
        # print("移除後的 DataFrame：")
        # print(df_reversed)
    else:
        # print("無法抓取資料，請確認網址是否正確。")
        df = pd.DataFrame()

    return df

def Get_Month_StockPrice_OTC(Symbol, Year):
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
            # print(StockPrice)
            # print(StockPrice.columns)
        except:
             StockPrice = pd.DataFrame()
    else :
         StockPrice = pd.DataFrame()

    return StockPrice
    # try:
    #     json_data = json.loads(data)

    #     Stock_data = json_data['data']

    #     StockPrice = pd.DataFrame(Stock_data, columns=['Year', 'Month', 'High', 'Low', 'Average', 'Order', 'Volume_Cash', 'Volume', 'TurnoverRate'])

    #     StockPrice['Volume'] = StockPrice['Volume'].str.replace(',', '').astype(float) / 1000
    #     StockPrice['Volume_Cash'] = StockPrice['Volume_Cash'].str.replace(',', '').astype(float)
    #     StockPrice['Order'] = StockPrice['Order'].str.replace(',', '').astype(float)

    #     StockPrice['High'] = StockPrice['High'].str.replace(',', '').astype(float)
    #     StockPrice['Low'] = StockPrice['Low'].str.replace(',', '').astype(float)
    #     StockPrice['Average'] = StockPrice['Average'].str.replace(',', '').astype(float)

    #     StockPrice = StockPrice.set_index('Month', drop=True)

    #     StockPrice = StockPrice[['High', 'Low', 'Average', 'Volume']]
    # except:
    #     StockPrice = pd.DataFrame()

    # return StockPrice

def Get_Month_StockPrice(Symbol, Date):
    url = f'https://www.twse.com.tw/pcversion/zh/exchangeReport/FMSRFK?response=json&date={Date}&stockNo={Symbol}'

    data = requests.get(url).text

    # print(data)
    # print(f'Symbol={Symbol} Date={Date}')
    # return []
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

        print(StockPrice)
        StockPrice = StockPrice.set_index('Month', drop = True)

        StockPrice = StockPrice[['High','Low','Average','Volume']]
    except:
        StockPrice = pd.DataFrame()
    # print(StockPrice)
    return StockPrice

# stock_code = '9921'
# stock_code = '0056'
# stock_code = '00919'
# stock_code = '00657'
# stock_code = '00679B'
stock_code = '00662'
df_all = getAllInfo2(stock_code)
print(df_all)
print(len(df_all))
print(f"stock_code={stock_code}")
# for item in df_all:
#     print(item)
if len(df_all) == 0:
    year_int = int(datetime.now().strftime('%Y'))
    point_stock = 'wait'
    list_years = []
    while year_int >= 1990 :
        year = str(year_int)
        # print(f"year={year}")
        year_start = year + '0101'

        if point_stock == 'wait':
            month_data_stock = Get_Month_StockPrice(stock_code, year_start)
            if len(month_data_stock) == 0:
                month_data_OTC = Get_Month_StockPrice_OTC(stock_code, year)
                point_stock = 'otc'
            else:
                month_data_OTC = pd.DataFrame()
                point_stock = 'stock'
        elif point_stock == 'stock':
            month_data_stock = Get_Month_StockPrice(stock_code, year_start)
        else:
            # otc
            month_data_OTC = Get_Month_StockPrice_OTC(stock_code, year)

        if len(month_data_stock) != 0 :
            year_1st_price =  month_data_stock.iloc[0]["Average"]
            year_last_price = month_data_stock.iloc[-1]["Average"]
        elif len(month_data_OTC) != 0 :
            year_1st_price =  month_data_OTC.iloc[0]["Average"]
            year_last_price = month_data_OTC.iloc[-1]["Average"]
        else:
            break

        rate = round(((year_last_price/year_1st_price) - 1) * 100, 2)
        # print(f"{year}  股價: {year_1st_price:7} --> {year_last_price:7}, 現金股利={cash_dividend:5}, 股票股利={stock_dividend:5}, 值利率={rate:7}%")
        # print(f"{year}  股價: {year_1st_price:7} --> {year_last_price:7}, 現金股利=*****, 股票股利=***** 值利率={rate:7}%")
        list_years.append(f"{year}  股價: {year_1st_price:7} --> {year_last_price:7}, 現金股利=*****, 股票股利=***** 值利率={rate:7}%")
        year_int -= 1
    # print(list_years)
    for item in reversed(list_years):
        print(item)
else :
    for index, row in df_all.iterrows():
        # print(f"第 {index+1} 行的值: {row.values}")
        year= row.values[0]
        # print(f'year={year}')
        year_start = year + '0101'
        month_data_stock = Get_Month_StockPrice(stock_code, year_start)
        if len(month_data_stock) == 0:
            month_data_OTC = Get_Month_StockPrice_OTC(stock_code, year)
        else:
            month_data_OTC = pd.DataFrame()

        if len(month_data_stock) == 0 and len(month_data_OTC) == 0:
            # print("no stock data...")
            print(f"{year} - 資料不足")
        else:
            # print(row)
            if row['現金股利'] =='-':
                cash_dividend = 0
            else:
                cash_dividend = float(row['現金股利'])

            if row['股票股利'] =='-':
                stock_dividend = 0
            else:
                stock_dividend = float(row['股票股利'])

            # print(f"現金股利={row['現金股利']}, 股票股利={row['股票股利']}")
            if len(month_data_stock) != 0 :
                year_1st_price =  month_data_stock.iloc[0]["Average"]
                year_last_price = month_data_stock.iloc[-1]["Average"]
            else:
                year_1st_price =  month_data_OTC.iloc[0]["Average"]
                year_last_price = month_data_OTC.iloc[-1]["Average"]

            # print(f"現金股利={cash_dividend}, 股票股利={stock_dividend}")
            # print(f'1st={year_1st_price}, last={year_last_price}')
            rate = round((((year_last_price * ( 1 + stock_dividend/100) + cash_dividend)/year_1st_price) - 1) * 100, 2)
            print(f"{year}  股價: {year_1st_price:7} --> {year_last_price:7}, 現金股利={cash_dividend:5}, 股票股利={stock_dividend:5}, 值利率={rate:7}%")
            # break
