# get ETF 基本資料(依規模排序)+指數
# python .\ch61_9.py etf : show eft
# python .\ch61_9.py 0 : show eft list 0 追蹤股票
# python .\ch61_9.py 1 : show eft list 1
# python .\ch61_9.py 2 : show eft list 2
# python .\ch61_9.py 3 : show eft list 3
# python .\ch61_9.py t : show eft list 4
# python .\ch61_9.py : only show index
from ch61_lib import *
import sys
import re

# https://www.stockq.org/etf/etf_high_dividend.php

etf_list0 = [
    '00713',
    '00915',
    '0050',
    '006208',
]

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

etf_list4 = [
    '00662',
    '00830',
    '00646',
    '00885',
    '00752',
]

# 提取數字並轉換為浮點數，作為排序的依據
def extract_scale(scale_text):
    scale_number = re.findall(r"[\d,]+\.\d+|[\d,]+", scale_text)[0]
    return float(scale_number.replace(",", ""))

# 列印 ETF 資料並根據「規模」排序
def etf_basic(title, etfs):
    print(f"==== {title} ===")

    etf_data = []

    # 提取所有 ETF 資料
    for item in etfs:
        try:
            info = get_dividend_list(item)
            etf_data.append(info)  # 儲存資料以便排序
        except Exception as e:
            print(f"Error fetching data for ETF {item}: {e}")

    # 根據「規模」進行排序
    sorted_data = sorted(etf_data, key=lambda x: extract_scale(x["規模"]), reverse=True)

    # 列印表頭
    if sorted_data:
        print(f'    ', end=' ')
        keys = list(sorted_data[0].keys())
        for index in range(len(keys)):
            print(f'{custom_ljust(keys[index], key_length[index])}', end=' ')
        print("")  # 表頭結束換行

        # 列印排序後的 ETF 資料
        for i, info in enumerate(sorted_data):
            print(f'({i+1:2})', end=' ')
            for index, (key, value) in enumerate(info.items()):
                print(f'{custom_ljust(value, key_length[index])}', end=' ')
            print("")  # 每個 ETF 資料列印後換行

    print("")

key_length = [6, 20, 24, 36, 24, 20, 20, 20]
arguments = sys.argv[1:]
# if len(arguments) != 0 and 'etf' in arguments:
if len(arguments) != 0:
    if arguments[0] == 'etf':
        etf_basic("高股息 ETF", etf_list1)
        etf_basic("指數 ETF", etf_list2)
        etf_basic("美國長期公債", etf_list3)
    elif arguments[0] == '0':
        etf_basic("追蹤 ETF", etf_list0)
    elif arguments[0] == '1':
        etf_basic("高股息 ETF", etf_list1)
    elif arguments[0] == '2':
        etf_basic("指數 ETF", etf_list2)
    elif arguments[0] == '3':
        etf_basic("美國長期公債", etf_list3)
    elif arguments[0] == 't':
        etf_basic("test 公債", etf_list4)

today = datetime.now().strftime('%Y/%m/%d')
index = Current_Index_Google()
pre_index, pre_date = Get_Pre_IndexPrice()
rate = ((index/pre_index)-1)*100
print(f'  {index}:{rate:.2}%({round(index-pre_index, 2)}) ({today}), {pre_index} ({pre_date})')

