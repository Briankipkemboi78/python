from tkinter import *
import requests

#-------UI SETUP-----------
window = Tk()
window.title("Kanye Says...")
window.config(pady=50, padx=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here", width=250, font=("Roboto", 25, "bold"), fill="cyan")
canvas.grid(row=0, column=0)

