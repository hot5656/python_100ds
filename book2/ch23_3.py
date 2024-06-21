import pandas as pd

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", ep='\s+')
# item0 to item12 data
data = boston.iloc[:, :13]
# item13 data
target = boston.iloc[:,13:14]

# 列出資料外型
print(f"資料外型        : {boston.shape}")
print(f"自變數  樣品外型 : {data.shape}")
print(f"目標變數樣品外型 : {target.shape}")

# 列出3筆 自變數(特徵值)
print(data.head(3))
# 列出3筆 目標變數(房價)
print(target.head(3))

# 特徵值名稱
print(f"{data.columns}")
print(f"{target.columns}")