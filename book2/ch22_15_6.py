import pandas as pd

data = {"color": ["red", "blue", "green", "blue"] }
df = pd.DataFrame(data)
print(df)
#    color
# 0    red
# 1   blue
# 2  green
# 3   blue

# 使用 pandas's get_dummies() 進行 one-hot 編碼
encoded_df = pd.get_dummies(df, columns=['color'])
print(encoded_df)
#    color_blue  color_green  color_red
# 0       False        False       True
# 1        True        False      False
# 2       False         True      False
# 3        True        False      False