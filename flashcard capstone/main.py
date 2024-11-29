import random
from tkinter import *
import pandas as pd

#----------------------Reading the data---------
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_file = pd.read_csv('data/french_words.csv')
    to_learn = original_file.to_dict(orient="records")
    current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=my_image)
    flip_timer = window.after(3000, func=flip_card)

#--------------Flip Card --------
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=back_img)

#-------------------IS KNOWN ----------
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/word_to_learn.csv')
    next_card()


# ------------------UI SETUP--------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
my_image = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=my_image)
card_title = canvas.create_text(400, 150, text="", font=("Roboto", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Roboto", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()




window.mainloop()
