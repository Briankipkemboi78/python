from tkinter import *


def button_clicked():
    print("I got tapped")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My app")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

#Label
my_label = Label(text="I am What I am", font=("Arial", 24, "bold"))
my_label.grid(column = 0, row = 0)

#Button
button = Button(text="Click here", command=button_clicked)
button.grid(column = 1, row = 1)

new_button = Button(text="New Button")
new_button.grid(column = 2, row = 0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column = 3, row = 2)



window.mainloop()