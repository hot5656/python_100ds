# 年配值利率
from ch61_lib import *


# also support call getAllInfo()
stock_code = '9921'
df_all = getAllInfo(stock_code, True)

# stock_code = '0056'
# stock_code = '00919'
# stock_code = '00657'
# stock_code = '00679B'
# stock_code = '00662'
# df_all = getAllInfo2(stock_code)
print(df_all)
print(len(df_all))
print(f"stock_code={stock_code}")
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
