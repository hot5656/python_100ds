# package FinMind - 抓取每日歷史紀錄
# pip3 install FinMind
# https://www.twse.com.tw/zh/trading/historical/stock-day.html
from FinMind.data import DataLoader

FM = DataLoader()
a = FM.taiwan_stock_daily(stock_id='0050', start_date='2020-01-01', end_date='2024-10-01')
print(a)

#             date stock_id  Trading_Volume  Trading_money    open     max     min   close  spread  Trading_turnover
# 0     2020-01-02     0050         4882015      476649683   97.05   98.00   97.05   97.65    0.70              2421
# 1121  2024-09-25     0050        12464313     2339725240  187.70  188.00  187.35  197.65    0.00              3080
# 1121  2024-09-25     0050        12464313     2339725240  187.70  188.00  187.35  187.75    2.75             15933
# 1122  2024-09-26     0050        17369543     3290621957  189.60  190.00  188.75  189.30    1.55             15267
# 1123  2024-09-27     0050        11999510     2280157942  190.20  191.25  188.60  188.90   -0.40             15599
# 1124  2024-09-30     0050        14461065     2678744441  186.55  187.20  183.95  183.95   -4.95             32756
# 1125  2024-10-01     0050         9883064     1816503951  183.90  184.60  183.35  183.60   -0.35             12966
# [1126 rows x 10 columns]