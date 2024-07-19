# 中位數填補區失值
import pandas as pd

# 讀取糖尿病數據
df = pd.read_csv('diabetes.csv')

# 可能存在缺失特徵
columns_with_potential_missing_values = ['BloodPressure', 'SkinThickness', 'Insulin', 'BMI'
]

# 將0值,替換為中位數
for column in columns_with_potential_missing_values:
    median = df[column].median()
    df[column] = df[column].replace(to_replace=0, value=median )

# 存入新的csv
df.to_csv('new_diabetes.csv', index=False)
