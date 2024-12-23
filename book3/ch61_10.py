# 值利率列表(含本月)
# python .\ch61_10.py 1 : show eft list 1
# python .\ch61_10.py 2 : show eft list 2
# python .\ch61_10.py 3 : show eft list 3
# python .\ch61_10.py t : show eft list 4
# python .\ch61_10.py : show all etf
from ch61_lib import *
import sys

etf_list1 = [
    '00878',
    '0056',
    '00929',
    '00919',
    '00940',
    '00713',
    '00939',
    '00918',
    '00882',
    '00934',
    '00915',
    '00900',
    '00936',
    '00946',
    '00932',
    '00701',
    '00930',
    '00907',
    '00731',
    '00944',
    '00730',
    '00943',
    '00771',
    '00702',
]

etf_list2 = [
    '0050',
    '006208',
    '00662',
    '00830',
    '00646',
    '00885',
    '00752',
    '006205',
    '00645',
    '00661',
    '00738U',
    '00635U',
    '00700',
    '006203',
    '00714',
    '00657',
    '00668',
    '00660',
    '00678',
    '00703',
    '006204',
    '00682U',
]

etf_list3 = [
    '00679B',
    '00687B',
    '00795B',
    '00764B',
    '00931B',
    '00779B',
    '00696B',
    '00768B',
    '00857B',
]

bank_list4 = [
    '2801',
    '2809',
    '2812',
    '2816',
    '2820',
    '2832',
    '2834',
    '2836',
    '2836A',
    '2838',
    '2838A',
    '2845',
    '2849',
    '2850',
    '2851',
    '2852',
    '2855',
    '2867',
    '2880',
    '2881',
    '2881A',
    '2881B',
    '2881C',
    '2882',
    '2882A',
    '2882B',
    '2883',
    '2883B',
    '2884',
    '2885',
    '2886',
    '2887',
    '2887E',
    '2887F',
    '2887Z1',
    '2888',
    '2888A',
    '2888B',
    '2889',
    '2890',
    '2891',
    '2891B',
    '2891C',
    '2892',
    '2897',
    '2897B',
    '5876',
    '5880',
    '6005',
    '6024',
]

etf_list9 = [
    # bank error year 2024/11/01
    # '2887F',
    # '2891C',
    # 食品 and 2 ETF
    # '1231',
    # '1216',
    # '00905',
    # '00922',
    # bank last
    # '6005',
    # '6024',
    # 小車金融
    # '5880',
    # '2880',
    # '2886',
    # 中鋼,台塑四寶
    '2002',
    '1301',
    '1303',
    '1326',
    '6505',
]

def etf_rate(title, etfs):
    stocks= get_stock_code()
    print(f"==== {title} ===")
    # print(etfs)
    for i, stock_code in enumerate(etfs):
        df_all = getAllInfo2(stock_code)

        try :
            print(f"({i+1:2}) stock_code={stock_code} {stocks.loc[stock_code, 'Name']}")
        except :
            # 加入OTC名稱
            info = get_dividend_list(stock_code)
            print(f"({i+1:2}) stock_code={stock_code} {info['名稱']}")

        this_year = int(datetime.now().strftime('%Y'))
        today = datetime.now().strftime('%Y%m%d')

        if len(df_all) == 0:
            year_int = int(datetime.now().strftime('%Y'))
            point_stock = 'wait'
            list_years = []
            while year_int >= 1990 :
                year = str(year_int)
                year_start = year + '0101'

                if point_stock == 'wait':
                    month_data_stock = Get_Month_StockPrice(stock_code, year_start)
                    if len(month_data_stock) == 0:
                        month_data_OTC = Get_Month_StockPrice_OTC(stock_code, year)
                        point_stock = 'otc'
                    else:
                        if this_year == year_int:
                            month_data_stock = Get_Month_StockPrice_AddCurrent(stock_code, year_start)
                        else:
                            month_data_stock = Get_Month_StockPrice(stock_code, year_start)
                        month_data_OTC = pd.DataFrame()
                        point_stock = 'stock'
                elif point_stock == 'stock':
                    if this_year == year_int:
                        month_data_stock = Get_Month_StockPrice_AddCurrent(stock_code, year_start)
                    else:
                        month_data_stock = Get_Month_StockPrice(stock_code, year_start)
                    month_data_OTC = pd.DataFrame()
                else:
                    # otc
                    month_data_OTC = Get_Month_StockPrice_OTC(stock_code, year)
                    month_data_stock = pd.DataFrame()

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
            for item in reversed(list_years):
                print(item)
        else :
            for index, row in df_all.iterrows():
                # print(f"第 {index+1} 行的值: {row.values}")
                year= row.values[0]
                year_start = year + '0101'

                month_data_stock = Get_Month_StockPrice(stock_code, year_start)
                if len(month_data_stock) == 0:
                    month_data_OTC = Get_Month_StockPrice_OTC(stock_code, year)
                else:
                    month_data_OTC = pd.DataFrame()
                    if this_year == int(year):
                        month_data_stock = Get_Month_StockPrice_AddCurrent(stock_code, year_start)
                    else:
                        month_data_stock = Get_Month_StockPrice(stock_code, year_start)

                if len(month_data_stock) == 0 and len(month_data_OTC) == 0:
                    print(f"{year} - 資料不足")
                else:
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

arguments = sys.argv[1:]
if len(arguments) !=0:
    if arguments[0] == '1':
            etf_rate("高股息 ETF", etf_list1)
    elif arguments[0] == '2':
        etf_rate("指數 ETF", etf_list2)
    elif arguments[0] == '3':
        etf_rate("美國長期公債", etf_list3)
    elif arguments[0] == '4':
        etf_rate("金融股", bank_list4)
    elif arguments[0] == 't':
        etf_rate("test", etf_list9)
else:
    etf_rate("高股息 ETF", etf_list1)
    etf_rate("指數 ETF", etf_list2)
    etf_rate("美國長期公債", etf_list3)