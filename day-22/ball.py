from turtle import Turtle
import time
from turtle import Screen
from paddle import Paddle




class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(1, 1)
        self.y = 10
        self.x = 10

    def move(self, r_paddle, l_paddle):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        time.sleep(0.05)
        if y >= 285:
            self.y = -10
        if self.distance(r_paddle) < 40:
            self.x = -10


        elif self.distance(l_paddle) < 40:
            self.x = 10
        elif y <= -285:
            self.y = 10
        self.goto(x, y)
