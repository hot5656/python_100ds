# 圓形圖
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

# title
plt.title('區域圓形圖', fontsize=20)

sizes = [25, 30, 15, 10]
locations = ['北部', '西部', '東部', '南部']
# label 加入數量
labels = [f"{location} ({size})" for location, size in zip(locations, sizes)]
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0, 0.2, 0)
# labels 項目標題
# colors
# explode 項目凸出距離, 0 正常
# labeldistance 項目具圓心距離 1.1 表 1.1倍
# autopct 項目百分比格式 %...%, %2.1f%%:整數2位小數1位
# shadow 陰影
# startangle 起始角度(逆時針算)
plt.pie(sizes,
        explode = explode,
        labels = labels,
        colors = colors,
        labeldistance = 1.1,
        autopct = '%2.1f%%',
        pctdistance = 0.6,
        shadow = True,
        startangle = 90)
# label 位置:upper right(default)
# plt.legend(loc = 'best')
# bbox_to_anchor 1.1:距中心位置 0.5:高度位置
plt.legend(loc='best', bbox_to_anchor=(1.1, 0.5))

plt.show()