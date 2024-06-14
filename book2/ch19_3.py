import numpy as np

A = np.matrix([[1,2],
               [3, 4]])
B = np.matrix([[5,6],
               [7,8]])
print(f"A * B = {A * B}")

C = np.matrix([[ 1, 0, 2],
               [-1, 3, 1]])
D = np.matrix([[3,1],
               [2,1],
               [1,0]])
print(f"C * D = {C * D}")
# A * B = [[19 22]
#          [43 50]]
# C * D = [[5 1]
#          [4 2]]

