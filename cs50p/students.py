# students.py
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["name"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# # students.py - csv write
# import csv
# import os

# file_path = "students.csv"

# name = input("What's your name? ")
# home = input("Where's your from? ")

# if not os.path.exists(file_path):
#     with open("students.csv", "a", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['name', 'home'])

# with open("students.csv", "a", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])


# # students.py - csv write
# import csv
# import os

# file_path = "students.csv"

# name = input("What's your name? ")
# home = input("Where's your from? ")

# if not os.path.exists(file_path):
#     with open(file_path, "w", newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=["name", "home"])
#         writer.writeheader()

# with open(file_path, "a", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})


# def main():
#     # name , house = get_student()
#     # print(f"{name} from {house}")
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)

# if __name__ == "__main__":
#     main()


# class Student():
#     def __init__(self, name, house):
#         # 因內部呼叫也會呼叫 .house(), __init__ 所以不用 check
#         # if house not in ["Gryffindor", "Hufflenuff", "Ravenclaw", "Slytherin"]:
#         #     raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @property # _name's getter
#     def name(self):
#         # 因 function house same as variable house所以 variable 改為 _house
#         return self._name

#     @name.setter # _name's setter
#     def name(self,name):
#         # 'not name' same as 'name == ""'
#         if not name:
#             raise ValueError("Missing name")
#         self._name = name

#     @property # _house's getter
#     def house(self):
#         # 因 function house same as variable house所以 variable 改為 _house
#         return self._house

#     @house.setter # _house's setter
#     def house(self,house):
#         if house not in ["Gryffindor", "Hufflenuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         # 因 function house same as variable house所以 variable 改為 _house
#         self._house = house

# def main():
#     student = get_student()
#     # _variable mean private, no modify it(but it can change)
#     # student._house = "Taipei"
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()

# class method - create instance
# students.py
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()