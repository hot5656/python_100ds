import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

unit_price =90
x = [x for x in range(1,11)]
y = [y * unit_price for y in x]
plt.plot(x,y, "-*")
plt.title('玉荷包 重量 vs 價格', fontsize=20)
plt.xlabel('重量', fontsize=14)
plt.ylabel('價格', fontsize=14)

plt.show()