# 階層觀念
# 5 個客戶分別在5個城市,有多少拜訪路徑? 5!
import itertools

n = {"A", "B", "C", "D", "E"}
r = 5
A = set(itertools.permutations(n, r))
print(f"元素數量 = {len(A)}")
for a in A:
    print(a)
# 元素數量 = 120
# ('C', 'D', 'E', 'A', 'B')
# ('B', 'E', 'D', 'A', 'C')
# ......

# 30個城市客戶的路徑
# 假設電腦每秒可計算 10000000000000(10兆) 路徑, 多久可算完
import math

N2 = 30
combinations = math.factorial(N2)
print(f"combinations = {combinations}")
times = 10000000000000
years = combinations/times/60/60/24/365
print(f"計算 {years:.2f} 年")
# combinations = 265252859812191058636308480000000
# 計算 841111300774.32 年
