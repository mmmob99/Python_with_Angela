from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = -200


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.setheading(90)



    def set_position(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        self.fd(MOVE_DISTANCE)
