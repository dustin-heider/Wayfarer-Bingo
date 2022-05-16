from random import shuffle, sample
from tkinter import *
from datetime import datetime

FONT_NORMAL = ("Arial", 13, "normal")
FONT_BOLD = ("Arial", 11, "bold")
STANDARD_DIFFICULTY = 4


def row_down():
    global x_position, y_position
    x_position = 135
    y_position += 176


easy_categories = ['"Historisch"', '"INRI"', '"Hier sieht\nman ..."', '"Bitte Standort\nx nehmen"',
                   '"Jung & Alt /\nGroß & Klein"', '"Kein\nPrivatgrundstück"', '"Danke für die\n Bewertung" / "Danke"',
                   '"Lädt zum\nVerweilen ein"',

                   'PokéStop-Variation', '3x gleicher Text', 'Beschreibung mit\neinem Wort', 'Wort mit\n12+ Buchstaben',
                   'Verweis auf\ndie Kriterien', 'Anführungszeichen\nim Text', 'Wayfarer-Referenz',
                   'Referenz zu einem\nNiantic-Spiel',

                   '"Unnötiger" Edit', 'Rechtschreibungs-\nEdit',

                   'Leere\nDuplikatsleiste', 'Duplikat',

                   'Haupt- &\nZusatzbild gleich', 'Schatten auf\ndem Wayspot', 'Schlechte Ausrichtung', 'Rangezoomt',
                   'Nummernschild\nerkennbar', 'Wayspot auf Schul-/\nKindergartengelände',

                   'Stromkasten', 'Aussichtspunkt', 'Sportplatz', 'Vereinsheim', 'Spielplatz', 'Tischtennisplatte',
                   'Feuerwehr/\n(-Gedenkstein)', 'Baumarktlöwe', 'Stolperstein',
                   'Generisches\nStraßenschild', 'Sitzbank', 'Brunnen/\nWasserpumpe',
                   'Gefallenendenkmal', 'Skulptur / Statue', 'Kleingartenverein', 'Insektenhotel',
                   'Naturmerkmal', 'Wanderwegweiser', 'Kirche', 'Schule/Kindergarten', 'Fahrrad im Bild',
                   'Wanderkarte/\nOrtskarte', 'Name des Spielgeräts\nim Titel']

hard_categories = ['"Mural" falsch\nbenutzt', '"Anno / Erbaut"', '"Graffito/Graffiti"\nfalsch geschrieben',
                   'Alliteration\n(3+ Wörter)', 'Wort in ALL CAPS', 'Link in Zusatzinfo', 'Beleidigung in\nZusatzinfo',
                   'Denglisches Wort', 'Platzhalter-Texte', 'Emoji / Emoticon', 'Texte in verschiedenen\nSprachen',

                   'Foto-Edits\n(3+ Bilder)', 'Standort-Edits\n(4+ Standorte)',

                   'Foto mit\nWasserzeichen', 'Bildschirmfoto/\nScreenshot', 'Geotag im Zusatzbild',
                   'Aktuelles Streetview\n(bis 1 Jahr)', 'Finger vor\nder Linse', 'Foto aus Auto/\nGebäude',
                   'Fuß/Schuh\nim Bild', 'Lebendiges\nTier im Bild',

                   'Gedenkplakette bei\neinem Straßenschild', 'Baum verdeckt\nWayspot', 'Sonnenuhr', 'Gullydeckel',
                   'Wegweiser\nzum Objekt', 'Museum', 'Litfaßsäule', 'Maibaum', 'Grenzstein/OD-Stein/\nKilometerstein',
                   'Ort mit 10+\nBuchstaben', 'Kaugummi-/\nZigarettenautomat', 'Objekt im Kreisel', 'Wayspot im Wasser',
                   'Schützenkönig/in-\nScheibe', 'Post-/Briefkasten', 'Spiegelung des\nFotografen',
                   'Spielplatz mit\n4+ Wayspots', 'Fitness-Station', 'Saisonale Deko']

# hard_categories_redacted = ['Collage', 'Casino / Stripclub',]

players_remaining = True
while players_remaining:
    name = input("Name: ")
    if name.title() == "Exit":
        break
    if name == "":
        name = "Standard-Bingo"
    try:
        number_hard_categories = int(input("Mit wie vielen schwierigen Kategorien möchtest du spielen?"
                                           "(Zahl von 0 - 16) "))
    except ValueError:
        print(f"{ValueError}. Die Eingabe enthält keine Zahl!")
    else:
        if number_hard_categories < 0 or number_hard_categories > 16:
            number_hard_categories = STANDARD_DIFFICULTY
            print(f"Standard-Schwierigkeitsgrad ({number_hard_categories} schwierige Kategorien) wurde ausgewählt!")

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
