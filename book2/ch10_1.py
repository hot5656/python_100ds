# nPr(permutation-排列):從 n 個位數圖提出r個數字排列
# n*(n-1)*(n-2)...
# 4P3
# [itertools](https://docs.python.org/3/library/itertools.html)
import itertools
n = {1, 2, 3, 4}
r = 3
A = set(itertools.permutations(n, r))
print(f"元素數量 = {len(A)}")
for a in A:
    print(a)
# 元素數量 = 24
# (2, 1, 3)
# (4, 2, 1)
# .....

# 5P2
n2 = {"a", "b", "c", "d", "e"}
r2 = 2
A2 = set(itertools.permutations(n2, r2))
print(f"元素數量 = {len(A2)}")
for a2 in A2:
    print(a2)
# 元素數量 = 20
# ('c', 'b')
# ('e', 'a')
# .....

