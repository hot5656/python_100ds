# 繪對數 2 及 0.5 的圖形
import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.linspace(0.1, 10, 90)
y1 = [math.log2(x) for x in x1 ]
y2 = [math.log(x, 0.5) for x in x1 ]

print(y1)
print(y2)
plt.plot(x1, y1, label="base=2")
plt.plot(x1, y2, label="base=0.5")

plt.legend(loc="best")
# plt.axis([-3, 3, 0, 20])
plt.grid()
plt.show()
