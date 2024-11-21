from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=('Arial', 14))
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", font=('Arial', 14))
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=('Arial', 14))
password_label.grid(column=0, row=3)

#Input
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

#-----Email/Username-
website_entry = Entry(width=35)
website_entry.grid(column=1, row=2, columnspan=2)

#----Password-
website_entry = Entry(width=21)
website_entry.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate Password", font=('Arial', 15, 'bold'))
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=('Arial', 15, 'bold'))
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
