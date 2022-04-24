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
easy_categories = ["Tischtennisplatte", "Stromkasten", "Kirche", '"INRI"', "Wandbild", "Radknotenpunkt",
                   "Restaurant/Gaststätte/\nKneipe", "Aussichtspunkt", "Kleingartenverein", "Insektenhotel",
                   "Sportplatz", "Spielplatz", "Baumarktlöwe", '"Historisch"', "Schild eines\nLehrpfads",
                   '"Hier sieht\nman ..."', "Jung & Alt /\nGroß & Klein", "Feuerwehr(-Gedenkstein)",
                   "Haupt- &\nZusatzbild gleich", "Stolperstein", "Generisches Straßenschild", "Sitzbank",
                   "Post-/Briefkasten", "Gefallenendenkmal", "Duplikat", "Wasserpumpe", "Wanderwegweiser",
                   "Bitte Standort x\nnehmen", "Objekt auf\nFriedhof / Friedhof", "Schutzhütte / Hütte",
                   "Nummernschild erkennbar", "Spiegelung des Fotografen", "Herzlich Willkommen-\nSchild",
                   "Skulptur / Statue", "Rechtschreibungs-Edit", "Beschreibung mit\neinem Wort", "Wort in ALL CAPS",
                   "Anführungszeichen\nim Text", "Fahrrad", "Verweis auf\ndie Kriterien", "Baum",
                   "PokéStop-Variation"]
hard_categories = ['"Mural"', '"Anno / Erbaut"', '"Graffiti" falsch\ngeschrieben', 'Wort mit\n12+ Buchstaben',
                   'Alliteration\n(3+ Wörter)', 'Wort in ALL CAPS', 'Ingress-Referenz', 'Link in Zusatzinfo',
                   'Beleidigung in\nZusatzinfo', 'Denglisches Wort', 'Platzhalter-Texte', 'Emoji / Emoticon',
                   'Foto-Edits\n(3+ Bilder)', 'Standort-Edits\n(3+ Standorte)', 'Aktuelles Streetview\n(bis 1 Jahr)',
                   'Foto mit Wasserzeichen', 'Bildschirmfoto/\nScreenshot', 'Geotag im Zusatzbild',
                   'Finger vor\nder Linse', 'Foto aus Auto/\nGebäude', 'Fuß/Schuh\nim Bild', 'Lebendiges Tier\nim Bild',
                   'Gedenkplakette bei\neinem Straßenschild', 'Baum verdeckt Wayspot', 'Sonnenuhr', 'Gullydeckel',
                   'Wegweiser zum Objekt', 'Museum', 'Litfaßsäule', 'Maibaum', 'Casino / Stripclub', 'Grenzstein',
                   'Kaugummi-Automat', 'Objekt im Kreisel', 'Wayspot im Wasser', 'Saisonale Deko']


print(hard_categories)

name = input("Name: ")
number_hard_categories = int(input("Mit wie vielen schwierigen Kategorien möchtest du spielen? (Zahl von 0 - 16) "))
if number_hard_categories < 0 or number_hard_categories > 16:
    number_hard_categories = 0

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
    canvas.create_text(x_position, y_position, justify="center", text=item, font=("Arial", 10, "normal"))
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
