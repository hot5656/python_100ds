# 電影分類
import math

# 玩命關頭
film = [5, 7, 8, 10, 2]
film_titles = [
    "復仇者聯盟",
    "決戰中途島",
    "冰雪奇緣",
    "雙子殺手"
]
film_features = [
    [2, 8, 8, 5, 6],
    [5, 6, 9, 2, 5],
    [8, 2, 0, 0, 10],
    [5, 8, 8, 8, 3]
]

dists =[]
for p in film_features:
    distance = 0
    for i, item in enumerate(p):
        score = int(item) - int(film[i])
        distance += score * score
    dists.append(math.sqrt(distance))
good_point = 0
good_distance = dists[0]
for index, value in enumerate(dists):
    print(f"{film_titles[index]} : {value:.2f}")
    if index > 0 and dists[index] < good_distance:
        good_point = index
        good_distance = dists[index]

print(f"close movie is {film_titles[good_point]} : {dists[good_point]:.2f}")
# 復仇者聯盟 : 7.14
# 決戰中途島 : 8.66
# 冰雪奇緣 : 16.19
# 雙子殺手 : 2.45
# close movie is 雙子殺手 : 2.45