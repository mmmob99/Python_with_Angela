import turtle
import random
tim = turtle.Turtle()
angles = []
for i in range(3, 11):
    angle = ((i - 2) * 180)/i
    angles.append(angle)
for i in angles:
    a = 1
    b = angles.index(i) + 4
    while b >= a:
        tim.color()
        tim.forward(50)
        tim.right(180 - i)
        a += 1
    if b == 11:
        break
