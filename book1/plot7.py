# 直方圖(值的統計)
import matplotlib.pyplot as plt

# bins bin數量
# orientation 圖形方向 vertical(default)/horizontal
data = [3,4,2,3,4,5,6,7,8,9,4,6,2,0,1,9,7,6,6,5,4,
        3,4,2,3,4,5,6,7,8,9,4,6,2,0,1,9,7,6,6,5,4,
        3,4,2,3,4,5,6,7,8,9,4,6,2,0,1,9,7,6,6,5,4,
        3,4,2,3,4,5,6,7,8,9,4,6,2,0,1,9,7,6,6,5,4,
        3,4,2,3,4,5,6,7,8,9,4,6,2,0,1,9,7,6,6,5,4,
        ]
# plt.hist(data, bins=10)
plt.hist(data, bins=10, density=True)

plt.xlabel('Value')
plt.ylabel('Counts')
plt.grid(True)
plt.show()
