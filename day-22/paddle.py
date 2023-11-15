from turtle import Turtle

WIDHT = 5
HEIGHT = 1
R_X_POS = 350
R_Y_POS = 0
L_X_POS = -350
L_Y_POS = 0


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=WIDHT, stretch_len=HEIGHT)
        self.penup()


    def set_position(self, X, Y):
        self.setposition(X, Y)
        self.y_current_position = self.ycor()
        self.x_current_position = self.xcor()

    def move_up(self):
        self.y_current_position += 20
        self.goto(self.x_current_position, self.y_current_position)

    def move_down(self):
        self.y_current_position -= 20
        self.goto(self.x_current_position, self.y_current_position)
