
from tkinter import * 
 
# Create window
window = Tk() 
window.title("MPG Calculator") 
 
# Create labels
lbl_gallons = Label(window, text="Number of Gallons:") 
lbl_miles = Label(window, text="Number of Miles:") 
 
# Create entry boxes
txt_gallons = Entry(window) 
txt_miles = Entry(window) 
 
# Create button
btn_calc = Button(window, text="Calculate MPG", command=lambda: calculate_mpg())
 
# Place widgets in window
lbl_gallons.grid(column=0, row=0) 
lbl_miles.grid(column=0, row=1) 
txt_gallons.grid(column=1, row=0) 
txt_miles.grid(column=1, row=1) 
btn_calc.grid(column=1, row=2) 
 
# Calculate MPG
def calculate_mpg(): 
    # Get input
    gallons = float(txt_gallons.get()) 
    miles = float(txt_miles.get()) 
  
    # Calculate MPG
    mpg = miles/gallons 
  
    # Display MPG
    lbl_mpg = Label(window, text="Miles per Gallon: {:.2f}".format(mpg)) 
    lbl_mpg.grid(column=1, row=3) 
  
  
# Run main loop
window.mainloop()