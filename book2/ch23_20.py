# 生成一元二次多項式特徵值
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# 設定基本數據
X = np.array([[1], [2], [3], [4]])

# 使用 PolynomialFeatures 生成一元二次特徵
# 生成二次多項式
degree = 2
poly = PolynomialFeatures(degree)
# fit : 學習數據的參數
# transform : 加入數據
X_poly = poly.fit_transform(X)

print(X)
# 列印生成多項式特徵
print(poly.get_feature_names_out(input_features=['x']))
print(X_poly)

# 使用 PolynomialFeatures 生成一元四次特徵
degree = 4
poly4 = PolynomialFeatures(degree)
X_poly4 = poly4.fit_transform(X)
print(poly4.get_feature_names_out(input_features=['x']))
print(X_poly4)

# [[1]
#  [2]
#  [3]
#  [4]]
# ['1' 'x' 'x^2']
# [[ 1.  1.  1.]
#  [ 1.  2.  4.]
#  [ 1.  3.  9.]
#  [ 1.  4. 16.]]
# ['1' 'x' 'x^2' 'x^3' 'x^4']
# [[  1.   1.   1.   1.   1.]
#  [  1.   2.   4.   8.  16.]
#  [  1.   3.   9.  27.  81.]
#  [  1.   4.  16.  64. 256.]]