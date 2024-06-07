import numpy as np
import statistics as st

x = [66, 57, 25, 80, 60, 15, 120, 39, 80, 50]
x2 = [66, 57, 25, 80, 60, 15, 120, 39, 80, 50, 77]
print(f"加總: {sum(x)}")
print(f"平均數: {sum(x)/len(x)}")
print(f"平均數2: {np.mean(x)}")
# 中位數
print(f"中位數: {np.median(x)}")
print(f"中位數2: {np.median(x2)}")
# bincount 傳回 array lenth 為最大值 +1
# x 陣列必需為正整數陣列, 傳回 array 為 0 ~ max 數字數量
print(f"x bincount : {len(np.bincount(x))}")
print(f"x2 bincount : {len(np.bincount(x2))}")
# argmax 傳回最大值索引
print(f"x argmax : {np.argmax(x)} {x[np.argmax(x)]}")
print(f"x2 argmax : {np.argmax(x2)} {x2[np.argmax(x)]}")
# argmin 傳回最小值索引
print(f"x argmin : {np.argmin(x)} {x[np.argmin(x)]}")
print(f"x2 argmin : {np.argmin(x2)} {x2[np.argmin(x)]}")
# 眾數(mode):出現最高次數的數字
print(f"x mode:{st.mode(x)}")

# 加總: 592
# 平均數: 59.2
# 平均數2: 59.2
# 中位數: 58.5
# 中位數2: 60.0
# x bincount : 121
# x2 bincount : 121
# x argmax : 6 120
# x2 argmax : 6 120
# x argmax : 5 15
# x2 argmax : 5 15
# x mode:80