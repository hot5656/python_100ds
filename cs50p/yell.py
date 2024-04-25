# map, list comprehensions
# yell.py
def main():
    yell("This", "is", "CS50")
    yell2("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(type(uppercased))
    print(uppercased)
    print(*uppercased)


# list comprehensions
def yell2(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()


