import turtle
import random
tim = turtle.Turtle()
colors = ["maroon", "red", "black", "navy", "yellow", "powder blue", "indigo", "dark magenta", "crimson", "pale violet red"]
numbers = [90, 180]
while True:
    tim.pensize(10)
    tim.forward(20)
    number = random.choice(colors)
    tim.color(number)
    z = random.randint(1, 60)
    a = random.choice(numbers)
    if z % 2 == 0:
        tim.right(a)
    else:
        tim.left(a)
