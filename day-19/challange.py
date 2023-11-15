import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
screen.listen()


def move_upward():
    tim.fd(10)


def clockwise():
    tim.right(10)

def counter_clockwise():
    tim.left(10)

def back_wards():
    tim.backward(10)
screen.onkey(fun=move_upward, key="w")
screen.onkey(fun=back_wards, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=screen.resetscreen, key="c")
screen.exitonclick()
