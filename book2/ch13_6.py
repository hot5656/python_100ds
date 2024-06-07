# 繪製 y=0.5**x, y=0.25**x(底數小於1)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 30)
y2 = 0.5 ** x
y4 = 0.25 ** x

plt.plot(x, y2, label="0.25**x")
plt.plot(x, y4, label="0.5**x")
plt.plot(0, 1, '-o')

plt.legend(loc="best")
plt.axis([-3, 3, 0, 20])
plt.grid()
plt.show()