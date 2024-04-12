# 折線圖
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

listx = [1,5,7,8,13,16]
listy = [15,50,80,40,70,50]
# color: red, blue, green, yellow, black, white
# linewidth/lw: default 1.0
# linestyle/ls: -(default 實線), --(虛線), -.(虛點), :(點線),
# marker:標記像式
# .點 o圓 *星 h六邊形 H六邊形2 v/^正倒三角形 </>左右三角形 d鑽型 D鑽型2
# +十字 x叉叉 s矩形 _橫線 |直線 p五角形 1234上左下右人字姓
# markersize/ms:標記大小
# color+ls+marker example 'g--*'
plt.plot(listx, listy, color='red', lw='2.0', ls='-.', marker='*', ms=12
         ,label='label')
# 第二條
listx2 = [2,4,6,8,11,16]
listy2 = [10,40,80,30,50,60]
plt.plot(listx2, listy2, "g-^", ms=12
         ,label='label2')
# label 位置:upper right(default)
# plt.legend(loc = 'upper left')
plt.legend()
# 圖表,X,Y 標題
# plt.title('Chart Title', fontsize=20)
plt.title('圖表標題', fontsize=20)
plt.xlabel('X-Label', fontsize=14)
plt.ylabel('Y-Label', fontsize=14)
# x,y 顯示範圍
plt.xlim(0,20)
plt.ylim(0, 100)
# 格線 alpha(透明度)
plt.grid(color="green", ls=":", lw=1, alpha=0.5)
# 自訂刻度
tickx = [2,4,6,8,10,12,14,16,18,20]
plt.xticks(tickx)
# plt.ytricks(ticky)
# 刻度參數
plt.tick_params(axis='both', labelsize='16', colors="green")
# plt.tick_params(direction='out', length=6, width=2, colors='r',
#                grid_color='r', grid_alpha=0.5)
plt.show()