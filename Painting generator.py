from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import *
from random import randrange
from random import *
window = Tk()
canvas = Canvas(width=800, height=500)
canvas.pack()
window.title("Painting generator")
def pickColor():
    color1 = askcolor()
    color2 = askcolor()
    color3 = askcolor()
    color4 = askcolor()

def generate(input1):
    for x in range(0, input1):
        x1 = choice(range(1, 800))
        y1 = choice(range(1, 500))
        x2 = x1 + choice(range(1, 800))
        y2 = y1 + choice(range(1, 500))
        canvas.create_rectangle(x1, y1 ,x2, y2, fill=str(color1[-1]))

        x1 = choice(range(1, 800))
        y1 = choice(range(1, 500))
        x2 = x1 + choice(range(1, 800))
        y2 = y1 + choice(range(1, 500))
        canvas.create_rectangle(x1, y1 ,x2, y2, fill=str(color2[-1]))
        x1 = choice(range(1, 800))
        y1 = choice(range(1, 500))
        x2 = x1 + choice(range(1, 800))
        y2 = y1 + choice(range(1, 500))
        canvas.create_rectangle(x1, y1 ,x2, y2, fill=str(color3[-1]))
        x1 = choice(range(1, 800))
        y1 = choice(range(1, 500))
        x2 = x1 + choice(range(1, 800))
        y2 = y1 + choice(range(1, 500))
        canvas.create_rectangle(x1, y1 ,x2, y2, fill=str(color4[-1]))
        
print("Welcome to painting generator! Press ENTER to continue...")
input()
rectangle = int(input("Enter the number of rectangles: "))
print("Select color")
color1 = askcolor()
color2 = askcolor()
color3 = askcolor()
color4 = askcolor()
print("Generating... Please wait.")
generate(rectangle)
print("Done. Close window to exit.")
window.mainloop()