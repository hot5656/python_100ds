# 組合(combination) - 從5數字中選出3個數字
import itertools

n = {1, 2, 3, 4, 5}
r = 3
A = set(itertools.combinations(n , 3))
print(f"組合 = {len(A)}")
for a in A:
    print(a)
# 組合 = 10
# (2, 4, 5)
# (1, 3, 5)

# 計算2個骰子有多少組合
n2 = {1, 2, 3, 4, 5, 6}
A2 = set(itertools.combinations(n2 , 2))
print(f"骰子組合 = {len(A2)}")
# 骰子組合 = 15

