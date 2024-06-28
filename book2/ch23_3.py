import pandas as pd

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')
# item0 to item12 data
data = boston.iloc[:, :13]
# item13 data
target = boston.iloc[:,13:14]

# 列出資料外型
print(f"資料外型        : {boston.shape}")
print(f"自變數  樣品外型 : {data.shape}")
print(f"目標變數樣品外型 : {target.shape}")

# 列出3筆 自變數(特徵值)
print(data.head(3))
# 列出3筆 目標變數(房價)
print(target.head(3))

# 特徵值名稱
print(f"{data.columns}")
print(f"{target.columns}")

# 資料外型        : (506, 14)
# 自變數  樣品外型 : (506, 13)
# 目標變數樣品外型 : (506, 1)
#       CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  PTRATIO       B  LSTAT
# 0  0.00632  18.0   2.31     0  0.538  6.575  65.2  4.0900    1  296.0     15.3  396.90   4.98
# 1  0.02731   0.0   7.07     0  0.469  6.421  78.9  4.9671    2  242.0     17.8  396.90   9.14
# 2  0.02729   0.0   7.07     0  0.469  7.185  61.1  4.9671    2  242.0     17.8  392.83   4.03
#    MEDV
# 0  24.0
# 2  34.7
# Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
#        'PTRATIO', 'B', 'LSTAT'],
#       dtype='object')
# Index(['MEDV'], dtype='object')