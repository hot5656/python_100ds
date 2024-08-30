# 2D 平面上使用等高線圖來表示一個二次函數的高度
import numpy as np
import matplotlib.pyplot as plt

# 建立一個網格
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
XX, YY = np.meshgrid(x, y)

# 定義一個二次函數 Z = X^2 + Y^2
Z = XX**2 + YY**2

# 創建一個圖形和軸
fig, ax = plt.subplots()

# 使用 contour 畫出等高線
contour = ax.contour(XX, YY, Z, colors='b', levels=[10, 20, 30], alpha=0.8, linestyles=['--', '-', '--'])

# 添加等高線的標籤
ax.clabel(contour, inline=True, fontsize=10)

# 設置標題和軸標籤
ax.set_title('Contour Plot Example')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

# 顯示圖形
plt.show()