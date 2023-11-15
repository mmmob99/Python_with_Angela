import turtle
import random
tim = turtle.Turtle()
color_list = [(232, 144, 77), (246, 220, 82), (230, 64, 101), (8, 175, 214), (163, 51, 104), (235, 79, 59), (91, 186, 211), (4, 131, 169), (230, 124, 153), (156, 76, 48), (143, 211, 221), (121, 191, 159), (50, 168, 104), (4, 153, 97), (177, 147, 53), (237, 161, 181), (149, 25, 80), (21, 90, 72), (26, 56, 86), (21, 60, 120), (170, 202, 196), (3, 107, 114), (76, 67, 45), (242, 171, 156), (73, 18, 75), (69, 48, 20)]
a = 0
turtle.colormode(255)
current_positiony = 0
tim.hideturtle()
while a < len(color_list):
    for i in range(5):
        color_number = random.choice(color_list)
        tim.color(color_number)
        tim.dot(20)
        tim.penup()
        tim.fd(40)
        a += 1
    current_positiony += 40
    tim.setposition(0, current_positiony)

screen = turtle.Screen()
screen.exitonclick()

