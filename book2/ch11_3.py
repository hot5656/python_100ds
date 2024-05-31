# 機率乘法與加法
# 員工中獎率計算
# 7 支籤,2位中獎可抽獎

# 分數計算
from fractions import Fraction

x = Fraction(2, 7) * Fraction(1 ,6)
y = Fraction(5, 7) * Fraction(2, 6)
p = x + y
print(f"第一位中獎率 {Fraction(2, 7)}")
print(f"第二位中獎率 {p} 轉成浮點數 {float(p)}")
# 第一位中獎率 2/7
# 第二位中獎率 2/7 轉成浮點數 0.2857142857142857


