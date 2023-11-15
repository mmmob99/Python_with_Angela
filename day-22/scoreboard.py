from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="left", font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="left", font=("Arial", 50, "normal"))

    def l_scorer(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_scorer(self):
        self.r_score += 1
        self.update_scoreboard()
