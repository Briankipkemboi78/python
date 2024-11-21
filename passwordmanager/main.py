from tkinter import *




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=('Arial', 14))
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", font=('Arial', 14))
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=('Arial', 14))
password_label.grid(column=0, row=3)








window.mainloop()