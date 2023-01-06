
# import tkinter module 
from tkinter import *

# Create a window
window = Tk() 
window.title("Celsius to Fahrenheit Converter")

# Create a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    # Get the value from the input field
    celsius = float(celsius_value.get())
    # Calculate Fahrenheit value
    fahrenheit = (9/5*celsius + 32)
    # Put the result in the output field
    fahrenheit_value.set(fahrenheit)

# Create a Label and an Entry field
celsius_value = DoubleVar()
celsius_label = Label(window, text="Celsius Temperature")
celsius_entry = Entry(window, textvariable=celsius_value)

# Create a button
convert_button = Button(window, text="Convert", command=celsius_to_fahrenheit)

# Create another Label and Entry field
fahrenheit_value = DoubleVar()
fahrenheit_label = Label(window, text="Fahrenheit Temperature")
fahrenheit_entry = Entry(window, textvariable=fahrenheit_value)

# Place the widgets onto the window
celsius_label.grid(row=0, column=0, sticky=W)
celsius_entry.grid(row=0, column=1, sticky=W)
convert_button.grid(row=0, column=2, sticky=W)
fahrenheit_label.grid(row=1, column=0, sticky=W)
fahrenheit_entry.grid(row=1, column=1, sticky=W)

# Create an event loop
window.mainloop()