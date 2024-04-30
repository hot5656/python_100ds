# 非同步模組 - concurrent.futures
from concurrent.futures import ThreadPoolExecutor

time = 1
def show(fruits):
    global time
    index = time
    time += 1
    for fruit in fruits:
        print(f"({index} {fruit})")

# (1 西瓜)
# (1 百香果)
# (2 西瓜)
# (1 香蕉)
# (1 橘子)
# (3 西瓜)
# (1 蘋果)
# (3 百香果)
# (3 香蕉)
# (3 橘子)
# (3 蘋果)
# (2 百香果)
# (2 香蕉)
# (2 橘子)
# (2 蘋果)

fruits = ('西瓜', '百香果', '香蕉', '橘子', '蘋果')
with ThreadPoolExecutor() as executor:
    executor.submit(show, fruits)
    executor.submit(show, fruits)
    executor.submit(show, fruits)

def show1(fruit):
    print(fruit)
print('-- executor.map --')
with ThreadPoolExecutor(max_workers=4) as executor:
    result = executor.map(show1, fruits)

# 西瓜
# 百香果
# 香蕉
# 橘子
# 蘋果