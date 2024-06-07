# 擲骰子,繪直方圖
import numpy as np

slides = 6
n = 10000
dice = np.random.randint(1, slides+1, size=n )

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

h = plt.hist(dice, bins=slides)
print(f"bins y軸 {h[0]}")
print(f"bins x軸 {h[1]}")

plt.xlabel('點數')
plt.ylabel('出現次數')
plt.title(f"測試{n}次")

plt.show()
# bins y軸 [1650. 1647. 1650. 1736. 1633. 1684.]
# bins x軸 [1.         1.83333333 2.66666667 3.5        4.33333333 5.16666667 6.        ]