import numpy as np

# 設定 seed 可每次執行值都相同
np.random.seed(10)
x = np.random.randint(10, size=10)
print(x)

# [9 4 0 1 9 0 1 8 9 0]
# [9 4 0 1 9 0 1 8 9 0]
# [9 4 0 1 9 0 1 8 9 0]