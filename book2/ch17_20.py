import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 天氣溫度
temperature = [22,25,26,27,28,29,30,31,32,33]
# 營業額
rev = [600,900,1100,720,950,1020,1000,1200,1420,1500]

# 建立二次函數迴歸模型係數
coef = np.polyfit(temperature, rev, 2)
# 建立二次函數迴歸方程式
reg = np.poly1d(coef)

print(coef.round(2))
print(reg)

plt.plot(temperature, reg(temperature) , color='red')
plt.scatter(temperature, rev)

plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度")
plt.ylabel("營業額")
plt.show()
# [   4.64 -185.73 2530.84]
#        2
# 4.642 x - 185.7 x + 2531