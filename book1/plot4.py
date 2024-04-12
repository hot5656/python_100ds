# 堆疊長條圖
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

listx = ['c', 'c++', 'c#', 'java', 'python']
listy1 = [25, 20, 20, 16, 28]
listy2 = [20,  8, 18, 16, 22]
# 長條圖 設 width
plt.bar(listx, listy1, width=0.5, label='男')
# buttom 設定連接位置
plt.bar(listx, listy2, width=0.5, bottom=listy1 ,label='女')
# 圖表,X,Y 標題
# plt.title('Chart Title', fontsize=20)
plt.title('課程選修統計', fontsize=20)
plt.xlabel('課程', fontsize=14)
plt.ylabel('人數', fontsize=14)
# label 位置
plt.legend()
plt.show()