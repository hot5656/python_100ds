# name = input("What's your name? ")

# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffidor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")


# name = input("What's your name? ")

# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffidor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

# students = {
#     "Harry":"Gryffidor",
#     "Hermione":"Gryffidor",
#     "Ron":"Gryffidor",
#     "Draco":  "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep=", ")

# students = {
#     "Harry": "Gryffidor",
#     "Hermione": "Gryffidor",
#     "Ron": "Gryffidor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")

# set() : 儲存不重複
# houses.py
students = [
    {"name": "Harry", "house": "Gryffidor"},
    {"name": "Hermione", "house": "Gryffidor"},
    {"name": "Ron", "house": "Gryffidor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
