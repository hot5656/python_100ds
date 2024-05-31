# sympy 模組與集合
# sympy FiniteSet 可建立集合
from sympy import FiniteSet
A = FiniteSet(1, 2, 3)
print(A)
# {1, 2, 3}

# 建立集合冪集
a = A.powerset()
print(a)
# FiniteSet(EmptySet, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3})


