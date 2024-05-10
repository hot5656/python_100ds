import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    # ajax_url = 'https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer'
    ajax_url = 'https://www.ibon.com.tw/retail_inquiry_ajax.aspx'
    payload = {
        'strTargetField': 'COUNTY',
        'strKeyWords': '基隆市'
    }
    # try:
    ajax_resp = requests.post(ajax_url, data=payload)
    # except:
    #     ajax_resp = None
    #     # if not ajax error the end.
    #     print('if not ajax error the end.')
    # print(ajax_resp)
    # print(ajax_resp.text)
    # df = pd.read_html(ajax_resp.text, header=0)[0]
    # df = pd.read_html(ajax_resp.text, header=0)[0]
    # print(pd)
    if ajax_resp and ajax_resp.status_code == 200:
        # print(ajax_resp.text)
        soup = BeautifulSoup(ajax_resp.text, 'html.parser')
        tables = soup.select("tr")
        index = 1
        # print(tables)
        print(len(tables))
        for item in tables:
            datas = item.select("td")
            print(f"{datas[0].text}, {datas[1].text}, {datas[2].text}")
            index += 1
        # print(soup)
    else:
        print("get data error ...")


if __name__ == '__main__':
    main()