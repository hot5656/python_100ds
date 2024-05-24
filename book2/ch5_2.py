# 計算兩個向量的歐幾乎里德距離
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
distance = np.sqrt(np.sum((a-b)**2))
print(f"a and b 距離 : {distance:.2f}")
# a and b 距離 : 5.20