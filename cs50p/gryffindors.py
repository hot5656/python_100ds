# # filter
# # gryffindors.py
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# def is_gryffindor(s):
#     # print(s, s["house"], s["house"] == "Gryffindor")
#     return s["house"] == "Gryffindor"

# # gryffindors = filter(is_gryffindor, students)
# # for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
# #     print(gryffindor["name"])

# # gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
# # for gryffindor in sorted(gryffindors):
# #     print(gryffindor)

# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

# Harry
# Hermione
# Ron

# # dictionary comprehensions
# # gryffindors.py
# students = ["Hermione", "Harry", "Ron"]
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
# print(gryffindors)
# # [{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]

# students = ["Hermione", "Harry", "Ron"]
# gryffindors = {student: "Gryffindor" for student in students}
# print(gryffindors)
# # {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}

# enumerate
# gryffindors.py
students = ["Hermione", "Harry", "Ron"]
for i, student in enumerate(students):
    print(i + 1, student)
