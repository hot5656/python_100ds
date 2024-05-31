# 集合相乘 - 笛卡兒積
# 笛卡兒積指從2個集合各提出一個元素,所有可能集合,元素內容是元祖(tuple)
from sympy import *
A = FiniteSet("a", "b")
B = FiniteSet("c", "d")
AB = A * B
for ab in AB:
    print(f"{type(ab)} {ab}")
# <class 'tuple'> (a, c)
# <class 'tuple'> (b, c)
# <class 'tuple'> (a, d)
# <class 'tuple'> (b, d)

C = FiniteSet("a", "b", "c", "d", "e")
D = FiniteSet("f", "q")
CD = C * D
print(f"len of CD : {len(CD)}")
for cd in CD:
    print(f"{cd}")
# len of CD : 10
# (a, f)
# (b, f)
# (a, q)
# (c, f)
# (b, q)
# (d, f)
# (c, q)
# (e, f)
# (d, q)
# (e, q)

# 集合的 n 次方
AA = FiniteSet("a", "b")
AAA = AA**3
print(f"len of AAA : {len(AAA)}")
for a in AAA:
    print(f"{a}")
# len of AAA : 8
# (a, a, a)
# (b, a, a)
# (a, b, a)
# (b, b, a)
# (a, a, b)
# (b, a, b)
# (a, b, b)
# (b, b, b)
