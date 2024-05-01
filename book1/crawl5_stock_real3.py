# 股票即時通知
import twstock
import requests
import os
import time
from datetime import datetime

def main():
    STOCK_NO = '2317'
    UP_PRICE = 150
    DOWN_PRICE = 130
    notify_url = "https://notify-api.line.me/api/notify"
    token = os.getenv("LINE_NOTIFY_TOKEN")
    headers = {
        "Authorization": "Bearer " + token,
        "Connect-Type" : "application/x-www-form-urlencoded"
    }

    while True :
        price = get_real_stock(STOCK_NO)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"time : {current_time}")
        if price >= UP_PRICE:
            send_line(1, price, STOCK_NO, notify_url, headers, current_time)
        elif price <= DOWN_PRICE and price != 0:
            send_line(2, price, STOCK_NO, notify_url, headers, current_time)
        time.sleep(300)

# mode = 1 可買
# mode = 2 可買
def send_line(mode, price, stock_no, notify_url, headers, current_time):
    if mode == 1:
        msg = f"{current_time} {stock_no} {price} 元可以賣出"
    elif mode == 2:
        msg = f"{current_time} {stock_no} {price} 元可以買入"

    payload = {"message": msg}
    notify = requests.post(notify_url,
                    headers = headers,
                    params = payload)
    # if notify.status_code == 200:
    #     print("Send LINE Notify success!")


def get_real_stock(stock_no):
    real = twstock.realtime.get(stock_no)
    current_price = 0
    if (real['success']):
        current_price = float(real['realtime']['latest_trade_price'])
        # print(f"即時股票資料: \n{float(real['realtime']['latest_trade_price'])}\n")
    else:
        print('errer access.')
    return current_price

if __name__ == '__main__':
    main()