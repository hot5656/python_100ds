# 用來生成網格點座標矩陣，通常用於數值計算和可視化中。
# 該函數可以生成多維網格，這在多變量函數的計算和圖形繪製中特別有用。
# np.meshgrid(*xi, copy=True, sparse=False, indexing='xy')
#   *xi: 一個或多個一維數組。
#   copy: 如果為 True（默認值），則返回的數組是輸入數據的副本。否則，返回的數組是引用。
#   sparse: 如果為 True，則在生成的網格中使用稀疏矩陣。這對於處理大型數據集非常有用，因為它可以節省內存。
#   indexing: 'xy'（默認值）表示使用矩陣索引（即直角坐標系），'ij' 表示使用陣列索引。
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
# 生成網格
X, Y = np.meshgrid(x, y)
print("X:\n", X)
print("Y:\n", Y)
# X:
#  [[1 2 3]
#  [1 2 3]
#  [1 2 3]]
# Y:
#  [[4 4 4]
#  [5 5 5]
#  [6 6 6]]

# 稀疏矩陣
X2, Y2 = np.meshgrid(x, y, sparse=True)
print("X2:\n", X2)
print("Y2:\n", Y2)
# X2:
#  [[1 2 3]]
# Y2:
#  [[4]
#  [5]
#  [6]]

# 3 矩陣
z = np.array([7, 8, 9])
X3, Y3, Z3= np.meshgrid(x, y, z)
print("X3:\n", X3)
print("Y3:\n", Y3)
print("Y3:\n", Z3)
# X3:
#  [[[1 1 1]
#   [2 2 2]
#   [3 3 3]]
#  [[1 1 1]
#   [2 2 2]
#   [3 3 3]]
#  [[1 1 1]
#   [2 2 2]
#   [3 3 3]]]
# Y3:
#  [[[4 4 4]
#   [4 4 4]
#   [4 4 4]]
#  [[5 5 5]
#   [5 5 5]
#   [5 5 5]]
#  [[6 6 6]
#   [6 6 6]
#   [6 6 6]]]
# Y3:
#  [[[7 8 9]
#   [7 8 9]
#   [7 8 9]]
#  [[7 8 9]
#   [7 8 9]
#   [7 8 9]]
#  [[7 8 9]
#   [7 8 9]
#   [7 8 9]]]

# 3 矩陣 - 稀疏矩陣
# z = np.array([7, 8, 9])
X4, Y4, Z4= np.meshgrid(x, y, z, sparse=True)
print("X4:\n", X4)
print("Y4:\n", Y4)
print("Y4:\n", Z4)
# X4:
#  [[[1]
#   [2]
#   [3]]]
# Y4:
#  [[[4]]
#  [[5]]
#  [[6]]]
# Y4:
#  [[[7 8 9]]]

# # f(x,y) = x + y
# import numpy as np

# x = [-2, -1, 0 , 1 ,2]
# y = [-2, -1, 0 , 1 ,2]
# X, Y = np.meshgrid(x,y)
# print(X)
# print(Y)
