from turtle import Turtle


class Scoreborad(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def incrase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 20, "normal"))

