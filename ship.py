from turtle import Turtle


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/player.gif")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)
        self.playerspeed = 15