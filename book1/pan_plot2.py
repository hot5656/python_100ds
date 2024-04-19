# 繪圖 - 折線圖
import pandas as pd
import matplotlib.pyplot as plt

# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,315],
                   [220,280,250,305,250]],
                  index = ['北部','中部','南部',],
                  columns = [2015,2016,2017,2018,2019])

g1 = df.iloc[0].plot(kind='line', legend=True,
                            xticks=range(2015,2020),
                            title = '公司年度銷售表',
                            figsize=[10,5])
g1 = df.iloc[1].plot(kind='line', legend=True,
                            xticks=range(2015,2020))
g1 = df.iloc[2].plot(kind='line', legend=True,
                            xticks=range(2015,2020))
plt.show()