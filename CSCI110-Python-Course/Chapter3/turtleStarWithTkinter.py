#-------------------------------------------------------------------
# Written by Carter Stickler, September 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

def star(data):

    alex.shape('classic')
    alex.right(110) #For the sake of orientation only

    for i in range(5): #simple for loop
        alex.forward(50)
        alex.left(144)
    alex.left(110)

def turtleClock(data):
    alex.shape('turtle')
    alex.penup()
    # print("why isn't this working") #I was confused why this function wasn't working, but it seems to have been because the second button was set as <Button-2> before. Not sure why that was a problem, but clearly my guess-work there was not accurate. I'll be researching more later to understand that better.
    for i in range(12): #Simple concept, similar to the star program, just more lines really. 
        alex.forward(150)
        alex.pendown()
        alex.forward(10)
        alex.penup()
        alex.forward(20)
        alex.stamp()
        alex.back(180)
        alex.right(30) #since the programs are combined now, I figure it's best to make it easier to invoke both one after the other.
    alex.pendown()

def resetCanvas(data):
    alex.reset()
    alex.shape('classic')

root = Tk()

canvas = ScrolledCanvas(root)
canvas.pack(side=LEFT)
screen = TurtleScreen(canvas)
alex = RawTurtle(canvas)

starButton = Button(text="Draw a star!")
turtleClockButton = Button(text="Draw a turtle clock!")
resetButton = Button(text="Reset the canvas. :(")

starButton.bind("<Button-1>", star)
turtleClockButton.bind("<Button-1>", turtleClock)
resetButton.bind("<Button-1>", resetCanvas)

starButton.pack()
turtleClockButton.pack()
resetButton.pack()
screen.listen()

screen.mainloop()