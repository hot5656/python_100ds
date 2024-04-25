# format.py
# re capture
import re

name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + ' ' + matches.group(1)
print(f"hello, {name}")

# python .\format.py
#  What's your name? Robert Kao
#  hello, Robert Kao
# python .\format.py
#  What's your name? Kao,Robert
#  hello, Robert Kao
