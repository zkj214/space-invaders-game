from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("orange")
        self.penup()
        self.goto(-280, 250)
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"{self.score}", align="left", font=("Arial", 25, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.display_scoreboard()