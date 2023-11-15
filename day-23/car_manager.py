from turtle import Turtle, Screen
from random import randint
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
color = Screen()
color.colormode(255)
y_position = []
for i in range(-260, 260, 10):
    y_position.append(i)


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.all_cars = []
        self.hideturtle()



    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=1.5, stretch_wid=0.8)
            new_car.penup()
            self.b = randint(1, 255)
            self.g = randint(1, 255)
            self.r = randint(1, 255)
            self.setheading(180)
            new_car.color(self.r, self.g, self.b)
            y_position_number = randint(0, len(y_position) - 1)
            new_car.goto(300, y_position[y_position_number])
            self.all_cars.append(new_car)

    def move(self):
        for i in self.all_cars:
            i.fd(-STARTING_MOVE_DISTANCE)
