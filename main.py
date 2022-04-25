from random import shuffle, sample
from pandas import *
from tkinter import *
from datetime import datetime
import pyperclip

FONT_NORMAL = ("Arial", 11, "normal")
FONT_BOLD = ("Arial", 11, "bold")


def row_down():
    global x_position, y_position
    x_position = 135
    y_position += 176


# data = read_csv("data/Bingo_Kategorien.CSV", encoding="ISO-8859-1").dropna()
easy_categories = ['"Historisch"', '"INRI"', '"Hier sieht\nman ..."', '"Bitte Standort\nx nehmen"',
                   '"Jung & Alt /\nGroß & Klein"', '"Kein\nPrivatgrundstück"', 'PokéStop-Variation', '3x gleicher Text',
                   'Beschreibung mit\neinem Wort', 'Verweis auf\ndie Kriterien', 'Anführungszeichen\nim Text',
                   '"Unnötiger" Edit', 'Rechtschreibungs-\nEdit', 'Leere\nDuplikatsleiste', 'Duplikat',
                   'Haupt- &\nZusatzbild gleich', 'Spiegelung des\nFotografen', 'Schlechte Ausrichtung', 'Rangezoomt',
                   'Nummernschild\nerkennbar', 'Stromkasten', 'Aussichtspunkt', 'Sportplatz', 'Vereinsheim',
                   'Spielplatz', 'Tischtennisplatte', 'Feuerwehr/\n(-Gedenkstein)', 'Baumarktlöwe', 'Stolperstein',
                   'Generisches\nStraßenschild', 'Sitzbank', 'Post-/Briefkasten',
                   'Gefallenendenkmal', 'Skulptur / Statue', 'Kleingartenverein', 'Wanderwegweiser']

hard_categories = ['"Mural"', '"Anno / Erbaut"', '"Graffiti" falsch\ngeschrieben', 'Wort mit\n12+ Buchstaben',
                   'Alliteration\n(3+ Wörter)', 'Wort in ALL CAPS', 'Ingress-Referenz', 'Link in Zusatzinfo',
                   'Beleidigung in\nZusatzinfo', 'Denglisches Wort', 'Platzhalter-Texte', 'Emoji / Emoticon',
                   'Foto-Edits\n(3+ Bilder)', 'Standort-Edits\n(3+ Standorte)', 'Aktuelles Streetview\n(bis 1 Jahr)',
                   'Foto mit\nWasserzeichen', 'Bildschirmfoto/\nScreenshot', 'Geotag im Zusatzbild',
                   'Finger vor\nder Linse', 'Foto aus Auto/\nGebäude', 'Fuß/Schuh\nim Bild', 'Lebendiges Tier\nim Bild',
                   'Gedenkplakette bei\neinem Straßenschild', 'Baum verdeckt\nWayspot', 'Sonnenuhr', 'Gullydeckel',
                   'Wegweiser\nzum Objekt', 'Museum', 'Litfaßsäule', 'Maibaum', 'Casino / Stripclub', 'Grenzstein',
                   'Kaugummi-Automat', 'Objekt im Kreisel', 'Wayspot im Wasser', 'Saisonale Deko']


name = input("Name: ")
number_hard_categories = int(input("Mit wie vielen schwierigen Kategorien möchtest du spielen? (Zahl von 0 - 16) "))
if number_hard_categories < 0 or number_hard_categories > 16:
    number_hard_categories = 0

number_easy_categories = 16 - number_hard_categories
easy_category_list = sample(easy_categories, number_easy_categories)
hard_category_list = sample(hard_categories, number_hard_categories)
category_list = easy_category_list + hard_category_list
shuffle(category_list)
# category_string = "\n".join(category_list)
# pyperclip.copy(category_string)

window = Tk()
window.title("Wayfarer D/A/CH Bingo")
canvas = Canvas(height=881, width=836, background="white")
template = PhotoImage(file="./data/Bingo 4x4_Feld.png")
canvas.create_image(418, 440.5, image=template)
canvas.pack()

x_position = 135
y_position = 233
count = 0
datum = datetime.today().strftime('%d.%m.%y')
for item in category_list:
    canvas.create_text(x_position, y_position, justify="center", text=item, font=FONT_NORMAL)
    x_position += 187
    count += 1
    if count % 4 == 0:
        row_down()

canvas.create_text(697, 78, text="Regeln:\n"
                                  "1 Punkt pro Feld\n"
                                  "3 Punkte pro Reihe (Bingo)", justify="center", font=FONT_BOLD)
canvas.create_text(135, 68, text=f"Datum: {datum}", justify="center", font=FONT_BOLD)
canvas.create_text(135, 88, text=f"Name: {name}", justify="center", font=FONT_BOLD)

window.mainloop()
