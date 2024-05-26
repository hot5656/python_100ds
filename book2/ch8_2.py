# Numpy 實作最小平方法
# 拜訪次數 回收問卷
# 100       500
# 200       1000
# 300       2000
# 拜訪次數(1=100次) vs 業績(回收問卷)
import numpy as np
x = np.array([1, 2, 3])
y = np.array([500, 1000, 2000])

# https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
# numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)
# 計算迴歸直線, deg 多項式次數
a, b = np.polyfit(x, y, 1)
print(f"斜率{a:.2f}")
print(f"截距{b:.2f}")

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 繪迴歸直線
x2 = np.linspace(0, 5, 100)
y2 = a * x2 + b
plt.plot(x2, y2)

# 計算 2500張,需拜訪次數
y_count = 2500
x_count = (y_count - b) / a
plt.plot(x_count, y_count, "-o", color="red")
plt.text(x_count-0.9, y_count+50, f"({x_count:.2f},{y_count})")

for index, x_value in enumerate(x):
    plt.plot(x_value, y[index], "-o", color="green")

plt.xlabel('拜訪次數(單位=100)')
plt.ylabel('回收問卷')

plt.grid()
plt.show()