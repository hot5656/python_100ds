# 直方圖(值的統計) - 概率密度計算
import matplotlib.pyplot as plt
import numpy as np

data = [0.90513322, 0.15810074, 0.32891869, 0.03708101, 0.27432692, 0.32718963,
        0.76349748, 0.67982328, 0.37927703, 0.23771415, 0.85356478, 0.85289975,
        0.88362553, 0.76916029, 0.34394394, 0.7994356, 0.46121558, 0.60705721,
        0.50982303, 0.38045841, 0.40422827, 0.29620067, 0.12077285, 0.41938933,
        0.83631546, 0.03351526, 0.2107422, 0.34037895, 0.68802419, 0.34909733,
        0.69598211, 0.02954847, 0.73337498, 0.58560771, 0.0880778, 0.25110801,
        0.29567434, 0.23931488, 0.74423415, 0.53426499, 0.63710205, 0.85050719,
        0.0219141, 0.13598411, 0.22482733, 0.34913734, 0.54646223, 0.59545045,
        0.79510712, 0.68748215, 0.99978247, 0.26372471, 0.57559782, 0.02730514,
        0.97328489, 0.25601602, 0.7447136, 0.53107671, 0.81301182, 0.01345121,
        0.55230886, 0.5942061, 0.53807666, 0.75641069, 0.89824032, 0.98566657,
        0.48525277, 0.83114744, 0.17032085, 0.59162258, 0.78336821, 0.82423893,
        0.31521662, 0.72591383, 0.45586739, 0.28447144, 0.64501956, 0.77192904,
        0.34181779, 0.96989949, 0.47152398, 0.04595838, 0.28884804, 0.30506038,
        0.07965552, 0.13688494, 0.49999705, 0.66975644, 0.16643227, 0.08857587,
        0.31085938, 0.50804045, 0.35961718, 0.53703562, 0.96675887, 0.1208318,
        0.84330491, 0.85891426, 0.49863786, 0.16626874]

# 計算直方圖
hist, bins = np.histogram(data, bins=10, density=True)

# 計算每个 bin 的概率密度
bin_widths = np.diff(bins)
probability_densities = hist / np.sum(hist * bin_widths)

print("Bin edges:", bins)
print("Probability densities:", probability_densities)
plt.hist(data, bins=10, density=True)
plt.show()