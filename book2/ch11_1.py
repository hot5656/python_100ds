# 隨機整數函數
# import random

# min = 1
# max = 6
# target1 = 1
# target2 = 6
# n = 10000
# counter1 = 0
# counter2 = 0
# for i in range(n):
#     once = random.randint(min, max)
#     if once == target1:
#         counter1 += 1
#     if once == target2:
#         counter2 += 1
# print(f"total{n}, target {target1} {counter1} times, 機率{counter1/n}")
# print(f"total{n}, target {target2} {counter2} times, 機率{counter2/n}")

# 計算隨機產生值,並繪出長條圖
# 隨機整數函數
import random

min = 1
max = 6
n = 10000
dice = [0] * 6
for i in range(n):
    data = random.randint(min, max)
    dice[data-1] += 1
print(dice)

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

listx = range(1,7)
plt.bar(listx, dice)

plt.xlabel('數字', fontsize=14)
plt.ylabel('次數', fontsize=14)
# show 數值
for i in range(len(dice)):
    plt.text(i+1, dice[i], str(dice[i]), ha='center', va='bottom')

plt.show()
# [1618, 1699, 1674, 1692, 1696, 1621]




