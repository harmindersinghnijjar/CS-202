from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=400)

# Create the sky
sky = canvas.create_rectangle(0, 0, 400, 400, fill="light blue")

# Create the sun
sun = canvas.create_oval(200, 0, 300, 100, fill="yellow")

# Create the house
house = canvas.create_rectangle(100, 200, 300, 400, fill="gray")

# Create the windows
window1 = canvas.create_rectangle(120, 220, 180, 280, fill="white")
window2 = canvas.create_rectangle(220, 220, 280, 280, fill="white")

# Create the door
door = canvas.create_rectangle(160, 320, 240, 400, fill="brown")

# Create the clouds
cloud1 = canvas.create_oval(20, 20, 80, 80, fill="white")
cloud2 = canvas.create_oval(110, 40, 180, 100, fill="white")
cloud3 = canvas.create_oval(250, 20, 320, 80, fill="white")

canvas.pack()

root.mainloop()