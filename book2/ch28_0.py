import matplotlib.pyplot as plt
import numpy as np

x = [2.5, 4, 4.2, 1, 2, 2.5]
y = [4.5, 4, 3.8, 2.8, 2, 1.2]

plt.scatter(x, y, marker='o')

x2 =  [x for x in range(0,6)]
y2 = [ y + 1 for y in x2]
plt.plot(x2, y2, "-*")


xx, yy = np.meshgrid(np.arange(0, 5, 0.1),
                     np.arange(0, 5, 0.1))

Z = xx.ravel() +  yy.ravel() - 4

# print(xx)
# print(yy)
# print(Z)
# for z in Z:
#     print(z, end=' ')
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3)
plt.show()