# 紀錄回測交易明細
from Data import getData
import pandas as pd

# 取得回測資料
prod = '0050'
data = getData(prod, '2013-01-01', '2022-05-01')

# 初始部位
position = 0
trade = pd.DataFrame()
# 開始回測
for i in range(data.shape[0]-1):
    # 取得策略會應用到的變數
    c_time = data.index[i]
    c_low = data.loc[c_time, 'low']
    c_high = data.loc[c_time, 'high']
    c_close = data.loc[c_time, 'close']
    c_open = data.loc[c_time, 'open']
    # 取下一期資料作為進場資料
    n_time = data.index[i+1]
    n_open = data.loc[n_time, 'open']

    # 進場程序
    if position == 0:
        # 進場邏輯 : 下引線是紅K 2倍以上
        if c_close > c_open and (c_close - c_open) *2 < (c_open - c_low):
            position = 1
            order_i = i
            order_time = n_time
            order_price = n_open
            order_unit = 1

    # 出場程序
    elif position == 1:
        # 出場邏輯: 持有3天以上, 紅k
        if i > order_i + 3 and c_close > c_open :
            position = 0
            cover_time = n_time
            cover_price = n_open
            # 交易紀錄
            trade=pd.concat([trade, pd.DataFrame([[
                prod,
                'Buy',
                order_time,
                order_price,
                cover_time,
                cover_price,
                order_unit
                ]])], ignore_index=True)
print(trade)

#         0    1          2       3          4       5  6
# 0    0050  Buy 2013-03-14   55.50 2013-03-28   54.70  1
# 1    0050  Buy 2013-04-11   53.95 2013-04-17   54.00  1
# 2    0050  Buy 2013-06-06   56.20 2013-06-18   55.15  1
# 3    0050  Buy 2013-06-27   54.05 2013-07-05   55.25  1
# 4    0050  Buy 2013-07-11   56.75 2013-07-18   57.60  1
# ..    ...  ...        ...     ...        ...     ... ..
# 119  0050  Buy 2021-10-13  133.40 2021-10-20  137.05  1
# 120  0050  Buy 2021-10-25  136.00 2021-11-02  136.80  1
# 121  0050  Buy 2021-12-08  143.10 2021-12-16  141.35  1
# 122  0050  Buy 2022-01-13  149.55 2022-01-21  143.90  1
# 123  0050  Buy 2022-02-14  143.95 2022-02-18  143.50  1