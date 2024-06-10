import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 天氣溫度
temperature = [25,31,28,22,27,30,29,33,32,26]
# 營業額
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]

# 建立迴歸模型係數
coef = np.polyfit(temperature, rev, 1)
# 建立迴歸直線函數
reg = np.poly1d(coef)

print(coef.round(2))
print(reg)
print(f"計算溫度 35 度時冰品銷售營業額 = {reg(35).round(0)}")
# [  71.63 -986.22]
# 71.63 x - 986.2
# 計算溫度 35 度時冰品銷售營業額 = 1521.0

plt.plot(temperature, reg(temperature) , color='red')

plt.scatter(temperature, rev)
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度")
plt.ylabel("營業額")
plt.show()
