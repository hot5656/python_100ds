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

# main()

for i in range(4):
    print("?", end="")
print()

print("?" * 4)