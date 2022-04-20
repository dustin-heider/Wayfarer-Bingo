from random import choice, randint, shuffle, sample
from pandas import *
from math import sqrt
from turtle import Turtle, Screen

data = read_csv("data/Bingo_Kategorien.CSV").dropna()
easy_categories = data["Einfache Kategorien"].tolist()
hard_categories = data["Schwere Kategorien"].tolist()

print(easy_categories)
print(hard_categories)

easy = sample(easy_categories, 13)
hard = sample(hard_categories, 3)

category_list = easy + hard
shuffle(category_list)
print(category_list)


screen = Screen()
#screen.screensize(canvwidth=500, canvheight=400)

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.pensize()
tim.speed("fastest")
tim.setheading(135)
tim.forward(350)
tim.setheading(0)
count = 0

for item in range(len(category_list)):

    tim.write(category_list[item], align="center", font=("Arial", 11, "normal"))
    tim.forward(175)
    count += 1
    if count % 4 == 0:
        tim.setheading(270)
        tim.forward(100)
        tim.setheading(180)
        tim.forward(700)
        tim.setheading(0)


screen.exitonclick()

#number_categories = int(input("How many categories do you want to have? "))
#rows_and_columns = sqrt(number_categories)
#number_hard_categories = rows_and_columns - 1

