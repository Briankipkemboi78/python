from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREENISH = "#243642"
GREEN = "#9bdeac"
SAGE = "#629584"
TEAL = "#387478"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Work Effectively")
window.config(padx=100, pady=50, bg=GREENISH)


canvas = Canvas(width=200, height=224, bg=GREENISH, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 28))
canvas.grid(column=1, row=1)

# Label
text_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), bg=GREENISH, fg=TEAL)
text_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", bg=SAGE, fg=TEAL)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=SAGE, fg=TEAL)
reset_button.grid(column=2, row=2)







window.mainloop()
