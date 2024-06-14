import numpy as np

A = np.matrix([[1, 2],
               [3, 4]])
B = np.matrix([[1, 0],
               [0, 1]])
print(f"A * B = {A * B}")
print(f"B * A = {B * A}")
# A * B = [[1 2]
#          [3 4]]
# B * A = [[1 2]
#          [3 4]]