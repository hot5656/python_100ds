# 單股歷年股利股息
# chrome
# //li[@class='List(n)']/div[contains(@class, 'table-row')]
# //div[contains(@class, 'table-heade')]

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定義目標網站的 URL (Yahoo 財經台股例子)
# stock_code = '9921'
stock_code = '0056'
url = f"https://tw.stock.yahoo.com/quote/{stock_code}/dividend"

# 發送 GET 請求到網站
response = requests.get(url)

# 如果請求成功，則繼續處理
if response.status_code == 200:
    # 使用 BeautifulSoup 解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    header =  soup.select("div[class*='table-header']")

    # data_elements = soup.select("li.List(n) div.table-row")
    results = soup.select("li[class*='List'] div.table-row")

    # print('*'*20)
    # print(header[0])
    # print('*'*20)
    # print(results[0])

    columns = [col.get_text(strip=True) for col in header[0].select('div')]
    # remove 多餘欄位
    columns.pop(0)

    # 打印表頭的欄位數量和內容
    # print(f"表頭欄位數量: {len(columns)}")
    # print(f"-表頭內容: {columns}-")

    # 解析 results: 提取每一行的數據
    data = []
    for row in results:
        # 提取每行的每個欄位值
        row_data = [col.get_text(strip=True) for col in row.select('div')]
        data.append(row_data)

    # 將表頭與數據結合到 Pandas DataFrame
    df = pd.DataFrame(data, columns=columns)

    # 顯示結果
    # print(df)

    # 反轉資料順序
    df_reversed = df[::-1].reset_index(drop=True)
    print(df_reversed)

    # for index, row in df_reversed.iterrows():
    #     print(f'-{row.values[0]}-')
    #     if row.values[0] == '':
    #         print("999")

    # # 移除發放期間為空或 NaN 的行
    # df_reversed = df_reversed[df_reversed['發放期間'].notna() & (df_reversed['發放期間'] != '')]

    # # 移除 for 迴圈和 if 檢查，直接顯示已過濾的結果
    # print(df_reversed)

    # empty_rows = df_reversed[df_reversed['發放期間'].isna() | (df_reversed['發放期間'] == '')]
    # print(empty_rows)

    for index, row in df_reversed.iterrows():
        # the code have error
        # if row['發放期間'] == '' or pd.isna(row['發放期間']):
        if row.values[0] == '':
            # print(f"移除行: {index}, 發放期間為空: {row['發放期間']}")
            df_reversed = df_reversed.drop(index)

    # 重設索引以確保連續性（可選）
    df_reversed.reset_index(drop=True, inplace=True)

    # 顯示結果
    print("移除後的 DataFrame：")
    print(df_reversed)
else:
    print("無法抓取資料，請確認網址是否正確。")

#     發放期間  發放期間  所屬期間   現金股利  股票股利  現金殖利率 除息日昨收價         除息日         除權日     現金股利發放日     股票股利發放日 填息天數
# 0   2024  2024  2023   5.00     -  2.09%  239.0  2024/08/23           -  2024/09/19           -    3
# 1   2023  2023  2022   7.80     -  3.84%  203.0  2023/08/25           -  2023/09/20           -    -
# 2   2022  2022  2021  10.00     -  3.77%  265.0  2022/08/19           -  2022/09/15           -

#     發放期間  發放期間    所屬期間  現金股利 股票股利  現金殖利率 除息日昨收價         除息日 除權日     現金股利發放日 股票股利發放日 填息天數
# 0   2009  2009    2008  2.00    -      -      -  2009/10/23   -  2009/11/26       -   53
# 1   2010  2010    2010     -    -      -      -           -   -           -       -    -
# 2   2011  2011    2010  2.20    -      -      -  2011/10/26   -  2011/11/29       -   80
# 3   2012  2012    2011  1.30    -      -      -  2012/10/24   -  2012/11/27       -  136
# 4   2013  2013    2012  0.85    -      -      -  2013/10/24   -  2013/11/27       -  116
# 5   2014  2014    2013  1.00    -      -      -  2014/10/24   -  2014/11/27       -   31
# 6   2015  2015    2014  1.00    -      -  22.65  2015/10/26   -  2015/11/26       -   85
# 7   2016  2016    2015  1.30    -  5.13%  25.35  2016/10/26   -  2016/11/28       -  159
# 8   2017  2017    2016  0.95    -   3.6%  26.39  2017/10/30   -  2017/12/04       -   63
# 9   2018  2018    2017  1.45    -  5.62%  25.81  2018/10/23   -  2018/11/27       -   80
# 10  2019  2019    2018  1.80    -   6.2%  29.03  2019/10/23   -  2019/11/26       -   51
# 11  2020  2020    2019  1.60    -  5.39%  29.69  2020/10/28   -  2020/12/01       -   29
# 12  2021  2021    2020  1.80    -  5.56%  32.40  2021/10/22   -  2021/11/25       -   17
# 13  2022  2022    2021  2.10    -  8.13%  25.84  2022/10/19   -  2022/11/22       -   34
# 14              2023Q2  1.00    -  2.78%  35.94  2023/07/18   -  2023/08/11       -    5
# 15              2023Q3  1.20    -  3.44%  34.90  2023/10/19   -  2023/11/14       -   23
# 16  2023  2023          2.20    -  6.30%
# 17              2023Q4  0.70    -  1.92%  36.37  2024/01/17   -  2024/02/21       -   13
# 18              2024Q1  0.79    -  2.03%  38.94  2024/04/18   -  2024/05/15       -   13
# 19              2024Q2  1.07    -  2.53%  42.37  2024/07/16   -  2024/08/09       -    -
# 20              2024Q3  1.07    -  2.74%  39.02  2024/10/17   -  2024/11/12       -    -
# 21  2024  2024          3.63    -  9.30%