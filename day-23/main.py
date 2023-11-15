import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
player = Player()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.up, "Up")
scoreboard = Scoreboard()
car = CarManager()
number = 0.1
game_is_on = True
while game_is_on:
    time.sleep(number)
    car.create_car()
    car.move()
    if player.ycor() > 280:
        scoreboard.restart()
        player.set_position()
        number *= 0.8
    for i in car.all_cars:
        if player.distance(i) < 20:
            scoreboard.game_over()
            screen.update()
            game_is_on = False

    screen.update()
screen.exitonclick()
