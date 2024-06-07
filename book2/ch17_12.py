import numpy as np
import statistics as st
x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]

print(f"Numpy 母體變異數     : {np.var(x):6.2f}")
print(f"Numpy 樣本變異數     : {np.var(x, ddof=1):6.2f}")
print(f"Statistics 母體變異數: {st.pvariance(x):6.2f}")
print(f"Statistics 樣本變異數: {st.variance(x):6.2f}")
# Numpy 母體變異數     : 823.49
# Numpy 樣本變異數     : 914.99
# Statistics 母體變異數: 823.49
# Statistics 樣本變異數: 914.99
