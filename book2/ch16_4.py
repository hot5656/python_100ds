# 計算sin(), cos()
import numpy as np

degrees = [x*30 for x in range(0,13)]
for d in degrees:
    rad = np.radians(d)
    sin = np.sin(rad)
    cos = np.cos(rad)
    print(f"度數:{d:3d}\t弧度:{rad:3.2f}\tsin{d:3d}={sin:3.2f} cos{d:3d}={cos:3.2f}")
# 度數:  0        弧度:0.00       sin  0=0.00 cos  0=1.00
# 度數: 30        弧度:0.52       sin 30=0.50 cos 30=0.87
# 度數: 60        弧度:1.05       sin 60=0.87 cos 60=0.50
# 度數: 90        弧度:1.57       sin 90=1.00 cos 90=0.00
# 度數:120        弧度:2.09       sin120=0.87 cos120=-0.50
# 度數:150        弧度:2.62       sin150=0.50 cos150=-0.87
# 度數:180        弧度:3.14       sin180=0.00 cos180=-1.00
# 度數:210        弧度:3.67       sin210=-0.50 cos210=-0.87
# 度數:240        弧度:4.19       sin240=-0.87 cos240=-0.50
# 度數:270        弧度:4.71       sin270=-1.00 cos270=-0.00
# 度數:300        弧度:5.24       sin300=-0.87 cos300=0.50
# 度數:330        弧度:5.76       sin330=-0.50 cos330=0.87
# 度數:360        弧度:6.28       sin360=-0.00 cos360=1.00
