# 成  立,規  模,市  價,淨  值,折溢價

import requests
from bs4 import BeautifulSoup

def get_dividend_list(symbol):
    div_url = f'https://www.moneydj.com/ETF/X/Basic/Basic0004.xdjhtm?etfid={symbol}.TW'
    r = requests.get(div_url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    results = soup.select("table tr")
    index=1
    for item in results:
        print(f'({index}) {item}')
        index += 1

    print(f'data7 ---> {results[7]}')
    print(f'data8 ---> {results[8]}')
    print(f'data9 ---> {results[9]}')
    print(f'data10 ---> {results[10]}')
    print(f'data11 ---> {results[11]}')
    data7 = results[7].select("td")[0].text
    data8 = results[8].select("td")[0].text
    data9 = results[9].select("td")[1].text
    data10 = results[10].select("td")[1].text
    data11 = results[11].select("td")[1].text
    # print(f'-{results[9].select("td")[1]}-')
    print(f'stock_code={symbol}')
    print(f'成  立 : {data7}')
    print(f'規  模 : {data8}')
    print(f'市  價 : {data9}')
    print(f'淨  值 : {data10}')
    print(f'折溢價 : {data11}')

    return 1

dividend = get_dividend_list("0050")