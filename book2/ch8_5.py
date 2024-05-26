# 氣溫 vs 銷售量
# 氣溫x   22, 26, 23, 28, 27, 32, 30
# 銷售量y 15, 35, 21, 62, 48, 101, 86
# 預估氣溫31的銷售量
import numpy as np
x = np.array([22, 26, 23, 28, 27, 32, 30])
y = np.array([15, 35, 21, 62, 48, 101, 86])

a, b = np.polyfit(x, y, 1)
print(f"斜率{a:.2f}")
print(f"截距{b:.2f}")

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 繪迴歸直線
x2 = np.linspace(20, 35, 50)
y2 = a * x2 + b
plt.plot(x2, y2)

# 預估氣溫31的銷售量
x_count = 31
y_count = a*x_count + b
plt.plot(x_count, y_count, "-o", color="red")
plt.text(x_count-1.5, y_count+3, f"({x_count},{int(y_count)})")


for index, x_value in enumerate(x):
    plt.plot(x_value, y[index], "-o", color="green")

plt.xlabel('氣溫')
plt.ylabel('銷售量')

plt.grid()
plt.show()
# 斜率8.89
# 截距-186.30