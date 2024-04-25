# # say.py

# import sys
# from sayings import hello

# if len(sys.argv) == 2:
#     hello(sys.argv[1])

# say.py
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()

# python say.py
#     What's this? This is cs50
#     ____________
#     | This is cs50 |
#     ============
#                 \
#                 \
#                 ^__^
#                 (oo)\_______
#                 (__)\       )\/\
#                     ||----w |
#                     ||     ||
