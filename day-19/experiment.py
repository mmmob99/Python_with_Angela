import turtle

tim = turtle.Turtle()

screen = turtle.Screen()


def move():
    tim.forward(100)

screen.listen()
screen.onkey(key="space", fun=move)
screen.exitonclick()
