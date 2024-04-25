# class method
# hat.py
import random

class Hat:
    houses = ["Gryffindor", "Hufflenuff", "Ravenclaw", "Slytherin"]

    # class method
    @classmethod
    # cls class 簡寫
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
