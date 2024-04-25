# generators
# sleep.py
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

# 1000000 can not run
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐏" * i)
#     return flock

# generators - yield
def sheep(n):
    for i in range(n):
        yield "🐏" * i

if __name__ == "__main__":
    main()