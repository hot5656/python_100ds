# 計算兩條直線的夾角
import numpy as np
import math

a = np.array([1,1])
b = np.array([5,5])
c = np.array([1,5])
d = np.array([5,1])

# 向量
ab = b - a
cd = d - c
# 向量大小
norm_ab = np.linalg.norm(ab)
norm_cd = np.linalg.norm(cd)

dot_ab_cd = np.dot(ab, cd)
cos_value = dot_ab_cd/(norm_ab * norm_cd)
cos_value = dot_ab_cd/(norm_ab * norm_cd)
rad = math.acos(cos_value)
deg = math.degrees(rad)
print(f"角度是:{deg}")
# 角度是:90.0
