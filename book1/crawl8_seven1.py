# 下載單一超市門市資料
import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    ajax_url = 'https://www.ibon.com.tw/retail_inquiry_ajax.aspx'
    payload = {
        'strTargetField': 'COUNTY',
        'strKeyWords': '基隆市'
    }
    try:
        ajax_resp = requests.post(ajax_url, data=payload)
    except:
        ajax_resp = None

    if ajax_resp and ajax_resp.status_code == 200:
        soup = BeautifulSoup(ajax_resp.text, 'html.parser')
        tables = soup.select("tr")

        del tables[0]
        for data in tables:
            items = data.select("td")
            for item in items:
                print(item.text.strip(), end=',' )
            print()
    else:
        print("get data error ...")

if __name__ == '__main__':
    main()