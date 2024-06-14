# 計算甲和乙在超商及百貨公司採買各需多少錢
import numpy as np

A = np.matrix([[2, 3, 1],
               [3, 2, 5]])
B = np.matrix([[30, 50],
               [60, 80],
               [50, 60]])
print(f"A * B = {A * B}")
# A * B = [[290 400]
#          [460 610]]