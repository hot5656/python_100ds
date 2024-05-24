# sympy 說明
import sympy as sp

# simple
x = sp.Symbol('x')
y = sp.Symbol('y')
print(x.name)
print(x + x + 2)
z = 5*x + 6*y + x*y
print(z)
# x
# 2*x + 2
# x*y + 5*x + 6*y

# 多個符號
a, b, c = sp.symbols(('a', 'b', 'c'))
print(a.name, b.name, c.name)
# a b c

# 字串轉為數學表達式
# eq = input("輸入公式:") # x**3 + 2*x**2 + 3*x + 5
# eq = sp.sympify(eq)
# print(eq)
# print(2*eq)
# result = eq.subs({x:1})
# print(result)
# 輸入公式:x**3 + 2*x**2 + 3*x + 5
# x**3 + 2*x**2 + 3*x + 5
# 2*x**3 + 4*x**2 + 6*x + 10
# 11

# 支援數學函數
# pi
# E: 歐拉數e
# sin(x), cos(x), tan(x)
# log(x,n) : 計算 n 為底數的對數,省略n為自然對數
# exp(x): e**x
# root(x,n): x 開n次方,省略n為2次方
eq2 = sp.sin(x**2) + sp.log(8,2)*x + sp.log(sp.exp(3))
result2 = eq2.subs({x:1})
print(result2)
print(result2.evalf())  # 計算值
# 由於 SymPy 主要是用於符號計算的工具，所以當進行符號替換時，會保持符號的形式而不會自動計算出實際值。
# sin(1) + 6
# 6.84147098480790
