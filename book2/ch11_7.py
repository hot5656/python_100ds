# 蒙地卡羅模擬計算PI - 𝝿
# 2 * 2 正方形
# 圓面積/矩形面積 = PI / 4
# PI = 4 * hins / 1000000
import random

trials = 1000000
hits = 0
for i in range(trials):
    x = random.random()*2 - 1
    y = random.random()*2 - 1
    if x*x + y*y <= 1:
        hits += 1
PI = 4 * hits / trials
print(f"PI={PI}")
# PI = 3.144032