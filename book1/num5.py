# numpy 常用 計算及統計函式
import numpy as np

a = np.arange(1,10).reshape(3,3)
print(a)
print('最大值 max', np.max(a),)
print('最小值 min', np.min(a))
print('col , row 最大值', np.max(a, axis=0), np.max(a,axis=1))
print('總和 sum', np.sum(a))
print('乘積 prod', np.prod(a))
print('平均 mean', np.mean(a))
# 標準差是一個用來衡量一組數據散佈程度或變異程度的統計量。它衡量的是每個數據點與平均值的平均偏差，
# 因此可以幫助我們了解數據的離散程度。標準差越大，表示數據點越分散；標準差越小，表示數據點越集中
# 在平均值附近。
print('標準差 std', np.std(a))
# 變異數是標準差的平方，它也是用來衡量數據集合中數據點的分散程度或變異程度的一種統計量。與標準差類似，
# 它提供了一種了解數據集中數據點分散程度的方式，但是不像標準差那樣，它沒有取平方根。
print('變異數 var', np.var(a))

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# 最大值 max 9
# 最小值 min 1
# col , row 最大值 [7 8 9] [3 6 9]
# 總和 sum 45
# 乘積 prod 362880
# 平均 mean 5.0
# 標準差 std 2.581988897471611
# 變異數 var 6.666666666666667
b = np.random.randint(100 ,size=20)
print('')
print(b)
print('中位數 median', np.median(b))
print('最小元素索引 argmin', np.argmin(b))
print('最大元素索引 argmax', np.argmax(b))
print('陣列元素累加 cumsum', np.cumsum(b))
print('陣列元素累積 cumprod', np.cumprod(b))
# 將 b 中的數據從小到大排序後，找到排在第 80% 位置上的值
print('百分比顯示陣列中的指定值 percentile', np.percentile(b, 80))
print('最大值與最小值的差 ptp', np.ptp(b))

# [48 15  8 34 84 21 83 44 74  1 38 60 86 93 45 86 53 61 58 68]
# 中位數 median 55.5
# 最小元素索引 argmin 9
# 最大元素索引 argmax 13
# 陣列元素累加 cumsum [  48   63   71  105  189  210  293  337  411  412  450  510  596  689
#   734  820  873  934  992 1060]
# 陣列元素累積 cumprod [         48         720        5760      195840    16450560   345461760
#  -1391444992 -1094037504   645603328   645603328 -1236877312 -1198194688
#     34471936 -1089077248 -1763835904 -1366032384   614727680 -1156317184
#   1653080064   740294656]
# 百分比顯示陣列中的值 percentile 83.2
# 最大值與最小值的差 ptp 92