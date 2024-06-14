import numpy as np

A = np.matrix([[3, 2],
               [1, 2]])
B = np.linalg.inv(A)
C = np.matrix([[5],
               [-1]])
print(f"反矩陣 : {B}")
print(f"E : {B*A}")
print(f"解方程式 : {B*C}")
# 反矩陣 : [[ 0.5  -0.5 ]
#           [-0.25  0.75]]
# E : [[1.00000000e+00 2.22044605e-16]
#      [1.11022302e-16 1.00000000e+00]]
# 解方程式 : [[ 3.]
#            [-2.]]


