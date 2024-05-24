# aricle transfer to word list
# base.txt : 篩選文字比較檔
# article : 準備處理文件
# f"words_{article}" : 取出單字檔案

import os

# read base file for don't care
base_file = "base.ttt"
base_set = set()
if os.path.exists(base_file):
    with open(base_file, "r") as file:
        for line in file:
            base_set.add(line.strip())
else:
    print(f"no file {base_file}")
    exit(1)

# set() support 加入資料唯一
words_set = set()
while True:
    article = input("transfer article : ")
    name_files = article.split(".")
    # check file exist
    if len(name_files[0]) != 0:
        if os.path.exists(article):
            # read file
            with open(article, "r") as file:
                for line in file:
                    words = line.split(" ")
                    for word in words:
                        words_set.add(word.strip())
            # sort set() to list
            words_sort = sorted(words_set)

            words_file_name = f"words_{name_files[0]}.txt"
            # write text file
            with open(words_file_name, "w") as file:
                for item in words_sort:
                    # check if in base file, not write
                    if item.strip() not in base_set:
                        file.write(item + "\n")
        else:
            print(f"not found file {article}")
    else:
        exit(0)