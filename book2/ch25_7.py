import pandas as pd

# 建立 DataFrame
df = pd.DataFrame({
    '性別':['男','男','女','男','女','女','女','男','男','女'],
    '喜好':['籃球','足球','籃球','足球','籃球','足球','籃球','籃球','棒球','棒球']
})

# 創建交叉分析表
cross_tbl = pd.crosstab(df['性別'], df['喜好'])
print(cross_tbl)

# 喜好  棒球  籃球  足球
# 性別
# 女       1     3     1
# 男       1     2     2
