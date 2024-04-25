# # meows.py
# def meow(n: int) -> str:
#     # meow n times
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n

# number: int = int(input("Number:"))
# neows: str = meow(number)
# print(neows)

# meows.py
import argparse

# add description for meows.py
parser = argparse.ArgumentParser(description="Meow like a cat")
# add -n's parameter help
# add default value
# auto convert parameter to int
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")

# python .\meows.py -h
#    usage: meows.py [-h] [-n N]
#    Meow like a cat
#    options:
#      -h, --help  show this help message and exit
#      -n N        number of times to meow
