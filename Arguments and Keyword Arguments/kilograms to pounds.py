from tkinter import  *

FONT_1 = ('Arial', 20, "bold")
FONT_2 = ('Arial', 14)

def calculate():
    kg = float(kilograms_input.get())
    pounds = round(kg * 2.205, 2)
    lb_result_label.config(text=f"{pounds}")


window = Tk()
window.title("KG Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label for Static value
text_label = Label(text="Is equal to:", font=FONT_2)
text_label.grid(column=0, row=2)
text_label.config(padx=10, pady=10)

#textarea
kilograms_input = Entry(width=10)
kilograms_input.grid(column=1, row=1)

#Label for pounds converted
lb_result_label = Label(text="0", font=FONT_1)
lb_result_label.grid(column=1, row=2)
lb_result_label.config(padx=10, pady=10)

#Label for lb
lb_label = Label(text="lb", font=FONT_2)
lb_label.grid(column=2, row=2)
lb_label.config(padx=10, pady=10)

#Button to calculate
button = Button(text="calculate", command=calculate)
button.grid(column=1, row=3)
button.config(padx=10, pady=10)


window.mainloop()
