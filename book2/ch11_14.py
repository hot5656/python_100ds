# shuffle 重新排列
# reshape 更改形狀
import numpy as np

arr1 = np.arange(9)
print("一維陣列")
print(arr1)
print("一維陣列重新排列")
np.random.shuffle(arr1)
print(arr1)

arr2 = np.arange(9).reshape(3,3)
print("二維陣列")
print(arr2)
print("二維陣列重新排列")
np.random.shuffle(arr2)
print(arr2)

# 一維陣列
# [0 1 2 3 4 5 6 7 8]
# 一維陣列重新排列
# [0 5 3 2 1 8 4 6 7]
# 二維陣列
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# 二維陣列重新排列
# [[3 4 5]
#  [6 7 8]
#  [0 1 2]]