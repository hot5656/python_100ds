# 計算弧長
# 弧度 = 2𝝿r * degree/360
import numpy as np

r = 10
degrees = [30, 60, 90, 120]
for degree in degrees:
    print(f"角度={degree:3d} 弧長={2*np.pi*r*degree/360:.3f}")
# 角度= 30 弧長=5.236
# 角度= 60 弧長=10.472
# 角度= 90 弧長=15.708
# 角度=120 弧長=20.944