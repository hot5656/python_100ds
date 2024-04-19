# numpy 排序
import numpy as np

# 一維陣列的排序
# replace=False 不重複
a = np.random.choice(50, size=10, replace=False)
print(a)
print('排序後的陣列', np.sort(a))
print('排序後的索引', np.argsort(a))
# [14 49 15 33 43 29 20 47 31 19]
# 排序後的陣列 [14 15 19 20 29 31 33 43 47 49]
# 排序後的索引 [0 2 9 6 5 8 3 4 7 1]

# 多維陣列的排序
b = np.random.randint(0,10,(3,5))
print('\n',b)
print('直行排序')
print(np.sort(b, axis=0))
print('橫列排序')
print(np.sort(b, axis=1))

#  [[0 5 9 9 8]
#  [5 0 0 0 4]
#  [3 0 6 5 1]]
# 直行排序
# [[0 0 0 0 1]
#  [3 0 6 5 4]
#  [5 5 9 9 8]]
# 橫列排序
# [[0 5 8 9 9]
#  [0 0 0 4 5]
#  [0 1 3 5 6]]