#-------------------------------------------------------------------
# Written by Carter Stickler, September 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

colorOptions = [
    "black",
    "red",
    "pink",
    "blue",
    "green",
    "yellow",
    "purple"
]

shapeOptions = [
    "classic",
    "triangle",
    "turtle",
    "circle",
    "arrow",
    "square"
]

# speedOptions = [
#     0,
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10
# ]

sizeOptions = [
    1,
    2,
    5,
    8,
    10,
    12,
    15,
    18,
    20
]

def up(data): #Basic controls!
    alex.setheading(90)
    alex.forward(1)

def down(data):
    alex.setheading(-90)
    alex.forward(1)

def left(data):
    alex.setheading(180)
    alex.forward(1)

def right(data):
    alex.setheading(0)
    alex.forward(1)

def changeColor(): #Now the fun buttons. This is what makes the program an Etch-A-Sketch Plus! Change color!
    alex.color(colorClick.get())

def changeShape(): #Change the pen shape!
    alex.shape(turtleClick.get())

def changePenSize():
    alex.pensize(penSizeClick.get())

def turtlePenChange(): #Change the pen state!
    if penState.get() == "Down":
        alex.penup()
        penButton.config(text="Pen Down!")
        penState.set( "Up" )
    else:
        alex.pendown()
        penButton.config(text="Pen Up!")
        penState.set( "Down" )

def turtleStamp():
    alex.stamp()

# def changeSpeed(): #Really tried to get this one working, but since the other buttons work as repeating functions, while the speed DOES change, you can't notice any difference... I tried making the .forward function numbers bigger as well, but nothing really changed there either.
#     alex.speed(speedClick.get())

def resetCanvas():
    alex.reset()
    alex.shape('classic')

root = Tk()

colorClick = StringVar()
turtleClick = StringVar()
penSizeClick = IntVar()
penState = StringVar()
# speedClick = IntVar()

colorClick.set( "black" )
turtleClick.set( "classic" )
penSizeClick.set( 1 )
penState.set( "Down" )
# speedClick.set( 0 )

canvas = ScrolledCanvas(root)
canvas.pack(side=LEFT)
screen = TurtleScreen(canvas)
alex = RawTurtle(canvas)
colorButton = Button(root, text="Change Color!", command=changeColor)
shapeButton = Button(root, text="Change Shape!", command=changeShape)
sizeButton = Button(root, text="Change Size!", command=changePenSize)
penButton = Button(root, text="Pen Up!", command=turtlePenChange)
stampButton = Button(root, text="Stamp!", command=turtleStamp).pack()
# speedButton = Button(root, text="Change Speed!", command=changeSpeed)
resetButton = Button(root, text="Reset the canvas. :(", command=resetCanvas)

colorLabel = Label(root, text="Turtle Color:")
turtleShapeLabel = Label(root, text="Turtle Shape:")
penSizeLabel = Label(root, text="Pen Size:")
penLabel = Label(root, text="Pen Up/Down:")
# speedLabel = Label(root, text="Turtle Speed:")

colorDrop = OptionMenu(root, colorClick, *colorOptions)
shapeDrop = OptionMenu(root, turtleClick, *shapeOptions)
sizeDrop = OptionMenu(root, penSizeClick, *sizeOptions)
# speedDrop = OptionMenu(root, speedClick, *speedOptions)

canvas.bind("<Up>", up)
canvas.bind("<Down>", down)
canvas.bind("<Left>", left)
canvas.bind("<Right>", right)

colorLabel.pack()
colorDrop.pack()
colorButton.pack()
turtleShapeLabel.pack()
shapeDrop.pack()
shapeButton.pack()
penSizeLabel.pack()
sizeDrop.pack()
sizeButton.pack()
penLabel.pack()
penButton.pack()
# speedLabel.pack()
# speedDrop.pack()
# speedButton.pack()
resetButton.pack()
screen.listen()

screen.mainloop()