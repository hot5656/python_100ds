# 業務分析機率計算集繪製長條圖
import matplotlib.pyplot as plt
import math
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

def probability(k):
    num = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return num*success**(k)*fail**(n-k)

n = 5
success = 0.75
# 修改次數及成功率
# n = 10
# success = 0.35
fail = 1 - success
p = []
for k in range(0,n+1):
    if k == 0:
        p.append(fail**n)
    elif k == n:
        p.append(success**n)
    else:
        p.append(probability(k))

# show 機率加總
# total = 0
# for value in p:
#     total += value
#     print(f"{value} {total}")

print(p)
listx = [i for i in range(0,n+1) ]
plt.bar(listx, p)

plt.title(f'銷售機率分析n={n} 成功率:{success}')
plt.xlabel('銷售成功數')
plt.ylabel('機率')

plt.show()
# 0.0009765625 0.0009765625
# 0.0146484375 0.015625
# 0.087890625 0.103515625
# 0.263671875 0.3671875
# 0.3955078125 0.7626953125
# 0.2373046875 1.0
# [0.0009765625, 0.0146484375, 0.087890625, 0.263671875, 0.3955078125, 0.2373046875]

# [0.013462743344628911, 0.0724916949326172, 0.17565295310595708, 0.25221962497265626, 0.2376684927626953, 0.1535704107082031, 0.0689097996767578, 0.02120301528515624, 0.0042813780864257795, 0.0005123016513671872, 2.758547353515623e-05]
