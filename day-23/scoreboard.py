from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.goto(-250, 250)
        self.score = 0
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.hideturtle()


    def restart(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 50, "normal"))





