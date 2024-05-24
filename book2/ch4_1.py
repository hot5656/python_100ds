# 解聯立方程式
# a  +  b = 1
# 5a + b  = 2

from sympy import Symbol, solve
a = Symbol("a")
b = Symbol("b")
# 定義公式要右邊為 0
eq1 = a + b - 1
eq2 = 5*a + b -2
ans = solve((eq1, eq2))
print(type(ans))
print(ans)
print(f"a={ans[a]}")
print(f"b={ans[b]}")
# <class 'dict'>
# {a: 1/4, b: 3/4}
# a=1/4
# b=3/4


