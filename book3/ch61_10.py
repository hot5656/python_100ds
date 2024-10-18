# 值利率列表
from ch61_lib import *

etf_list1 = [
    '0056',
    '00878',
    '00713',
    '00701',
    '00702',
    '00730',
    '00731',
    '00771',
    '00882',
    '00900',
    '00907',
    '00915',
    '00918',
    '00919',
    '00929',
    '00930',
    '00932',
    '00934',
    '00936',
    '00939',
    '00940',
    '00943',
    '00944',
    '00946',
]

etf_list2 = [
    '0050',
    '006208',
    '006203',
    '006204',
    '00657',
    '00661',
    '00645',
    '00703',
    '00700',
    '006205',
    '00752',
    '00885',
    '00660',
    '00668',
    '00662',
    '00646',
    '00678',
    '00830',
    '00714',
    '00682U',
    '00635U',
    '00738U',
]

etf_list3 = [
    '00679B',
    '00687B',
    '00795B',
    '00764B',
    '00779B',
    '00931B',
    '00696B',
    '00768B',
    '00857B',
]

def etf_rate(title, etfs):
    print(f"==== {title} ===")
    for stock_code in etfs:
        df_all = getAllInfo2(stock_code)
        # print(df_all)
        print(f"stock_code={stock_code}")
        for index, row in df_all.iterrows():
            year= row.values[0]
            year_start = year + '0101'
            month_data = Get_Month_StockPrice(stock_code, year_start)
            if len(month_data) == 0:
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

                year_1st_price =  month_data.iloc[0]["Average"]
                year_last_price = month_data.iloc[-1]["Average"]
                rate = round((((year_last_price * ( 1 + stock_dividend/100) + cash_dividend)/year_1st_price) - 1) * 100, 2)
                print(f"{year}  股價: {year_1st_price:7} --> {year_last_price:7}, 現金股利={cash_dividend:5}, 股票股利={stock_dividend:5}, 值利率={rate:7}%")

etf_rate("高股息 ETF", etf_list1)
etf_rate("指數 ETF", etf_list2)
etf_rate("美國長期公債", etf_list3)