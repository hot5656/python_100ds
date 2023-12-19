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