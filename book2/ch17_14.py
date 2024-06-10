import numpy as np
import statistics as st
x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]

print(f"Numpy 母體標準差     : {np.std(x):.2f}")
print(f"Numpy 樣本標準差     : {np.std(x, ddof=1):.2f}")
print(f"Statistics 母體標準差: {st.pstdev(x):.2f}")
print(f"Statistics 樣本標準差: {st.stdev(x):.2f}")
# Numpy 母體標準差     : 28.70
# Numpy 樣本標準差     : 30.25
# Statistics 母體標準差: 28.70
# Statistics 樣本標準差: 30.25
