# 區域薪資統計圖 - 長條圖
import pandas as pd
import re
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager

def main():
    # 加入中文字體
    fontManager.addfont('NotoSansTC-Regular.ttf')
    matplotlib.rc('font', family='Noto Sans TC')

    sources = ["1111", "104", "CakeResume"]
    for index,item in enumerate(sources):
        print(f"({index+1}) {item}")
    kind_no = int(input("分析來源:"))
    if kind_no ==  1:
        jsb_file = "./job1.xlsx"
    elif kind_no == 2:
        jsb_file = "./job11.xlsx"
    elif kind_no == 3:
        jsb_file = "./job21.xlsx"
    else:
        print("input out of range...")
        exit(1)

    xsl = pd.ExcelFile(jsb_file)
    df = pd.read_excel(jsb_file)
    cities = ["台北", "新北", "桃園", "台中", "高雄", "台南", "其他"]
    salary_list = []

    # get 六都資料
    for i in range(len(cities)-1):
        df1 = df[df['工作地點'].str.contains(cities[i])]
        df1 = df1.reset_index(drop=True)
        for j in range(len(df1)):
            df1.iloc[j, 5] = get_salary(df1.iloc[j, 5])
            # print(f"    {cities[i]}-{j} {df1.iloc[j, 5]}")
         # 無內容無法算平均值
        if len(df1['薪資']) == 0:
            mean = 0
        else:
            mean = round(df1['薪資'].mean())
        salary_list.append(mean)

    # get 其他資料
    cities_to_exclude = ["台北", "新北", "桃園", "台中", "高雄", "台南"]
    df2 = df[~df['工作地點'].str.contains('|'.join(cities_to_exclude))]
    df2 = df2.reset_index(drop=True)
    for j in range(len(df2)):
        df2.iloc[j, 5] = get_salary(df2.iloc[j, 5])
        # print(f"    其他-{j} {df2.iloc[j, 5]}")
    # 無內容無法算平均值
    if len(df2['薪資']) == 0:
        mean = 0
    else:
        mean = round(df2['薪資'].mean())
    salary_list.append(mean)

    # 長條圖 設 width
    plt.bar(cities, salary_list, width=0.5)
    # 圖表,X,Y 標題
    # plt.title('Chart Title', fontsize=20)
    plt.title(xsl.sheet_names[0] ,fontsize=20)
    plt.xlabel('地區', fontsize=14)
    plt.ylabel('薪資', fontsize=14)

    # show 數值
    for i in range(len(cities)):
        plt.text(i, salary_list[i], str(salary_list[i]), ha='center', va='bottom')

    plt.show()

def get_salary(salary):
    salary = salary.replace(",", "")
    salaries = re.findall(f"\d+\.?\d*", salary)
    # range 平均
    if len(salaries) == 0:
        if "待遇面議" in salary:
            money = 40000
        else :
            money = float(salaries[0])
    elif len(salaries) == 1:
        money = float(salaries[0])
    else:
        money = (float(salaries[0]) + float(salaries[1])) / 2

    # 萬 * 10000
    if "萬" in salary:
        money *= 10000
    # 年薪 / 12
    if "年" in salary:
        money = money / 12

    return round(money)

if __name__ == '__main__':
    main()