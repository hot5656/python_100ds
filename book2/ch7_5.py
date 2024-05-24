# 一元三次圖形繪製
import matplotlib.pyplot as plt
import numpy as np

# 上下圖
# subplot(2,1,1)
# subplot(2,1,2)
plt.figure(figsize=[8,8])
# fig 1
plt.subplot(2,1,1)
line_x =  np.linspace(-1, 1, 100)
line_y = line_x**3 - line_x
plt.plot(line_x, line_y, color="green")
plt.grid()

# fig 2
plt.subplot(2,1,2)
line2_x =  np.linspace(-2, 2, 100)
line2_y = line2_x**3 - line2_x
plt.plot(line2_x, line2_y, color="red")
plt.grid()

plt.show()