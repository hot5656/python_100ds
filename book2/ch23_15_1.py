# 將兩個一維陣列組成二維陣列
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.c_[a, b]
print(c)
# [[1 4]
#  [2 5]
#  [3 6]]