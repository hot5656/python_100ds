# 即時股價讀取
# pip install twstock
import twstock

stock = twstock.Stock('2317')
print(f"最近31筆收盤價: \n{stock.price}\n")
print(f"最近31筆盤中最高價: \n{stock.high}\n")
print(f"最近31筆盤中最低價: \n{stock.low}\n")
print(f"最近31筆日期資料: \n{stock.date}\n")
print(f"最近6日期資料: \n{stock.date[-6:]}\n")
real = twstock.realtime.get('2317')
if (real['success']):
    print(f"即時股票資料: \n{real}\n")
else:
    print('errer access.')

stock_march = stock.fetch(2024, 3)
print(f"2024年3月資料: {len(stock_march)} \nfirst={stock_march[0]}\n last={stock_march[-1]}\n")
stock_from_march = stock.fetch_from(2024, 3)
print(f"2024年3月至今: {len(stock_from_march)}\nfirst={stock_from_march[0]}\n last={stock_from_march[-1]}\n")
print(f"1st date:{stock_from_march[0].date}")
print(f"1st open:{stock_from_march[0].open}")

# 最近31筆收盤價:
# [132.0, 136.0, 136.0, 138.0, 142.5, 145.5, 145.5, 142.0, 148.5, 155.5, 150.0, 150.5, 159.0, 159.0, 158.0, 158.0, 154.5, 150.0, 150.5, 146.0, 141.0, 146.5, 148.0, 143.0, 143.0, 144.0, 156.0, 151.5, 155.0, 158.5, 156.0]

# 最近31筆盤中最高價:
# [133.0, 137.0, 136.0, 142.0, 145.0, 148.5, 147.5, 147.0, 150.0, 157.0, 157.5, 154.5, 159.5, 159.0, 160.0, 161.5, 160.0, 153.5, 153.5, 150.0, 143.0, 147.5, 148.5, 147.5, 145.5, 146.5, 157.0, 154.5, 158.0, 161.0, 161.0]

# 最近31筆盤中最低價:
# [127.0, 131.5, 130.0, 135.5, 139.0, 142.0, 143.0, 139.0, 143.0, 150.0, 150.0, 150.0, 151.0, 155.0, 156.5, 155.5, 154.0, 147.0, 148.5, 144.5, 137.5, 141.0, 144.5, 140.0, 141.5, 143.5, 146.5, 151.0, 154.0, 156.0, 156.0]

# 最近31筆日期資料:
# [datetime.datetime(2024, 3, 15, 0, 0), datetime.datetime(2024, 3, 18, 0, 0), datetime.datetime(2024, 3, 19, 0, 0), datetime.datetime(2024, 3, 20, 0, 0), datetime.datetime(2024, 3, 21, 0, 0), datetime.datetime(2024, 3, 22, 0, 0), datetime.datetime(2024, 3, 25, 0, 0), datetime.datetime(2024, 3, 26, 0, 0), datetime.datetime(2024, 3, 27, 0, 0), datetime.datetime(2024, 3, 28, 0, 0), datetime.datetime(2024, 3, 29, 0, 0), datetime.datetime(2024, 4, 1, 0, 0), datetime.datetime(2024, 4, 2, 0, 0), datetime.datetime(2024, 4, 3, 0, 0), datetime.datetime(2024, 4, 8, 0, 0), datetime.datetime(2024, 4, 9, 0, 0), datetime.datetime(2024, 4, 10, 0, 0), datetime.datetime(2024, 4, 11, 0, 0), datetime.datetime(2024, 4, 12, 0, 0), datetime.datetime(2024, 4, 15, 0, 0), datetime.datetime(2024, 4, 16, 0, 0), datetime.datetime(2024, 4, 17, 0, 0), datetime.datetime(2024, 4, 18, 0, 0), datetime.datetime(2024, 4, 19, 0, 0), datetime.datetime(2024, 4, 22, 0, 0), datetime.datetime(2024, 4, 23, 0, 0), datetime.datetime(2024, 4, 24, 0, 0), datetime.datetime(2024, 4, 25, 0, 0), datetime.datetime(2024, 4, 26, 0, 0), datetime.datetime(2024, 4, 29, 0, 0), datetime.datetime(2024, 4, 30, 0, 0)]

# 最近6日期資料:
# [datetime.datetime(2024, 4, 23, 0, 0), datetime.datetime(2024, 4, 24, 0, 0), datetime.datetime(2024, 4, 25, 0, 0), datetime.datetime(2024, 4, 26, 0, 0), datetime.datetime(2024, 4, 29, 0, 0), datetime.datetime(2024, 4, 30, 0, 0)]

# 即時股票資料:
# {'timestamp': 1714458600.0, 'info': {'code': '2317', 'channel': '2317.tw', 'name': '鴻海', 'fullname': '鴻海精密工業股份有限公司', 'time': '2024-04-30 14:30:00'}, 'realtime': {'latest_trade_price': '156.0000', 'trade_volume': '12296', 'accumulate_trade_volume': '71882', 'best_bid_price': ['156.0000', '155.5000', '155.0000', '154.5000', '154.0000'], 'best_bid_volume': ['431', '2825', '2767', '538', '734'], 'best_ask_price': ['156.5000', '157.0000', '157.5000', '158.0000', '158.5000'], 'best_ask_volume': ['571',
# '776', '1911', '1753', '1873'], 'open': '159.5000', 'high': '161.0000', 'low': '156.0000'}, 'success': True}

# 2024年3月資料: 21
# first=Data(date=datetime.datetime(2024, 3, 1, 0, 0), capacity=28288633, turnover=2907270754, open=103.0, high=103.5, low=102.0, close=102.0, change=-1.0, transaction=11037)
#  last=Data(date=datetime.datetime(2024, 3, 29, 0, 0), capacity=154117085, turnover=23632502947, open=157.0, high=157.5, low=150.0, close=150.0, change=-5.5, transaction=97343)

# 2024年3月至今: 41
# first=Data(date=datetime.datetime(2024, 3, 1, 0, 0), capacity=28288633, turnover=2907270754, open=103.0, high=103.5, low=102.0, close=102.0, change=-1.0, transaction=11037)
#  last=Data(date=datetime.datetime(2024, 4, 30, 0, 0), capacity=73433543, turnover=11579053739, open=159.5, high=161.0, low=156.0, close=156.0, change=-2.5, transaction=39006)

# 1st date:2024-03-01 00:00:00
# 1st open:103.0