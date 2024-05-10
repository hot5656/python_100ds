# 區域職缺統計圖 - 圓形圖
import pandas as pd
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
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
city_count = []

city_total = 0
for i in range(len(cities)-1):
    mask = df['工作地點'].str.contains(cities[i]) & ~(df['工作地點'] == cities[i])
    count = mask.sum()
    city_total += count
    city_count.append(count)

city_count.append(len(df) - city_total)

plt.title(xsl.sheet_names[0] + ' 職缺', fontsize=20)
# label 加入數量
labels = [f"{city} ({count})" for city, count in zip(cities, city_count)]
plt.pie(
    city_count,
    labels = labels,
    autopct = "%2.1f%%",
    shadow = True,
    startangle = 90
)
# bbox_to_anchor 1.1:距中心位置 0.5:高度位置
plt.legend(loc='best', bbox_to_anchor=(1.1, 0.5))

plt.show()