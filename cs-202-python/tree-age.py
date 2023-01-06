from tkinter import *

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

# Draw the growth rings
canvas.create_oval(25, 25, 275, 275, outline="grey")
canvas.create_oval(50, 50, 250, 250, outline="grey")
canvas.create_oval(75, 75, 225, 225, outline="grey")
canvas.create_oval(100, 100, 200, 200, outline="grey")
canvas.create_oval(125, 125, 175, 175, outline="grey")
canvas.create_oval(150, 150, 150, 150, outline="grey")
canvas.create_oval(175, 175, 125, 125, outline="grey")


# Number the growth rings
canvas.create_text(150, 15, text="5-year-old tree", font="Arial 15 bold")
canvas.create_text(150, 150, text="1", font="Arial 15 bold")
canvas.create_text(125, 125, text="2", font="Arial 15 bold")
canvas.create_text(105, 105, text="3", font="Arial 15 bold")
canvas.create_text(87, 87, text="4", font="Arial 15 bold")
canvas.create_text(71, 71, text="5", font="Arial 15 bold")

root.mainloop()