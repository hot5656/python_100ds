# 角度弧度的換算
import numpy as np

degrees = [30, 45, 60, 90, 120, 135, 150, 180]
for degree in degrees:
    print(f"角度={degree} 弧度={np.pi*degree/180:.3f}")
# 角度=30 弧度=0.524
# 角度=45 弧度=0.785
# 角度=60 弧度=1.047
# 角度=90 弧度=1.571
# 角度=120 弧度=2.094
# 角度=135 弧度=2.356
# 角度=150 弧度=2.618
# 角度=180 弧度=3.142
