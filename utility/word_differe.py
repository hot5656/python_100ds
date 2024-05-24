# words different with base.txt
# base.txt : 篩選文字比較檔
# words.txt : 單字編輯後(用做比較)
# org_words : 單字編輯前檔案
# f"diff_{org_words}" : 預計加入篩選文字比較檔
# 考慮 單字編輯後 一般單字會轉成開頭小寫, 若大寫篩選文字手動輸入
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

words_file = "words.txt"
base_set = set()
if os.path.exists(words_file):
    with open(words_file, "r") as file:
        for line in file:
            base_set.add(line.strip())
    # print(base_set)
else:
    print(f"no file {words_file}")
    exit(1)

words_set = set()
while True:
    org_words = input("compare words file: ")
    name_files = org_words.split(".")
    # check file exist
    if len(name_files[0]) != 0:
        if os.path.exists(org_words):
            # read file
            with open(org_words, "r") as file:
                for line in file:
                    if line.strip() not in base_set:
                        # 若為小寫開頭才寫入(大寫保護不自動寫入)
                        # print(f"{line[0].islower()} {line.strip()}")
                        if (line[0].islower()):
                            # 為以放入 base.txt
                            if line.strip() not in base_set:
                                words_set.add(line.strip())
                    # else:
                    #     print(f"word: {line}")

            words_file_name = f"diff_{name_files[0]}.txt"
            # write text file
            with open(words_file_name, "w") as file:
                for item in words_set:
                    file.write(item + "\n")
        else:
            print(f"not found file {org_words}")
    else:
        exit(0)