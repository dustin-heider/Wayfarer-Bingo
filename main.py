from random import shuffle, sample
from tkinter import *
from datetime import datetime

FONT_NORMAL = ("Arial", 13, "normal")
FONT_BOLD = ("Arial", 11, "bold")
STANDARD_DIFFICULTY = 5                 # change if too hard/easy


# one row down if 4 categories are in one row
def row_down():
    global x_position, y_position
    x_position = 135
    y_position += 176


# add/delete categories in these two lists
easy_categories = ['"Historisch"', '"INRI"', '"Hier sieht\nman ..."', '"Bitte Standort\nx nehmen"',
                   '"Jung & Alt/\nGroß & Klein"', '"Kein\nPrivatgrundstück"', '"Danke für die\n Bewertung"/"Danke"',
                   '"Lädt zum\nVerweilen ein"',

                   'PokéStop-Variation', '3x gleicher Text', 'Beschreibung mit\neinem Wort', 'Wort mit\n12+ Buchstaben',
                   'Verweis auf\ndie Kriterien', 'Anführungszeichen\nim Text', 'Wayfarer-Referenz',
                   'Referenz zu einem\nNiantic-Spiel',

                   '"Unnötiger" Edit', 'Rechtschreibungs-\nEdit',

                   'Leere\nDuplikatsleiste', 'Duplikat',

                   'Haupt- &\nZusatzbild gleich', 'Schatten auf\ndem Wayspot', 'Schlechte Ausrichtung', 'Rangezoomt',
                   'Nummernschild\nerkennbar', 'Wayspot auf Schul-/\nKindergartengelände', 'Nutzloses\nUmgebungsfoto',

                   'Stromkasten', 'Aussichtspunkt', 'Sportplatz', 'Vereinsheim', 'Spielplatz', 'Tischtennisplatte',
                   'Feuerwehr/\n(-Gedenkstein)', 'Baumarktlöwe', 'Stolperstein',
                   'Generisches\nStraßenschild', 'Sitzbank', 'Brunnen/\nWasserpumpe',
                   'Gefallenendenkmal', 'Skulptur/Statue', 'Kleingartenverein', 'Insektenhotel',
                   'Naturmerkmal', 'Wanderwegweiser', 'Radwegweiser', 'Kirche', 'Schule/Kindergarten',
                   'Fahrrad im Bild', 'Wanderkarte/\nOrtskarte', 'Name des Spielgeräts\nim Titel', 'Willkommensschild',
                   'Objekt auf Friedhof/\nFriedhof', 'Wandbild/Garagenbild', 'Geschäft/Bäcker/\nSupermarkt',
                   'Restaurant/Kneipe/\nGaststätte', 'Schild eines\nLehrpfads', 'Schutzhütte/Hütte']

hard_categories = ['"Mural"', '"Anno/Erbaut"', '"Graffito/Graffiti"\nfalsch geschrieben', '"Erfüllt alle\nKriterien"',
                   'Alliteration\n(3+ Wörter)', 'Wort in ALL CAPS', 'Link in Zusatzinfo',
                   '(Passiv-) aggressive\nZusatzinfo', 'Platzhalter-Texte', 'Emoji/Emoticon',
                   'Texte in verschiedenen\nSprachen',

                   'Standort-Edits\n(4+ Standorte)', 'Foto-Edits\n(3+ Bilder)', 'Spielplatz mit\n2+ Wayspots',
                   'Aktuelles Streetview\n(bis 1 Jahr)', 'Ort mit 10+\nBuchstaben',

                   'Spiegelung des\nFotografen', 'Foto mit\nWasserzeichen', 'Geotag im Zusatzbild',
                   'Foto aus Auto/\nGebäude', 'Bildschirmfoto/\nScreenshot', 'Finger vor\nder Linse',
                   'Fuß/Schuh\nim Bild', 'Lebendiges\nTier im Bild',

                   'Baum verdeckt\nWayspot', 'Wayspot im Wasser', 'Objekt im Kreisel', 'Wegweiser\nzum Objekt',
                   'Gedenkplakette bei\neinem Straßenschild',  'Sonnenuhr', 'Gullydeckel', 'Museum', 'Litfaßsäule',
                   'Maibaum', 'Grenzstein/OD-Stein/\nKilometerstein', 'Kaugummi-/\nZigarettenautomat',
                   'Schützenkönig/in-\nScheibe', 'Post-/Briefkasten', 'Fitness-Station', 'Saisonale Deko']

# hard_categories_redacted = ['Collage', 'Casino / Stripclub',]

# use inputs to create Tkinter window with categories, screenshot window to save image
# possibility of Ghostscript to save a file without using screenshot?
players_remaining = True
while players_remaining:
    name = input("Name: ")
    if name.title() == "Exit":
        break
    if name == "":
        name = "Standard-Bingo"

    number_hard_categories = input("Mit wie vielen schwierigen Kategorien möchtest du spielen?"
                                    "(Zahl von 0 - 16): ")
    if len(number_hard_categories) == 0:
        number_hard_categories = STANDARD_DIFFICULTY
    elif not number_hard_categories.isdigit():
        break

    number_hard_categories = int(number_hard_categories)
    if number_hard_categories < 0 or number_hard_categories > 16:
        break
    number_easy_categories = 16 - number_hard_categories
    easy_category_list = sample(easy_categories, number_easy_categories)
    hard_category_list = sample(hard_categories, number_hard_categories)
    category_list = easy_category_list + hard_category_list
    shuffle(category_list)

    window = Tk()
    window.title("Wayfarer D/A/CH Bingo")
    canvas = Canvas(height=881, width=836, background="white")
    template = PhotoImage(file="./data/Bingo 4x4_new.png")
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

    canvas.create_text(135, 94, text="Regeln:\n"
                                     "1 Punkt pro Feld\n"
                                     "3 Punkte pro Reihe (Bingo)", justify="center", font=FONT_BOLD)
    canvas.create_text(697, 94, text=f"Datum: {datum}\n"
                                     f"Name: {name}\n"
                                     f"Schwierige Kategorien: {number_hard_categories}", justify="center",
                                     font=FONT_BOLD)

    window.mainloop()
