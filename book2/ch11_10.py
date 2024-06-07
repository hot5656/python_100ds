import numpy as np

# 傳回1個 0~4 整數
x = np.random.randint(5)
print(x)
# 2

# 傳回3個 0~9 整數
x = np.random.randint(10, size=3)
print(x)
# [2 3 0]

# 傳回 3*2 個 0~9 整數
x = np.random.randint(0, 10, size=(3,2))
print(x)
# [[2 0]
#  [5 8]
#  [2 5]]