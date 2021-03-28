from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        # x_random = random.randint(-280, 280)
        # y_random = random.randint(-280, 280)
        x_random = random.randint(-13, 13) * 20
        y_random = random.randint(-13, 13) * 20
        self.goto(x_random, y_random)