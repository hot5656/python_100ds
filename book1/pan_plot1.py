# 繪圖 - 長條圖
import pandas as pd
import matplotlib.pyplot as plt

# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')
#                             default
# kind        圖形形式        Line(折線圖)
# title       圖形標題        None
# legend      顯示圖示說明    True
# grid        格線           False
# xlim        繪 x軸 刻度範圍 None
# ylim        繪 y軸 刻度範圍 None
# xtick       繪圖形 x軸刻度  None
# ytick       繪圖形 y軸刻度  None
# x           設定 x軸 資料   None
# y           設定 y軸 資料   None
# fontsize    設定 x,y軸刻度字體大小  None
# figsize     設定圖形長度及寬度      None
# kind: line(折線圖), hist(直方圖), scatter(散佈圖),
#       bar(長條圖), barh(橫條圖), pie(圓餅圖)

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,315],
                   [220,280,250,305,250]],
                  index = ['北部','中部','南部',],
                  columns = [2015,2016,2017,2018,2019])

g1 = df.plot(kind='bar', title='長條圖', figsize=[10,5])
g2 = df.plot(kind='barh', title='橫條圖', figsize=[10,5])
g3 = df.plot(kind='bar', stacked=True, title='堆疊圖', figsize=[10,5])
# also need srun plt.show()
plt.show()