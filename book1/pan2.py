# DataFrame create - pandas 二維陣列
import pandas as pd
# create DataFrame
df = pd.DataFrame([[65,92,78,83,70],
                   [90,72,76,93,56],
                   [81,85,91,89,77],
                   [79,53,47,94,80]])
print('df1')
print(type(df))
print(df)
# <class 'pandas.core.frame.DataFrame'>
#     0   1   2   3   4
# 0  65  92  78  83  70
# 1  90  72  76  93  56
# 2  81  85  91  89  77
# 3  79  53  47  94  80

# 自訂索引,行
df2 = pd.DataFrame([[65,92,78,83,70],
                   [90,72,76,93,56],
                   [81,85,91,89,77],
                   [79,53,47,94,80]],
                  index=['大明','小王','張山','李四'],
                  columns=['英文','國文','數學','社會','生活'])
print('df2')
print(df2)
#     英文  國文  數學  社會  生活
# 大明  65  92  78  83  70
# 小王  90  72  76  93  56
# 張山  81  85  91  89  77
# 李四  79  53  47  94  80

# create DataFrame by dict
scores = {
 '英文':{'大明':65, '小王':90, '張山':81, '李四':79},
 '國文':{'大明':92, '小王':72, '張山':85, '李四':53},
 '數學':{'大明':25, '小王':92, '張山':21, '李四':72},
 '社會':{'大明':35, '小王':93, '張山':31, '李四':73},
 '生活':{'大明':45, '小王':94, '張山':41, '李四':74}
}
df3 = pd.DataFrame(scores)
print('df3')
print(df3)
#     英文  國文  數學  社會  生活
# 大明  65  92  25  35  45
# 小王  90  72  92  93  94
# 張山  81  85  21  31  41
# 李四  79  53  72  73  74

# create DataFrame by Series(dict)
se1 = pd.Series({'大明':65, '小王':90, '張山':81, '李四':79})
se2 = pd.Series({'大明':92, '小王':72, '張山':85, '李四':53})
se3 = pd.Series({'大明':25, '小王':92, '張山':21, '李四':72})
se4 = pd.Series({'大明':35, '小王':93, '張山':31, '李四':73})
se5 = pd.Series({'大明':45, '小王':94, '張山':41, '李四':74})
df4 = pd.DataFrame({
        '英文':se1,
        '國文':se2,
        '數學':se3,
        '社會':se4,
        '生活':se5})
print('df4')
print(df4)
#     英文  國文  數學  社會  生活
# 大明  65  92  25  35  45
# 小王  90  72  92  93  94
# 張山  81  85  21  31  41
# 李四  79  53  72  73  74

# create DataFrame by Series(concat)
se1 = pd.Series({'大明':65, '小王':90, '張山':81, '李四':79})
se2 = pd.Series({'大明':92, '小王':72, '張山':85, '李四':53})
se3 = pd.Series({'大明':25, '小王':92, '張山':21, '李四':72})
se4 = pd.Series({'大明':35, '小王':93, '張山':31, '李四':73})
se5 = pd.Series({'大明':45, '小王':94, '張山':41, '李四':74})
df5 = pd.concat([se1,se2,se3,se4,se5], axis=1)
df5.columns = ['英文','國文','數學','社會','生活']
print('df5')
print(df5)
#     英文  國文  數學  社會  生活
# 大明  65  92  25  35  45
# 小王  90  72  92  93  94
# 張山  81  85  21  31  41
# 李四  79  53  72  73  74