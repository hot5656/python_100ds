import numpy as np

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits, 3)
print(f"隨意選3種 : {fruit1}")

fruit2 = np.random.choice(fruits, 5)
print(f"隨意選5種(可重複) : {fruit2}")

fruit3 = np.random.choice(fruits, 5, replace=False)
print(f"隨意選5種(不可重複) : {fruit3}")

fruit4 = np.random.choice(fruits, 5, p =[0.8, 0.05, 0.05, 0.05, 0.05])
print(f"依權重選5種(可重複) : {fruit4}")

fruit5 = np.random.choice(fruits, 5, p =[0.05, 0.05, 0.05, 0.05, 0.8])
print(f"依權重選5種(可重複) : {fruit5}")

# 隨意選3種 : ['Mango' 'Grapes' 'Orange']
# 隨意選5種(可重複) : ['Apple' 'Grapes' 'Grapes' 'Orange' 'Grapes']
# 隨意選5種(不可重複) : ['Banana' 'Mango' 'Apple' 'Orange' 'Grapes']
# 依權重選5種(可重複) : ['Grapes' 'Apple' 'Apple' 'Banana' 'Apple']
# 依權重選5種(可重複) : ['Apple' 'Mango' 'Mango' 'Mango' 'Apple']
