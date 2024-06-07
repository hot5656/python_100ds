# 使用隨機數據陣列產生圖像
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10000)
y = np.random.rand(10000)
# 使用 cmap='hsv' 意味著顏色將按 HSV 顏色空間進行映射，色調從 0 到 1 對應于一個色環，涵蓋所有顏色。
plt.scatter(x, y, c=y, cmap='hsv' )
# 顯示顏色條
plt.colorbar()
plt.show()