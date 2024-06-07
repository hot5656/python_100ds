# 繪製 0.1 ~ 9.99 的 logit 函數
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 0.99, 100)
y = [np.log(x/(1-x)) for x in x]
plt.plot(x, y, label="logit function")
plt.plot(0.5, np.log(0.5/(1-0.5)), "-o")
print(np.log(0.5/(1-0.5)))

plt.axis([0, 1, -5, 5])
plt.legend()
plt.grid()
plt.show()


