# 橫條圖
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

listy = ['c', 'c++', 'c#', 'java', 'python']
listx = [45, 28, 38, 32,50]
# 橫條圖 設 height
plt.barh(listy, listx, height=0.5, color=['r', 'g', 'b'])
# 圖表,X,Y 標題
# plt.title('Chart Title', fontsize=20)
plt.title('課程選修統計', fontsize=20)
plt.ylabel('課程', fontsize=14)
plt.xlabel('人數', fontsize=14)
plt.show()