import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# def get_value(language):
#     return counts[language]

# for favorite in counts:
# for favorite in sorted(counts, reverse=True):
# get_value 無 () 表不馬上執行
# for favorite in sorted(counts, key=get_value, reverse=True):
# lambda 使用於僅使用一次 function
for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
    print(f"{favorite}: {counts[favorite]}")
