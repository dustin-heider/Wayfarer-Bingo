from random import shuffle, sample
from pandas import *
from tkinter import *
from PIL import ImageGrab


def row_down():
    global x_position, y_position
    x_position = 174
    y_position += 90


x_position = 174
y_position = 210
count = 0

data = read_csv("data/Bingo_Kategorien.CSV").dropna()
easy_categories = data["Einfache Kategorien"].tolist()
hard_categories = data["Schwere Kategorien"].tolist()

easy = sample(easy_categories, 13)
hard = sample(hard_categories, 3)
category_list = easy + hard
shuffle(category_list)
print(category_list)

window = Tk()
window.title("Wayfarer D/A/CH Bingo")
canvas = Canvas(height=600, width=900)
template = PhotoImage(file="./data/Bingo 4x4.png")
canvas.create_image(450, 300, image=template)

for item in category_list:
    text = canvas.create_text(x_position, y_position, text=item, font=("Arial", 10, "normal"))
    x_position += 184
    count += 1
    if count % 4 == 0:
        row_down()

canvas.pack()

window.mainloop()
