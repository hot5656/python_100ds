# array create, show information and modify shape
import numpy as np

# 建立 array np.array(list/tuple, dtype=資料格式(default int64))
np1 = np.array([1,2,3,4]) # list
np2 = np.array((4,5,6,7)) # tuple
print(type(np1), np1)
print(type(np2), np2)

# <class 'numpy.ndarray'> [1 2 3 4]
# <class 'numpy.ndarray'> [4 5 6 7]

# 建立 順序 array
# np.arange([start,] stop [,step] )
na = np.arange(0, 32, 2)
print(na)
# [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30]

# 建立 等距 array(float)
# np.linespace(start, stop, item number)
na2 = np.linspace(1,16,3)
print(na2)

# create 0 array
# np.zeors((x,..))
a = np.zeros((5))
b = np.zeros((2,3))
print(a)
print(b)
# [0. 0. 0. 0. 0.]
# [[0. 0. 0.]
#  [0. 0. 0.]]

# create 1 array
# np.ones((x,))
a = np.ones((5))
print(a)

# show array information
print('dim:', b.ndim)
print('shape:', b.shape)
print('size:', b.size)
# dim: 2
# shape: (2, 3)
# size: 6

# change array shape
adata = np.arange(1,17)
print(adata)
bdata = adata.reshape(4,4)
bdata[0,0] = 9
print(adata)
print(bdata)
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]
# [ 9  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]
# [[ 9  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]