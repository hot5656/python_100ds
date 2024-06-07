import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10000)
y = [1/(1+np.e**-x) for x in x]
plt.plot(x, y, label="Logistic function")

plt.axis([-5, 5, 0, 1])
plt.legend()
plt.grid()
plt.show()