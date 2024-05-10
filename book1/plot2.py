# 長條圖
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

listx = ['c', 'c++', 'c#', 'java', 'python']
listy = [45, 28, 38, 32,50]
# 長條圖 設 width
plt.bar(listx, listy, width=0.5, color=['r', 'g', 'b'])
# 圖表,X,Y 標題
# plt.title('Chart Title', fontsize=20)
plt.title('課程選修統計', fontsize=20)
plt.xlabel('課程', fontsize=14)
plt.ylabel('人數', fontsize=14)

# show 數值
for i in range(len(listy)):
    plt.text(i, listy[i], str(listy[i]), ha='center', va='bottom')

plt.show()