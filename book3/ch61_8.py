# get ETF 基本資料
from ch61_lib import *

# https://www.stockq.org/etf/etf_high_dividend.php
etf_list1 = [
    '0056',
    '00878',
    '00713',
    '00701',
    '00702',
    '00730',
    '00731',
    '00771',
    '00882',
    '00900',
    '00907',
    '00915',
    '00918',
    '00919',
    '00929',
    '00930',
    '00932',
    '00934',
    '00936',
    '00939',
    '00940',
    '00943',
    '00944',
    '00946',
]

etf_list2 = [
    '0050',
    '006208',
    '006203',
    '006204',
    '00657',
    '00661',
    '00645',
    '00703',
    '00700',
    '006205',
    '00752',
    '00885',
    '00660',
    '00668',
    '00662',
    '00646',
    '00678',
    '00830',
    '00714',
    '00682U',
    '00635U',
    '00738U',
]

etf_list3 = [
    '00679B',
    '00687B',
    '00795B',
    '00764B',
    '00779B',
    '00931B',
    '00696B',
    '00768B',
    '00857B',
]

def etf_basic(title, etfs):
    print(f"==== {title} ===")
    head_show = 0
    for item in etfs:
        info = get_dividend_list(item)
        if head_show == 0:
            keys = list(info.keys())
            # print key
            for index in range(len(keys)):
                print(f'{custom_ljust(keys[index], key_length[index])}', end=' ')
            head_show = 1

        print("")
        # print info
        for index, (key, value) in enumerate(info.items()):
            print(f'{custom_ljust(value, key_length[index])}', end=' ')
    print("")

key_length = [6, 20, 24, 36, 24, 20, 20, 20]
etf_basic("高股息 ETF", etf_list1)
etf_basic("指數 ETF", etf_list2)
etf_basic("美國長期公債", etf_list3)
