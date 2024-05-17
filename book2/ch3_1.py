# y = 3x - 18
import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

x = [x for x in range(1,11)]
y = [3 * y - 18 for y in x]
# 標記 每個 x 的 x 座標
plt.xticks(x)
# x 顯示範圍 0~10, y 顯示範圍 -20~15
plt.axis([0,10, -20, 15])
plt.plot(x,y, "-*")
plt.xlabel('小孩人數')
plt.ylabel('蘋果數量')
plt.grid()

plt.show()