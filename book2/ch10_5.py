# 重複排列
# n**r
# 5個數字可重複排列於3個位置 5*5*5=125
import itertools
n = {1, 2, 3, 4, 5}
A = set(itertools.product(n, n , n))
print(f"元素數量 = {len(A)}")
for a in A:
    print(a)
# 元素數量 = 125
# (5, 3, 3)
# (5, 4, 2)
# .....