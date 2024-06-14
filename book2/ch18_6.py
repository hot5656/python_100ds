# 計算兩個向量組成三角形面積
import numpy as np
import math

a = np.array([4, 2])
b = np.array([1, 3])
# 計算角度再算面積
# 計算向量大小
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
# 計算內積
dot_ab = np.dot(a, b)
# a.b = |a||b|cos(θ)
cos_value = dot_ab/(norm_a*norm_b)
rad = math.acos(cos_value)
# 算面積
area = norm_a * norm_b * math.sin(rad)/2
print(f"計算角度再算面積 area={area:.2f}")

# 以外積計算面積
ab_cross = np.cross(a,b)
area2 =  ab_cross / 2
print(f"以外積計算面積 area={area2:.2f}")
# 計算角度再算面積 area=5.00
# 以外積計算面積 area=5.00
