import numpy as np

A = np.matrix([[1,2,3], [4,5,6]])
B = np.matrix([[4,5,6], [7,8,9]])
print(f"A + B = {A + B}")
print(f"A - B = {A - B}")
# A + B = [[ 5  7  9]
#          [11 13 15]]
# A - B = [[-3 -3 -3]
#          [-3 -3 -3]]