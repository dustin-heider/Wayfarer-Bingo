from random import shuffle, sample
from tkinter import *
from PIL import ImageGrab
from datetime import datetime

STANDARD_DIFFICULTY = 2  # number of difficult categories, change if too hard/easy
FONT_NORMAL = ("Arial", 13, "normal")  # appearance of normal text
FONT_BOLD = ("Arial", 12, "bold")  # appearance of bold text
COLOR = "orangered"  # color of Bingo-grid
WIDTH = 2  # width of Bingo-grid
BASE_LINE_X = 25
END_LINE_X = 725
INCREMENT_X = 175
BASE_LINE_Y = 120
END_LINE_Y = 675
INCREMENT_Y = 138.75
x_position = 0
y_position = 0
datum = datetime.today().strftime('%d.%m.%Y')  # date in widget
datum_v2 = datetime.today().strftime('%d-%m-%Y')  # date for filename


# create the Bingo field
def create_bingo_field():
    canvas.create_rectangle(BASE_LINE_X, BASE_LINE_Y, END_LINE_X, END_LINE_Y,
                            outline=COLOR,
                            width=WIDTH)
    for x_line_counter in range(1, 4):
        canvas.create_line(
            BASE_LINE_X + INCREMENT_X * x_line_counter,
            BASE_LINE_Y,
            BASE_LINE_X + INCREMENT_X * x_line_counter,
            END_LINE_Y,
            fill=COLOR,
            width=WIDTH)
    for y_line_counter in range(1, 4):
        canvas.create_line(
            BASE_LINE_X,
            BASE_LINE_Y + INCREMENT_Y * y_line_counter,
            END_LINE_X,
            BASE_LINE_Y + INCREMENT_Y * y_line_counter,
            fill=COLOR,
            width=WIDTH)


#  writes the texts above the Bingo-field
def create_texts():
    canvas.create_text(125, 60,
                       text="rules:\n"
                            "1 point per square\n"
                            "3 points per row (Bingo)",
                       justify="center",
                       font=FONT_BOLD)
    canvas.create_text(375, 60,
                       text="Niantic Wayfarer\n"
                            "Discussion Discord\n"
                            "Bingo",
                       justify="center",
                       font=("Arial", 18, "bold")
                       )
    canvas.create_text(630, 60,
                       text=f"date: {datum}\n"
                            f"name: {name}\n"
                            f"difficult categories: {number_difficult_categories}",
                       justify="center",
                       font=FONT_BOLD)


# writes the Bingo categories on the canvas
def write_categories():
    global x_position, y_position
    count = 0
    x_position = 114
    y_position = 189
    for item in category_list:
        canvas.create_text(x_position, y_position, justify="center", text=item, font=FONT_NORMAL)
        x_position += 174.5
        count += 1
        if count % 4 == 0:
            row_down()


# one row down if 4 categories are in one row
def row_down():
    global x_position, y_position
    x_position = 113
    y_position += 140


# saves a png file of the tkinter-window with date and (individual) name
def save_as_png():
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    x1 = x + window.winfo_width()
    y1 = y + window.winfo_height()
    ImageGrab.grab(bbox=(x, y, x1, y1)).save(f'Bingo_{datum_v2}_{name}.png')


# add/delete categories in these two lists
easy_categories = [
    'same text in\ntitle and description', 'title with\none word', 'title with six\nor more words',
    '"Need more Stops"\nor similar expression', 'reference to a\nNiantic game',
    'text with\nquotation marks',

    'photo of a\nlegible license plate', 'literal garbage\nin the picture', 'live animal\nin the photo',
    'live person\nin photo', 'picture taken\nat night', 'Low quality picture\n(LPQ)', 'photo where the\nsun is visible',
    'primary photo\ncontains graffiti', 'zoomed-in picture', 'useless\nsupporting picture',

    'empty duplicate map', 'duplicate',

    'public transit\nstation/stop',

    'baseball/soccer/\nUS football field', 'basketball/\ntennis/\npickle-ball court', 'bench', 'brewery/\nwinery/\nbar',
    'cemetery/nomination\nin a cemetery', 'fire hydrant/\nfire department', 'water tower/tank/\nswimming pool',
    'fountain',
    'garden/\nflower landscaping', 'gazebo/similar\nshade structure', 'gym/\nexercise equipment', 'historic building',
    'nomination at/of\na K12 school', 'library/\nlittle free library',
    'memorial/donor/\ndedication plaque', 'mural', 'named art piece', 'nature sign',
    'park/park sign', 'place of worship', 'playground',
    'located on PRP', 'sculpture/statue', 'sign for apartment/\nneighborhood/city',
    'trail marker/\ncairn', 'tree/plant or\nmarker for them', 'footbridge', 'restaurant/cafe',
    'place name/\ndirectional sign/\nmap', 'utility box', 'generic street sign',

]

difficult_categories = [
    'Wayfarer-reference', 'Link in\nsupporting information', 'word in ALL CAPS', 'placeholder-texts',
    'emoji/emoticon', 'texts in\ndifferent languages', '"please select\nlocation x"',

    'edit-review with\n3 or more options', 'city with 10\nor more characters',

    'photo with watermark', 'selfie/reflection\nof the submitter', 'Pokémon GO\nAR photo', 'picture with\nsnow/sand',
    'third party photo/\npicture of a screen', 'identical main and\nsupporting picture', 'picture taken\nfrom a car',

    'ornithological (bird)-\nrelated', 'train-related', 'vehicle/\nvehicle-related shop', 'bicycle-related',

    'museum', 'place of worship', 'dock/pier or\nsimilar structure', 'nomination of\na hospital\n(or located at one)',
    'post office/\npost box', 'theater/auditorium', 'campground', 'nomination in an\namusement park',
]

# use inputs to create standard/individual Bingo-sheet with certain difficulty
players_remaining = True
while players_remaining:
    name = input("name: ")
    if name.lower() == "exit":
        break
    if name == "":
        name = "default-bingo"

    number_difficult_categories = input("With how many difficult categories do you want to play? "
                                        "(number from 0 - 16): ")
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
    difficult_category_list = sample(difficult_categories, number_difficult_categories)
    category_list = easy_category_list + difficult_category_list
    shuffle(category_list)

    # creates window and canvas
    window = Tk()
    window.geometry('750x700+100+100')  # size of window, location of window at the screen
    window.title("Wayfarer Bingo")
    window.resizable(False, False)  # NOT resizable
    window.lift()
    window.attributes('-topmost', True)  # window pops up at the screen in front of everything else
    window.after_idle(window.attributes, '-topmost', False)

    canvas = Canvas(window, height=700, width=750, background="white", highlightthickness=0)
    canvas.pack()

    # call functions
    create_texts()
    create_bingo_field()
    write_categories()
    window.update()
    window.after(1000, save_as_png)  # takes screenshot one second to make sure the canvas is finished

    window.mainloop()
