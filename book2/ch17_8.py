# 繪製成績長條圖
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f"平均成績 = {np.mean(sc)}")
print(f"中位數成績 = {np.median(sc)}")
print(f"眾數成績 = {st.mode(sc)}")

hist = [0] * 9
for s in sc :
    n = int(s/10) - 1
    hist[n] += 1
# print(hist)

x = np.arange(len(hist))
plt.bar(x, hist, width=0.5 )

plt.xticks(x, (10,20,30,40,50,60,70,80,90))
plt.title("成績表")
plt.xlabel("分數")
plt.ylabel("學生人數")
plt.show()
# 平均成績 = 59.25
# 中位數成績 = 60.0
# 眾數成績 = 80