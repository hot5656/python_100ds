import pandas as pd

# 讀取數據
df = pd.read_csv('nasa.csv')

# 刪除資料
df = df.drop(['Name', 'Neo Reference ID', 'Est Dia in M(min)',
              'Est Dia in M(max)', 'Est Dia in Miles(min)',
              'Est Dia in Miles(max)', 'Est Dia in Feet(min)',
              'Est Dia in Feet(max)', 'Epoch Date Close Approach',
              'Relative Velocity km per hr', 'Miles per hour',
              'Miss Dist.(Astronomical)', 'Miss Dist.(lunar)',
              'Miss Dist.(miles)', 'Equinox'],
             axis=1)

# 將 'Hazardous' True/False 轉為 1/0
df['Hazardous'] = df['Hazardous'].map({True:1, False:0})

# 將 'Close Approach Date' 和 'Orbit Determination Date'
# 轉為日期時間物件,再轉為時間戳記
# test format
# df['Close Approach Date'] = pd.to_datetime(df['Close Approach Date'])
# df['Orbit Determination Date'] = pd.to_datetime(df['Orbit Determination Date'])
df['Close Approach Date'] = pd.to_datetime(df['Close Approach Date']).astype('int64') // 10**9
df['Orbit Determination Date'] = pd.to_datetime(df['Orbit Determination Date']).astype('int64') // 10**9

# 列出5筆
print(df.head)

# <bound method NDFrame.head of       Absolute Magnitude  Est Dia in KM(min)  Est Dia in KM(max)  Close Approach Date  Relative Velocity km per sec  Miss Dist.(kilometers)  ... Perihelion Arg  Aphelion Dist  Perihelion Time  Mean Anomaly  Mean Motion  Hazardous
# 0                 21.600            0.127220            0.284472            788918400                      6.115834            6.275369e+07  ...      57.257470       2.005764     2.458162e+06    264.837533     0.590551          1
# 1                 21.300            0.146068            0.326618            788918400                     18.113985            5.729815e+07  ...     313.091975       1.497352     2.457795e+06    173.741112     0.845330          0
# 2                 20.300            0.231502            0.517654            789523200                      7.590711            7.622912e+06  ...     248.415038       1.966857     2.458120e+06    292.893654     0.559371          1
# 3                 27.400            0.008801            0.019681            790128000                     11.173874            4.268362e+07  ...      18.707701       1.527904     2.457902e+06     68.741007     0.700277          0
# 4                 21.600            0.127220            0.284472            790128000                      9.840831            6.101082e+07  ...     158.263596       1.483543     2.457814e+06    135.142133     0.726395          1
# ...                  ...                 ...                 ...                  ...                           ...                     ...  ...            ...            ...              ...           ...          ...        ...
# 4682              23.900            0.044112            0.098637           1473292800                     22.154265            6.187511e+06  ...     276.395697       1.581299     2.457708e+06    304.306025     0.787436          0
# 4683              28.200            0.006089            0.013616           1473292800                      3.225150            9.677324e+05  ...      42.111064       1.153835     2.458088e+06    282.978786     0.884117          0
# 4684              22.700            0.076658            0.171412           1473292800                      7.191642            9.126775e+06  ...     274.692712       2.090708     2.458300e+06    203.501147     0.521698          0
# 4685              21.800            0.116026            0.259442           1473292800                     11.352090            3.900908e+07  ...     180.346090       1.787733     2.458288e+06    203.524965     0.543767          0
# 4686              19.109            0.400641            0.895860           1473292800                     35.946852            6.916986e+07  ...     222.436688       2.071980     2.458319e+06    184.820424     0.550729          0