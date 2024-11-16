from tkinter import *

def calculate():
    miles = float(miles_input.get())  # Get the miles value from the input
    kilometers = round(miles * 1.60934, 2)  # Convert to kilometers (rounded to 2 decimals)
    km_result_label.config(text=f"{kilometers}")  # Update the result label

# Create the main window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Label for static text "Is equal to:"
text_label = Label(text="Is equal to:", font=('Arial', 14))
text_label.grid(column=0, row=1)

# Input for miles
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label for "Miles"
miles_label = Label(text="Miles", font=('Arial', 14))
miles_label.grid(column=2, row=0)

# Label for kilometers result
km_result_label = Label(text="0", font=('Arial', 14))
km_result_label.grid(column=1, row=1)

# Label for "Km"
km_label = Label(text="Km", font=('Arial', 14))
km_label.grid(column=2, row=1)

# Button to trigger calculation
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

# Start the event loop
window.mainloop()
