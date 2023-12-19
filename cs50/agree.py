s = input("Do you agree?")

# if s == "Y" or s == "y":
#     print("Agreed.")
# elif s == "N" or s =="n":
#     print("Not agreed.")

print("low:", s.lower)
s = s.lower()
if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["N", "no"]:
    print("Not agreed.")