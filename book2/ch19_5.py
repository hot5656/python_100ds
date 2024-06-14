# 計算甲,乙各吃下多少熱量
import numpy as np

A = np.matrix([[1, 2, 1],
               [2, 1, 2]])
B = np.matrix([[30],[50],[20]])
print(f"A * B = {A * B}")
# A * B = [[150]
#          [150]]