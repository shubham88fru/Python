from tkinter import *

def miles_to_km(miles):
    miles = miles_input.get()
    km = float(miles)*1.609
    kilometers_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers converter")
window.config(padx=50, pady=50)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(row=1, column=0)

kilometers_result_label = Label(text="0")
kilometers_result_label.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()