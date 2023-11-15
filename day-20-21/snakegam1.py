from turtle import Screen, distance
import time
from snake import Snake
from food import Food
from scoreboard import Scoreborad

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
segments = []
snake = Snake()
food = Food()
score = Scoreborad()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.incrase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score.game_over()

    for i in snake.segments:
        if i != snake.segments[0]:

            if snake.head.distance(i) < 10:
                game_is_on = False
                score.game_over()
screen.exitonclick()
