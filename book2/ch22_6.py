# 繪製身高與體中資料圖表
import matplotlib.pyplot as plt

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

height = [1.6, 1.63, 1.71, 1.73, 1.83]
weight = [55, 58, 62, 65, 71]

plt.plot(height, weight, "ko")
plt.axis([1.5, 1.85, 50, 90])
plt.title("身高 vs 體重")
plt.xlabel("身高")
plt.ylabel("體重")
plt.grid()
plt.show()