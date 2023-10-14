#-------------------------------------------------------------------
# Written by Carter Stickler, September 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

colorOptions = [ #Dropdown menu options
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

speedOptions = [
    1,
    3,
    5,
    8,
    10,
    15,
    20,
    30,
    40,
    50,
    60
]

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
    canvas.unbind("<Up>") #These unbinds are my fix for the maximum recursion depth. Overall it stablizes the program, and doesn't affect the user experience negatively at all. Simply disabling the keypresses until the function finishes. It turns out that I was having that issue since it was calling the function while in the middle of the function, so I disable all key presses when one is pressed, and this stabilizes the application, and overall experience as some of the one off weird lines stopped happening. 
    canvas.unbind("<Down>")
    canvas.unbind("<Left>")
    canvas.unbind("<Right>")
    alex.setheading(90)
    alex.forward(speedClick.get())
    canvas.bind("<Up>", up)
    canvas.bind("<Down>", down)
    canvas.bind("<Left>", left)
    canvas.bind("<Right>", right)
def down(data):
    canvas.unbind("<Up>")
    canvas.unbind("<Down>")
    canvas.unbind("<Left>")
    canvas.unbind("<Right>")
    alex.setheading(-90)
    alex.forward(speedClick.get())
    canvas.bind("<Up>", up)
    canvas.bind("<Down>", down)
    canvas.bind("<Left>", left)
    canvas.bind("<Right>", right)
def left(data):
    canvas.unbind("<Up>")
    canvas.unbind("<Down>")
    canvas.unbind("<Left>")
    canvas.unbind("<Right>")
    alex.setheading(180)
    alex.forward(speedClick.get())
    canvas.bind("<Up>", up)
    canvas.bind("<Down>", down)
    canvas.bind("<Left>", left)
    canvas.bind("<Right>", right)

def right(data):
    canvas.unbind("<Up>")
    canvas.unbind("<Down>")
    canvas.unbind("<Left>")
    canvas.unbind("<Right>")
    alex.setheading(0)
    alex.forward(speedClick.get())
    canvas.bind("<Up>", up)
    canvas.bind("<Down>", down)
    canvas.bind("<Left>", left)
    canvas.bind("<Right>", right)

def changeColor(): #Now the fun buttons. This is what makes the program an Etch-A-Sketch Plus! Change color!
    alex.color(colorClick.get())

def fillColor(): #Fill in color!
    alex.color(colorClick.get(), colorFillClick.get())

    if fillState.get() == "False":
        colorFillButton.config(text="Stop Color Fill!")
        alex.begin_fill()
        fillState.set( "True" )
    else:
        colorFillButton.config(text="Start Color Fill!")
        alex.end_fill()
        fillState.set( "False" )


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

def turtleStamp(): #Make a stamp!
    alex.stamp()

def changeSpeed(): #Changes the Turtle's Speed! ###Really tried to get this one working, but since the other buttons work as repeating functions, while the speed DOES change, you can't notice any difference... I tried making the .forward function numbers bigger as well, but nothing really changed there either.
    alex.speed(speedClick.get()) #Ignore the above note. With fixing the recursion depth issue, this started to function correctly, so I reintegrated.

def resetCanvas(): #Reset your work.
    alex.reset()
    alex.shape('classic')

root = Tk() #Tkinter main UI settings
root.geometry("1900x1900")
root.attributes('-fullscreen', True)
root.title("Etch-A-Sketch-Plus!")

colorClick = StringVar() #Variables for functions/buttons
colorFillClick = StringVar()
turtleClick = StringVar()
penSizeClick = IntVar()
penState = StringVar()
fillState = StringVar()
speedClick = IntVar()

colorClick.set( "black" ) #Setting initial variables
colorFillClick.set( "green" )
turtleClick.set( "classic" )
penSizeClick.set( 1 )
penState.set( "Down" )
fillState.set( "False" )
speedClick.set( 1 )

canvas = ScrolledCanvas(root, width=2300, height=1900) #Canvas creation/settings for Tkinter
canvas.pack(side=LEFT)

screen = TurtleScreen(canvas) #Turtles initialization
alex = RawTurtle(canvas) 

colorButton = Button(root, text="Change Color!", command=changeColor) #UI buttons
colorFillButton = Button(root, text="Start Color Fill!", command=fillColor)
shapeButton = Button(root, text="Change Shape!", command=changeShape)
sizeButton = Button(root, text="Change Size!", command=changePenSize)
penButton = Button(root, text="Pen Up!", command=turtlePenChange)
stampButton = Button(root, text="Stamp!", command=turtleStamp).pack()
speedButton = Button(root, text="Change Speed!", command=changeSpeed)
resetButton = Button(root, text="Reset the canvas. :(", command=resetCanvas)

colorLabel = Label(root, text="Turtle Color:") #UI Labels - I wanted to add some spacing here, but it would require some restructuring of my UI page in general, and I decided to just go with what I had since it's not necessary for the project.
colorFillLabel = Label(root, text="Fill Color:")
turtleShapeLabel = Label(root, text="Turtle Shape:")
penSizeLabel = Label(root, text="Pen Size:")
penLabel = Label(root, text="Pen Up/Down:")
speedLabel = Label(root, text="Turtle Speed:")

colorDrop = OptionMenu(root, colorClick, *colorOptions) #Dropdown menus for buttons
colorFillDrop = OptionMenu(root, colorFillClick, *colorOptions)
shapeDrop = OptionMenu(root, turtleClick, *shapeOptions)
sizeDrop = OptionMenu(root, penSizeClick, *sizeOptions)
speedDrop = OptionMenu(root, speedClick, *speedOptions)

canvas.bind("<Up>", up) #Key press bindings for arrow keys
canvas.bind("<Down>", down)
canvas.bind("<Left>", left)
canvas.bind("<Right>", right)

colorLabel.pack() #Packing all the UI elements
colorDrop.pack()
colorButton.pack()
colorFillLabel.pack()
colorFillDrop.pack()
colorFillButton.pack()
turtleShapeLabel.pack()
shapeDrop.pack()
shapeButton.pack()
penSizeLabel.pack()
sizeDrop.pack()
sizeButton.pack()
penLabel.pack()
penButton.pack()
speedLabel.pack()
speedDrop.pack()
speedButton.pack()
resetButton.pack()

screen.listen()
screen.mainloop()