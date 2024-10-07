# 撰寫進出場邏輯
from Data import getData

# 取得回測資料
prod = '0050'
# data = getData('0050', '2008-01-03', '2024-10-02')
# data = getData('0050', '2020-01-03', '2024-10-02')
data = getData(prod, '2013-01-01', '2022-05-01')

# 初始部位
position = 0

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
            print(c_time, '觸發進場信號 隔日進場', order_time, '進場價', order_price, '進場', order_unit, '單位')
    # 出場程序
    elif position == 1:
        # 出場邏輯: 持有3天以上, 紅k
        if i > order_i + 3 and c_close > c_open :
            position = 0
            cover_time = n_time
            cover_price = n_open
            print(c_time, '觸發出場訊號 隔日出場', cover_time, '出場價', cover_price)


# 2013-03-13 00:00:00 觸發進場信號 隔日進場 2013-03-14 00:00:00 進場價 55.5 進場 1 單位
# 2013-03-27 00:00:00 觸發出場訊號 隔日出場 2013-03-28 00:00:00 出場價 54.7
# 2013-04-10 00:00:00 觸發進場信號 隔日進場 2013-04-11 00:00:00 進場價 53.95 進場 1 單位
# 2013-04-16 00:00:00 觸發出場訊號 隔日出場 2013-04-17 00:00:00 出場價 54.0
# 2013-06-05 00:00:00 觸發進場信號 隔日進場 2013-06-06 00:00:00 進場價 56.2 進場 1 單位
# 2013-06-17 00:00:00 觸發出場訊號 隔日出場 2013-06-18 00:00:00 出場價 55.15
# 2013-06-26 00:00:00 觸發進場信號 隔日進場 2013-06-27 00:00:00 進場價 54.05 進場 1 單位
# 2013-07-04 00:00:00 觸發出場訊號 隔日出場 2013-07-05 00:00:00 出場價 55.25
# 2013-07-10 00:00:00 觸發進場信號 隔日進場 2013-07-11 00:00:00 進場價 56.75 進場 1 單位
# 2013-07-17 00:00:00 觸發出場訊號 隔日出場 2013-07-18 00:00:00 出場價 57.6