from turtle import Turtle


class Lasers(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(0.15, 1)
        self.hideturtle()
        self.bulletspeed = 30
        self.bulletstate = "ready"