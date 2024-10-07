# 資料繪圖
# 繪製蠟燭圖
# pip3 install mplfinance
import pandas as pd
from Data import getData
import mplfinance as mpf

# data = getData('0050', '20')
data = getData('0050', '2024-05-01', '2024-10-02')
print(data.head())

# mpf.plot(data)
# 繪製蠟燭圖
# mpf.plot(data, type='candle')

# list support style
# print(mpf.available_styles())
# yahoo(上漲為 green)
# mpf.plot(data, type='candle', style='yahoo')

# 自訂 style #1
mcolor = mpf.make_marketcolors(up='r', down='g', inherit=True)
# Create a style using the defined market colors
mstyle = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mcolor)
# mpf.plot(data, type='candle', style=mstyle)
# 顯示成交量
mpf.plot(data, type='candle', style=mstyle, volume=True)


#               open    high     low   close  adj close   volume
# Date
# 2024-05-02  157.35  157.35  156.00  156.15     155.36  6217027
# 2024-05-03  158.55  158.65  156.45  156.95     156.15  5689696
# 2024-05-06  159.00  160.15  159.00  159.20     158.39  8596258
# 2024-05-07  160.25  160.55  159.50  160.10     159.29  6228736
# 2024-05-08  160.00  160.80  159.65  160.70     159.88  5977267






