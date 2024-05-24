# 解一元二次方程式的根
# x**2 - 2x - 8 = 0
# x**2 - 2x + 1 = 0
# x**2 + x + 1 = 0
from sympy import *

# 兩個根
x = Symbol("x")
f = x**2 - 2*x - 8
roots = solve(f)
print(roots)
# [-2, 4]

# 一個根
f = x**2 - 2*x + 1
roots = solve(f)
print(roots)
# [1]

# 無實數根
f = x**2 + x + 1
roots = solve(f)
print(roots)
number_roots = [root.evalf() for root in roots]
print(number_roots)
# [-1/2 - sqrt(3)*I/2, -1/2 + sqrt(3)*I/2]
# [-0.5 - 0.866025403784439*I, -0.5 + 0.866025403784439*I]

# 算實際值(當含函數式)
f = 3*(x-2)**2 - 2
# solve 函數的輸出是符號表達式。這些表達式可能是涉及根號或其他符號的形式。
# 如果我們需要實際的數值，我們需要進一步轉換這些符號表達式為數值。
roots = solve(f)
print(roots)
number_roots = [root.evalf() for root in roots]
print(number_roots)
# [2 - sqrt(6)/3, sqrt(6)/3 + 2]
# [1.18350341907227, 2.81649658092773]

