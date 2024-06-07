# 繪製 y=2**x, y=4**x
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 30)
y2 = 2 ** x
y4 = 4 ** x

plt.plot(x, y2, label="2**x")
plt.plot(x, y4, label="4**x")
plt.plot(0, 1, '-o')

plt.legend(loc="best")
plt.axis([-3, 3, 0, 20])
plt.grid()
plt.show()