# BackTest.py
# pip3 install mplfinance
import mplfinance as mpf
import pandas as pd


# addop 繪製副圖
def ChartCandle(data, addop=[]):
    mcolor = mpf.make_marketcolors(up='r', down='g', inherit=True)
    mstyle = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mcolor)
    mpf.plot(data, addplot=addop ,type='candle', style=mstyle, volume=True)

# 繪製交易圖
def ChartTrade(data, trade=pd.DataFrame(), addp=[], v_enable=True):
    addp = addp.copy()
    data1 = data.copy()

    # 如有交易紀錄,則把交易紀錄與K線彙整
    if trade.shape[0]>0:
        # 將物件複製出來,不影響原交易明細變數
        trade1 = trade.copy()
        # 取出進場明細,透過時間索引將資料合併
        buy_order_trade = trade[[2,3]]
        buy_order_trade = buy_order_trade.set_index(2)
        buy_order_trade.columns = ['buy_order']
        buy_order_trade = buy_order_trade.drop_duplicates()
        # 取出出場明細,透過時間索引將資料合併
        buy_cover_trade = trade[[4,5]]
        buy_cover_trade = buy_cover_trade.set_index(4)
        buy_cover_trade.columns = ['buy_cover']
        buy_cover_trade=buy_cover_trade.drop_duplicates()
        # 將交易紀錄與K線資料彙整
        data1 = pd.concat([data1, buy_order_trade, buy_cover_trade], axis=1)

        # 將交易紀錄透過副圖的方式繪製
        addp.append(mpf.make_addplot(data1['buy_order']
                                     ,type='scatter',color='#FF4500'
                                    ,marker='^', markersize=50 )) #red
        addp.append(mpf.make_addplot(data1['buy_cover']
                                     ,type='scatter',color='#16982B'
                                    ,marker='^', markersize=50 )) # green

    # show size for data
    # print("^^^^^^^^^^^^^^^^^^^^")
    # print(data.shape)


    # # 繪製圖表
    mcolor = mpf.make_marketcolors(up='r', down='g', inherit=True)
    mstyle = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mcolor)
    # WARNING: YOU ARE PLOTTING SO MUCH DATA THAT IT MAY NOT BE
    #      POSSIBLE TO SEE DETAILS (Candles, Ohlc-Bars, Etc.)
    # mpf.plot(data, addplot=addp ,type='candle', style=mstyle, volume=v_enable)


    # #   TO SILENCE THIS WARNING, set `type='line'` in `mpf.plot()`
    # #    OR set kwarg `warn_too_much_data=N` where N is an integer
    # #    LARGER than the number of data points you want to plot.
    # mpf.plot(data, addplot=addp ,type='line', style=mstyle, volume=v_enable)
    mpf.plot(data, addplot=addp ,type='candle', style=mstyle, volume=v_enable, warn_too_much_data=10000)

