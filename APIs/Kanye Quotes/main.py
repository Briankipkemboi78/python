from tkinter import *
import requests


#Fetching the quote from API
def get_quote():
    response = requests.get("http://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

#-------UI SETUP-----------
window = Tk()
window.title("Kanye Says...")
window.config(pady=50, padx=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here", width=250, font=("Roboto", 16, "bold"), fill="#387478")
canvas.grid(row=0, column=0)

kanye_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()