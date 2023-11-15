from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.data = open("data.txt", "r")
        high_score = int(self.data.read())
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        print(self.high_score)

    def update_scoreboard(self):
        self.clear()

        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            data2 = open("data.txt", "w")
            data2.write(str(self.score))
            data2.close()
            self.data.close()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1

        self.update_scoreboard()
