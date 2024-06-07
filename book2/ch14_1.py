# 對數函數
import numpy as np
import math

n = np.linspace(1.1, 10, 90)
print(n)

count =0
for i in n:
    count += 1
    print(f"{i:2.1f} = {np.log10(i):4.3f}", end="  ")
    if count % 5 == 0:
        print()

print(math.sqrt(3))

