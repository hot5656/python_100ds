# numpy array 運算
import numpy as np
a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
print('a array:\n', a)
print('b array:\n', b)
# a array:
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# b array:
#  [[10 11 12]
#  [13 14 15]
#  [16 17 18]]

# 對 array 運算
print('a array + 1:\n', a + 1)
print('a array ** 2:\n', a ** 2 )
print('a array < 5:\n', a  < 5 )
# a array + 1:
#  [[ 2  3  4]
#  [ 5  6  7]
#  [ 8  9 10]]
# a array ** 2:
#  [[ 1  4  9]
#  [16 25 36]
#  [49 64 81]]
# a array < 5:
#  [[ True  True  True]
#  [ True False False]
#  [False False False]]

# 取出 array
print('a array row 0:\n', a[0,:])
print('a array col 0:\n', a[:,0])
# a array row 0:
#  [1 2 3]
# a array col 0:
#  [1 4 7]

# array 交互運算(arry 形狀相同)
print('array a+b :\n', a+b)
print('array a*b :\n', a*b)
# array a+b :
#  [[11 13 15]
#  [17 19 21]
#  [23 25 27]]
# array a*b :
#  [[ 10  22  36]
#  [ 52  70  90]
#  [112 136 162]]

# array 內積計算 .dot
# a col == b row
print('a,b 內積:\n', a.dot(b))
# a,b 內積:
#  [[ 84  90  96]
#  [201 216 231]
#  [318 342 366]]