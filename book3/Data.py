import yfinance as yf
import pandas as pd
import os

datapath = 'data'

def getData(prod, st, en):
    if not os.path.exists(datapath):
        os.makedirs(datapath)

    bakfile = 'data//YF_%s_%s_%s_stock_daily_adj.csv' % (prod, st, en)
    if os.path.exists(bakfile):
        data = pd.read_csv(bakfile)
        data['Date'] = pd.to_datetime(data['Date'])
        data = data.set_index('Date')
    else:
        data = yf.download(f"{prod}.TW", start=st , end=en)
        data.columns = [i.lower() for i in data.columns]
        if data.shape[0] == 0:
            print('No data')
            return pd.DataFrame()
        data.to_csv(bakfile)
    return data
