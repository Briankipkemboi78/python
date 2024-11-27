from tkinter import *

# ------------------UI SETUP--------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
my_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=my_image)
canvas.grid(row=0, column=0)

window.mainloop()
