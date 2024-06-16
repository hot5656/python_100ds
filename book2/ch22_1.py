# 產生數據
from sklearn.datasets import make_regression

X, y = make_regression(n_features=1, noise=0, random_state=0)
print("X 的資料格式:")
print(type(X), len(X))
print(f"陣列維度:{X.ndim}")
print(f"陣列外型:{X.shape}")
print(f"陣列大小:{X.size}")
print(f"前5個X的樣本:")
print(X[:5])
print("="*70)

print("y 的資料格式:")
print(type(y), len(y))
print(f"陣列維度:{y.ndim}")
print(f"陣列外型:{y.shape}")
print(f"陣列大小:{y.size}")
print(f"前5個y的樣本:")
print(y[:5])

# X 的資料格式:
# <class 'numpy.ndarray'> 100
# 陣列維度:2
# 陣列外型:(100, 1)
# 陣列大小:100
# 前5個X的樣本:
# X 為 2維 陣列
# [[ 0.12691209]
#  [ 0.44386323]
#  [ 0.76103773]
#  [ 0.95008842]
#  [-0.40317695]]
# ======================================================================
# y 的資料格式:
# <class 'numpy.ndarray'> 100
# 陣列維度:1
# 陣列外型:(100,)
# 陣列大小:100
# 前5個y的樣本:
# y 為 2維 陣列
# [  5.37923312  18.81336721  32.25696819  40.26997723 -17.08885844]



