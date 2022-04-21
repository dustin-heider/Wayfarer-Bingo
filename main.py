from random import shuffle, sample
from pandas import *
from tkinter import *
from datetime import datetime
import pyperclip


def row_down():
    global x_position, y_position
    x_position = 174
    y_position += 90


data = read_csv("data/Bingo_Kategorien.CSV", encoding="ISO-8859-1").dropna()
easy_categories = data["Einfache Kategorien"].tolist()
hard_categories = data["Schwierige Kategorien"].tolist()

name = input("Name: ")
number_hard_categories = int(input("Mit wie vielen schwierigen Kategorien möchtest du spielen? (Zahl von 0 - 16) "))

number_easy_categories = 16 - number_hard_categories
easy_category_list = sample(easy_categories, number_easy_categories)
hard_category_list = sample(hard_categories, number_hard_categories)
category_list = easy_category_list + hard_category_list
shuffle(category_list)
category_string = "\n".join(category_list)
pyperclip.copy(category_string)

window = Tk()
window.title("Wayfarer D/A/CH Bingo")
canvas = Canvas(height=600, width=900)
template = PhotoImage(file="./data/Bingo 4x4.png")
canvas.create_image(450, 300, image=template)
canvas.pack()

x_position = 174
y_position = 210
count = 0
datum = datetime.today().strftime('%d.%m.%y')
for item in category_list:
    canvas.create_text(x_position, y_position, text=item, font=("Arial", 10, "normal"))
    x_position += 184
    count += 1
    if count % 4 == 0:
        row_down()

canvas.create_text(178, 115, text="Regeln:\n"
                                  "1 Punkt pro Feld\n"
                                  "3 Punkte pro Reihe (Bingo)", justify="center", font=("Arial", 10, "bold"))
canvas.create_text(720, 105, text=f"Name: {name}", justify="center", font=("Arial", 10, "bold"))
canvas.create_text(720, 125, text=f"Datum: {datum}", justify="center", font=("Arial", 10, "bold"))

window.mainloop()
