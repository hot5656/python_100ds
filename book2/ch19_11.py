import numpy as np
A = np.array([[0, 2, 4, 6],
              [1, 3, 5, 7]])
B = A.T
print(f"轉置矩陣1 = {B}")
C = np.transpose(A)
print(f"轉置矩陣2 = {C}")
# 轉置矩陣1 = [[0 1]
#              [2 3]
#              [4 5]
#              [6 7]]
# 轉置矩陣2 = [[0 1]
#              [2 3]
#              [4 5]
#              [6 7]]
