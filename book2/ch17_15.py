import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 天氣溫度
temperature = [25,31,28,22,27,30,29,33,32,26]
# 營業額
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]

print(f"相關係數 = {np.corrcoef(temperature, rev).round(2)}")
# 相關係數 = [[1.   0.87]
#  [0.87 1.  ]]

plt.scatter(temperature, rev)
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度")
plt.ylabel("營業額")
plt.show()