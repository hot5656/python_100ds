# 繪製執行時間關係圖(n=1~5)
# O(1), O(logn), O(n), O(nlogn), O(n*n)
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1,5,5)
print(xpt)
ypt1 = xpt / xpt
ypt2 = np.log2(xpt)
ypt3 = xpt
ypt4 = xpt*np.log2(xpt)
ypt5 = xpt*xpt
print(ypt1)
print(ypt2)
print(ypt3)
print(ypt4)
print(ypt5)

plt.plot(xpt, ypt1, '-o', label="O(1)")
plt.plot(xpt, ypt2, '-o', label="O(logn)")
plt.plot(xpt, ypt3, '-o', label="O(n)")
plt.plot(xpt, ypt4, '-o', label="O(nlogn)")
plt.plot(xpt, ypt5, '-o', label="O(n*n)")
plt.legend(loc="best")
plt.axis("equal")
plt.show()