import numpy as np
import matplotlib.pyplot as plt

x = np.array([8,9,10,7,8,9,5,7,9,8])
y = np.array([12,15,16,18,6,11,3,12,11,16])

x_mean = np.mean(x)
y_mean = np.mean(y)

xi_x =[v - x_mean for v in x]
yi_x =[v - y_mean for v in y]

data1 = [0] * 10
data2 = [0] * 10
data3 = [0] * 10
for i in range(len(x)):
    data1[i] = xi_x[i] * yi_x[i]
    data2[i] = xi_x[i]**2
    data3[i] = yi_x[i]**2

v1 = np.sum(data1)
v2 = np.sum(data2)
v3 = np.sum(data3)
r = v1/((v2**0.5)*(v3**0.5))
print(f"coefficient={r:.3f}")
# coefficient=0.505

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]


xpt1 = np.linspace(0, 12, 12)
ypt1 = [y_mean for xp in xpt1]
ypt2 = np.linspace(0, 20, 20)
xpt2 = [x_mean for xp in ypt2]

plt.scatter(x, y)
plt.plot(xpt1, ypt1, color="g")
plt.plot(xpt2, ypt2, color="r")

# plt.axis([0, 12, 0, 20])
plt.title("滿意度 vs 再購買次數")
plt.xlabel("滿意度")
plt.ylabel("再購買次數")
plt.grid()
plt.show()