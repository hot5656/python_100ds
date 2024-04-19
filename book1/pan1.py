# Series create - pandas 一維陣列
import pandas as pd

# Series create
se = pd.Series([1,2,3,4])
print(type(se))
print(se)
print(se.values)
print(se.index)
# <class 'pandas.core.series.Series'>
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
# [1 2 3 4]
# RangeIndex(start=0, stop=4, step=1)


# 自訂索引
stocks = ['p1', 'p2', 'p3', 'p4']
prices  = [42, 510, 694, 2115]
# index 索引
se2 = pd.Series(prices, index=stocks)
print('')
print(se2)
# p1      42
# p2     510
# p3     694
# p4    2115
# dtype: int64

# create Series by dict
dict1 = {'Taipei': '台北', 'Taichung': '台中', 'Kaohsiung': '高雄', }
se3 = pd.Series(dict1)
print('')
print(se3)
print(se3.values)
print(se3.index)
# Taipei       台北
# Taichung     台中
# Kaohsiung    高雄
# dtype: object
# ['台北' '台中' '高雄']
# Index(['Taipei', 'Taichung', 'Kaohsiung'], dtype='object')

# get value
print('')
print(se[2])
print(se3['Kaohsiung'])
# 3
# 高雄