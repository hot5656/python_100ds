from ch61_lib import *
import sys

arguments = sys.argv[1:]
if len(arguments) !=0:
    if arguments[0] == '1':
        # 計算輸入年份第一個月即最後一個月,指數平均值
        year = 2024
        taiex_data = fetch_taiex_monthly(year, True)
        if taiex_data:
            start = round(taiex_data[0]['Close'],2)
            end = round(taiex_data[-1]['Close'],2)
            print(f'{year} 指數: {start:10} --> {end:10} {round(((end/start)-1)*100,2):6}%')
    elif arguments[0] == '2':
        # 上市 年月報(不含當月)
        stock_code = '0056'
        year_start = datetime.now().strftime('%Y') + '0101'
        month_data_stock = Get_Month_StockPrice(stock_code, year_start, True)
    elif arguments[0] == '3':
        # 上市 年月報(含當月)
        stock_code = '0056'
        year_start = datetime.now().strftime('%Y') + '0101'
        month_data_stock = Get_Month_StockPrice_AddCurrent(stock_code, year_start, True)
    elif arguments[0] == '4':
        # 單股 上市 當月統計(最高,最低 及 平均)
        stock_code = '0056'
        today = datetime.now().strftime('%Y%m%d')
        month_price = Get_Month_analyze_StockPrice(stock_code, today, True)
    elif arguments[0] == '5':
        # 單股 上市 月日報
        data = Get_StockPrice('0056','20240901', True)
    elif arguments[0] == '6':
        # OTC 年月報(含當月)
        month_data_OTC = Get_Month_StockPrice_OTC('00679B', '2024', True)
    elif arguments[0] == '7':
        # get 單股股利資訊
        # support 處理季或月配
        df_all = getAllInfo2('0056', True)
    elif arguments[0] == '8':
        # get 單股股利資訊
        # support 處理年配
        df_all = getAllInfo('9921', True)
    elif arguments[0] == '9':
        # get 前一天指數及日期
        pre_index, pre_date = Get_Pre_IndexPrice(True)
    elif arguments[0] == '10':
        # get 指定日期指數
        today = datetime.now().strftime('%Y%m%d')
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        index_value = Get_IndexPrice(today, True)
        index_value = Get_IndexPrice(yesterday, True)
    elif arguments[0] == '11':
        # get 單股 及時股價
        stoce_price = Current_stock_Price_yahoo('0056', True)
    elif arguments[0] == '12':
        # get 及時指數
        Current_Index_Google(True)
    elif arguments[0] == '13':
        # get 單股基本資料
        info = get_dividend_list("00687B", True)
        print(info['名稱'])
    else:
        print(f"the index {arguments[0]} not support")
else:
    print("please input test index")
