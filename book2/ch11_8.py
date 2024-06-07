# 蒙地卡羅模擬計算PI - 𝝿 繪圖
import matplotlib.pyplot as plt
import random
import math

trials = 5000
hits = 0
radius = 50
for i in range(trials) :
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    if math.sqrt((x-50)**2 + (y-50)**2) <= radius:
        plt.plot(x, y, "-o", c="y")
        hits += 1
    else:
        plt.plot(x, y, "-o", c="g")

PI = 4 * hits / trials
print(f"PI={PI}")

plt.axis('equal')
plt.show()
# PI=3.1272