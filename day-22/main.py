from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.tracer(0)

screen.bgcolor("black")
r_paddle = Paddle()
l_paddle = Paddle()
r_paddle.set_position(350, 0)
l_paddle.set_position(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.title("Pong")

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:

    ball.move(r_paddle, l_paddle)
    screen.update()
    if ball.xcor() > 380:
        ball.goto(0, 0)
        scoreboard.l_scorer()
    elif ball.xcor() < -380:
        ball.goto(0, 0)
        scoreboard.r_scorer()

screen.exitonclick()
