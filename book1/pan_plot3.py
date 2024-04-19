# 繪圖 - 圓餅圖
import pandas as pd
import matplotlib.pyplot as plt

# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

df = pd.DataFrame([[40,320,300,312,280],
                   [280,300,280,290,30],
                   [220,280,25,305,250]],
                  index = ['北部','中部','南部',],
                  columns = [2015,2016,2017,2018,2019])
# subplots=True 多張圖放在一個區域
df.plot(kind='pie', subplots=True, figsize=[20,20])
plt.show()