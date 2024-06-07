# 產生一年的 sin, cos 值
import pandas as pd
import numpy as np

dates = pd.date_range(start="2023-01-01", end="2023-12-31")
df = pd.DataFrame(data={'date':dates})
df['day_of_year'] = df['date'].dt.day_of_year
df["sin_day_of_year"] = np.sin(2*np.pi*df["day_of_year"]/365)
df["cos_day_of_year"] = np.cos(2*np.pi*df["day_of_year"]/365)
print(df)
#           date  day_of_year  sin_day_of_year  cos_day_of_year
# 0   2023-01-01            1     1.721336e-02         0.999852
# 1   2023-01-02            2     3.442161e-02         0.999407
# 2   2023-01-03            3     5.161967e-02         0.998667
# 3   2023-01-04            4     6.880243e-02         0.997630
# 4   2023-01-05            5     8.596480e-02         0.996298
# ..         ...          ...              ...              ...
# 360 2023-12-27          361    -6.880243e-02         0.997630
# 361 2023-12-28          362    -5.161967e-02         0.998667
# 362 2023-12-29          363    -3.442161e-02         0.999407
# 363 2023-12-30          364    -1.721336e-02         0.999852
# 364 2023-12-31          365     6.432491e-16         1.000000