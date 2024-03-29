from turtle import Turtle
import random


class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/invader.gif")
        self.penup()
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        self.goto(x, y)