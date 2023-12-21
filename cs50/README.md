## python
``` bash
# install cs50
pip3 install cs50
# install pyttsx3
pip install pyttsx3
# upgrade pip
python.exe -m pip install --upgrade pip
```

``` py
# print
answer = get_string("What's your name?")
print(f"hello, {answer}")

#x: 1
#y: 3
#0.33333333333333331482961625624739099293947219848633
z = x / y
print(f"{z:.50f}")

# main()
def main():
    for i in range(3):
        meow()
def meow():
    print("meow")
main()

# try
def main():
    height = get_height()
    for i in range(height):
        print("#")
# def get_height():
#     while True:
#         try :
#             n = int(input("Height: "))
#             if n > 0:
#                 return n
#         except ValueError:
#             print("Not an integer")
def get_height():
    while True:
        try :
            n = int(input("Height: "))
        except ValueError:
            print("Not an integer")
        else:
            if n > 0:
                return n
main()

# same line
for i in range(4):
    print("?", end="")
print()
# same line
print("?" * 4)

# list
scores = [72, 73, 33]
average = sum(scores) / len(scores)
print(f"Average: {average}")
# list - 2
from cs50 import get_int
# scores = list() - same
scores = []
for i in range(3):
    score = get_int("Score: ")
    # scores.append(score)
    scores += [score]
average = sum(scores) / len(scores)
print(f"Average: {average}")
# list -3
for arg in argv[0:1]:

# sys module
from sys import argv
if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")
from sys import argv
# sys module - 2
for i in range(len(argv)):
    print(argv[i])
# ----------------
for arg in argv:
    print(arg)
# sys module - 3
import sys
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
print(f"hello, {sys.argv[1]}")
sys.exit(0)

# dict
# people = dict() -- same -- people ={}
people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}
name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")
# for pie, price in pizzas.items():
#     print("A whole {} pizza costs ${}".format(price))

# swap
x = 1
y =2
print(f"x is {x}, y is {y}")
x, y = y, x
print(f"x is {x}, y is {y}")

# talk
import pyttsx3
engine = pyttsx3.init()
name = input("Name: ")
engine.say(f"hello, {name}")
engine.runAndWait()

# qr code
import os
import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran")
img.save("qr.png", "PNG")
# windows not support
# os.system("open qr.png")

# CSV
import csv
# file = open("phonebook.csv", "a")
# name = input("Name: ")
# number = input("number: ")
# writer = csv.writer(file)
# writer.writerow([name, number])
# file.close()
with open("phonebook.csv", "a") as file:
    name = input("Name: ")
    number = input("number: ")
    # writer = csv.writer(file)
    # writer.writerow([name, number])
    writer = csv.DictWriter(file, filenames=["name", "number"])
    writer.writerow({"name": name, "number": number})
#with open("phonebook.csv") as file:
#    file_reader = csv.DictReader(file)
#    for book in file_reader:
#        print(book)
#

# tuple - constent
# list of tuples
presidents = [
    ("George Washington", 1789,),
    ("John Adams", 1797,),
    ("Thomas Jefferson", 1801,),
]

for prez, year in presidents:
        print("In {1}, {0} took office".format(prez, year))

# run main
if __name__ == "__main__"
    main()

# boject
class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))

jane = Student("Jane", 10)
jane.print()
jane.changeID(11)
jane.print()

# direct run - linux (also need set file can execute)
#!/usr/bin/env pythone

# lambda 使用於僅使用一次 function
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
#
# for favorite in counts:
# for favorite in sorted(counts, reverse=True):
# get_value 無 () 表不馬上執行
# for favorite in sorted(counts, key=get_value, reverse=True):
# lambda 使用於僅使用一次 function
for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
    print(f"{favorite}: {counts[favorite]}")
```

``` py
from cs50 import SQL
db = SQL("sqlite:///favorites.db")
favorite = input("Favorite: ")
rows = db.execute("SELECT (*) FROM favorites WHERE problem = 'Mario'")
for row in rows:
    print(row["Timestamp"])

from cs50 import SQL
db = SQL("sqlite:///favorites.db")
favorite = input("Favorite: ")
#rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = 'Mario'")
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)
row = rows[0]
print(row["n"])

# race
db.execute("BEGIN TRANSACTION")
rows = db.execute("SELECT likes FROM posts WHERE id = ?", id)
likes = roes[0]["likes]
db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id)
db.execute("COMMIT)

# inject
# -- ignore right
# rows = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
# rows = db.execute(f"SELECT * FROM users WHERE username = 'mmalan@harvad.edu'--' AND password = '{password}'")
rows = db.execute("SELECT * FROM users WHERE username = ? AND password = ?", username, password )
if row:
    ...
```
