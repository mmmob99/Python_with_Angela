import turtle
from turtle import Turtle
scr = Turtle()
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

guessed_cities = []
while len(guessed_cities) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_cities)}/50 States Correct", prompt="What's another state's name?").title()
    with open("50_states.csv", "r") as data:
        file = pandas.read_csv(data)
        us_cities = file["state"].to_list()
        x = file.x.to_list()
        y = file.y.to_list()
        for i in us_cities:
            if answer_state == i:
                scr.speed("fastest")
                scr.hideturtle()
                scr.penup()
                scr.goto(x[(us_cities.index(i))], y[(us_cities.index(i))])
                scr.write(i)
                guessed_cities.append(i)
screen.exitonclick()
