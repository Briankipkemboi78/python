from tkinter import *

window = Tk()
window.title("My app")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am What I am", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column = 0, row = 0)

#Button
button = Button(text="Click here")
button.grid(column = 1, row = 1)

new_button = Button(text="New Button")
new_button.grid(column = 2, row = 0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column = 3, row = 2)



window.mainloop()