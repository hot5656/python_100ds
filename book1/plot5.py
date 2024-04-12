# 並列長條圖
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

width=0.25
listx = ['c', 'c++', 'c#', 'java', 'python']
# 並列長條圖,算 x 位置
listx1 = [ x - width/2 for x in range(len(listx))]
listx2 = [ x + width/2 for x in range(len(listx))]
listy1 = [25, 20, 20, 16, 28]
listy2 = [20,  8, 18, 16, 22]
# 長條圖 設 width
plt.bar(listx1, listy1, width=width, label='男')
# buttom 設定連接位置
plt.bar(listx2, listy2, width=width, label='女')
# 圖表,X,Y 標題
# plt.title('Chart Title', fontsize=20)
plt.title('課程選修統計', fontsize=20)
plt.xlabel('課程', fontsize=14)
plt.ylabel('人數', fontsize=14)
# 並列長條圖,show x tabel
plt.xticks(range(len(listx)), labels=listx)
# label 位置
plt.legend(loc='upper center')
plt.show()