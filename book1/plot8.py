# 散佈圖
import matplotlib.pyplot as plt

x = [1, 2, 3, 4,  5,  6,  7,  8]
y = [1, 4, 9, 16, 7, 15, 17, 19]
# s 標記大小
# c 標記顏色
# marker 標記樣式, default 'o'
# alpha 透明度 0~1
sizes = [20, 200, 100, 50, 500, 1000, 60, 90]
colors = ['red', "green", "black", "orange", "purple", "pink", "cyan", "magenta"]
plt.scatter(x, y, s=sizes, c=colors)
plt.show()