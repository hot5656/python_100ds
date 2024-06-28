import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('data23_19.csv')
X = pd.DataFrame(df.x)
print(df)
print(X)

# 使用 PolynomialFeatures 生成一元二次特徵
degree = 2
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

# 列印生成多項式特徵
print(poly.get_feature_names_out())
print(X_poly)

#   x    y
# 0  1  1.5
# 1  2  3.0
# 2  3  4.5
# 3  4  4.2
# 4  5  5.2
# 5  6  5.5
#    x
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5
# 5  6
# ['1' 'x' 'x^2']
# [[ 1.  1.  1.]
#  [ 1.  2.  4.]
#  [ 1.  3.  9.]
#  [ 1.  4. 16.]
#  [ 1.  5. 25.]
#  [ 1.  6. 36.]]