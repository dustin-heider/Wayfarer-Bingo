from random import shuffle, sample
from tkinter import *
from PIL import ImageGrab
from datetime import datetime

STANDARD_DIFFICULTY = 5                 # number of difficult categories, change if too hard/easy
FONT_NORMAL = ("Arial", 12, "bold")     # appearance of normal text
FONT_BOLD = ("Arial", 12, "bold")       # appearance of bold text
WIDTH = 2                               # width of Bingo-grid
BASE_LINE_X = 25
END_LINE_X = 725
INCREMENT_X = 175
BASE_LINE_Y = 120
END_LINE_Y = 675
INCREMENT_Y = 138.75

x_position = 0
y_position = 0

datum = datetime.today().strftime('%d.%m.%Y')       # date in widget
datum_v2 = datetime.today().strftime('%Y-%m-%d')    # date for filename


# create the Bingo field
def create_bingo_field():
    canvas.create_rectangle(BASE_LINE_X, BASE_LINE_Y, END_LINE_X, END_LINE_Y,
                            outline=color_field,
                            width=WIDTH)
    for x_line_counter in range(1, 4):
        canvas.create_line(
            BASE_LINE_X + INCREMENT_X * x_line_counter,
            BASE_LINE_Y,
            BASE_LINE_X + INCREMENT_X * x_line_counter,
            END_LINE_Y,
            fill=color_field,
            width=WIDTH)
    for y_line_counter in range(1, 4):
        canvas.create_line(
            BASE_LINE_X,
            BASE_LINE_Y + INCREMENT_Y * y_line_counter,
            END_LINE_X,
            BASE_LINE_Y + INCREMENT_Y * y_line_counter,
            fill=color_field,
            width=WIDTH)


#  writes the texts above the Bingo-field
def create_texts():
    canvas.create_text(135, 60,
                       text="Regeln:\n"
                            "1 Punkt pro Feld\n"
                            "3 Punkte pro Reihe (Bingo)",
                       justify="center",
                       font=FONT_BOLD,
                       fill=color_text)
    canvas.create_text(375, 60,
                       text="Niantic Wayfarer\n"
                            "D / A / C H\n"
                            "Bingo",
                       justify="center",
                       font=("Arial", 18, "bold"),
                       fill=color_text)
    canvas.create_text(615, 60,
                       text=f"Datum: {datum}\n"
                            f"Name: {name}\n"
                            f"Schwierige Kategorien: {number_difficult_categories}",
                       justify="center",
                       font=FONT_BOLD,
                       fill=color_text)


# writes the Bingo categories on the canvas
def write_categories():
    global x_position, y_position
    count = 0
    x_position = 114
    y_position = 189
    for item in category_list:
        canvas.create_text(x_position, y_position, justify="center", text=item, font=FONT_NORMAL, fill=color_text)
        x_position += 174.5
        count += 1
        if count % 4 == 0:
            row_down()


# one row down if 4 categories are in one row
def row_down():
    global x_position, y_position
    x_position = 113
    y_position += 140


# saves a png file of the tkinter-window with date andd (individual) name
def save_as_png():
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    x1 = x + window.winfo_width()
    y1 = y + window.winfo_height()
    ImageGrab.grab(bbox=(x, y, x1, y1)).save(f'Bingo_{datum_v2}_{name}.png')


# add/delete categories in these two lists
easy_categories = [
    '"Historisch"', '"INRI"', '"Hier sieht\nman ..."', '"Bitte Standort\nx nehmen"', '"Jung & Alt/\nGroß & Klein"',
    '"Kein\nPrivatgrundstück"', '"Danke für die\n Bewertung"/"Danke"', '"Lädt zum\nVerweilen ein"',

    'PokéStop-Variation', '3x gleicher Text', 'Beschreibung mit\neinem Wort', 'Wort mit\n12+ Buchstaben',
    'Verweis auf\ndie Kriterien', 'Anführungszeichen\nim Text', 'Wayfarer-Referenz',
    'Referenz zu einem\nNiantic-Spiel',

    '"Unnötiger" Edit', 'Rechtschreibungs-\nEdit',

    'Leere\nDuplikatsleiste', 'Duplikat',

    'Haupt- &\nZusatzbild gleich', 'Schatten auf\ndem Wayspot', 'Schlechte\nAusrichtung', 'Rangezoomt',
    'Nummernschild\nerkennbar', 'Wayspot auf Schul-/\nKindergartengelände', 'Nutzloses\nUmgebungsbild',

    'Stromkasten', 'Aussichtspunkt', 'Sportplatz', 'Vereinsheim', 'Spielplatz', 'Tischtennisplatte',
    'Feuerwehr/\n(-Gedenkstein)', 'Baumarktlöwe', 'Stolperstein', 'Generisches\nStraßenschild', 'Sitzbank',
    'Brunnen/\nWasserpumpe', 'Gefallenendenkmal', 'Skulptur/Statue', 'Kleingartenverein', 'Insektenhotel',
    'Naturmerkmal', 'Wanderwegweiser', 'Radwegweiser', 'Kirche', 'Schule/\nKindergarten', 'Fahrrad im Bild',
    'Wanderkarte/\nOrtskarte', 'Name des Spiel-\ngeräts im Titel', 'Willkommensschild',
    'Objekt auf Friedhof/\nFriedhof', 'Wandbild/\nGaragenbild', 'Geschäft/\nBäcker/\nSupermarkt',
    'Restaurant/\nKneipe/\nGaststätte', 'Schild eines\nLehrpfads', 'Schutzhütte/Hütte',
]

hard_categories = [
    '"Mural"', '"Anno/Erbaut"', '"Graffito/Graffiti"\nfalsch geschrieben', '"Erfüllt alle\nKriterien"', '"POI"',
    'Alliteration\n(3+ Wörter)', 'Wort in ALL CAPS', 'Link in Zusatzinfo', '(Passiv-) aggressive\nZusatzinfo',
    'Platzhalter-Texte', 'Emoji/Emoticon', 'Texte in\nverschiedenen\nSprachen',

    'Standort-Edits\n(4+ Standorte)', 'Foto-Edits\n(3+ Bilder)', 'Spielplatz mit\n2+ Wayspots',
    'Aktuelles Streetview\n(bis 1 Jahr)', 'Nutzloses Streetview', 'Ort mit 10+\nBuchstaben',

    'Spiegelung des\nFotografen', 'Foto mit\nWasserzeichen', 'Geotag im\nZusatzbild', 'Foto aus Auto/\nGebäude',
    'Bildschirmfoto/\nScreenshot', 'Finger vor\nder Linse', 'Fuß/Schuh\nim Bild', 'Lebendiges\nTier im Bild',

    'Baum verdeckt\nWayspot', 'Wayspot im Wasser', 'Objekt im Kreisel', 'Wegweiser\nzum Objekt',
    'Gedenkplakette bei\neinem Straßenschild',  'Sonnenuhr', 'Gullydeckel', 'Museum', 'Litfaßsäule', 'Maibaum',
    'Hydrant', 'Grenzstein/\nOD-Stein/\nKilometerstein', 'Kaugummi-/\nZigarettenautomat', 'Schützenkönig/in-\nScheibe',
    'Post-/Briefkasten', 'Fitness-Station', 'Saisonale Deko',
]


# use inputs to create standard/individual Bingo-sheet with certain difficulty
players_remaining = True
while players_remaining:
    color_field = "orangered"  # color of Bingo-grid
    color_background = "white"
    color_text = "black"

    name = input("Name: ")
    if name.lower() == "exit":
        break
    elif name == "":
        name = "Standard-Bingo"

    number_difficult_categories = input("Mit wie vielen schwierigen Kategorien möchtest du spielen? "
                                        "(Zahl von 0 - 16): ")
    if len(number_difficult_categories) == 0:
        number_difficult_categories = STANDARD_DIFFICULTY
    elif not number_difficult_categories.isdigit():
        break

    number_difficult_categories = int(number_difficult_categories)
    if number_difficult_categories < 0 or number_difficult_categories > 16:
        break

    # shuffle the list of categories
    number_easy_categories = 16 - number_difficult_categories
    easy_category_list = sample(easy_categories, number_easy_categories)
    difficult_category_list = sample(hard_categories, number_difficult_categories)
    category_list = easy_category_list + difficult_category_list
    shuffle(category_list)

    # creates window and canvas
    window = Tk()
    window.geometry('750x700+100+100')      # size of window, location of window at the screen
    window.title("Wayfarer Bingo")
    window.resizable(False, False)          # NOT resizable
    window.lift()
    window.attributes('-topmost', True)     # window pops up at the screen in front of everything else
    window.after_idle(window.attributes, '-topmost', False)
    
    canvas = Canvas(window, height=700, width=750, background=color_background, highlightthickness=0)
    canvas.pack()

    # call functions
    create_texts()
    create_bingo_field()
    write_categories()
    # window.update()
    window.after(1000, save_as_png)         # takes screenshot one second to make sure the canvas is finished

    window.mainloop()
