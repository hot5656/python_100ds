# 解一元一次方程式
import sympy as sp

# 3x+5 = 8
x = sp.Symbol('x')
eq = 3*x + 5 - 8
ans = sp.solve(eq)
print(ans)
print(type(ans))
# [1]
# <class 'list'>