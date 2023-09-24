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
    alex.right(108) #For the sake of orientation only

    for i in range(5): #simple for loop
        alex.forward(50)
        alex.left(144)
    alex.left(108)

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

def drawSquareOfSquares(data):
    alex.shape('classic')
    alex.color("red")
    # boxesSize = boxOfBoxesSize.get(1.0, "end-1c") # This was working, but ultimately, the logic would get pretty complicated, so I decided to cut it out to save time.
    numOfBoxes = boxesNum.get(1.0, "end-1c")

    if numOfBoxes == '':
        numOfBoxes = 5
    else:
        numOfBoxes = int(numOfBoxes)

    boxesSize = 20
    alex.penup()
    alex.left(90)
    alex.forward(10)
    alex.right(90)
    alex.back(10)
    alex.pendown()
    for i in range(numOfBoxes):
        for x in range(4):
            alex.forward(boxesSize)
            alex.right(90)
        alex.left(90)
        alex.penup()
        alex.forward(5)
        alex.right(90)
        alex.back(5)
        alex.pendown()
        boxesSize += 10
    alex.penup()
    alex.forward(5 * numOfBoxes)
    alex.forward(10)
    alex.right(90)
    alex.forward(5 * numOfBoxes)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
    alex.color("black")

def createChart(data):
    chartValuesRaw = chartValues.get(1.0, "end-1c")
    chartValuesSplit = chartValuesRaw.split(",")

    for i in chartValuesSplit:
        if int(i) >= 200: #I wanted to add a input for choosing the color the bar fills here, but it would take more time than I want to spend on this one.
            alex.color("blue", "red")
            alex.begin_fill()
        elif int(i) >= 100:
            alex.color("blue", "yellow")
            alex.begin_fill()
        else:
            alex.color("blue", "green")
            alex.begin_fill()
        alex.left(90)
        alex.forward(int(i))
        alex.write("  "+ str(int(i)))
        alex.right(90)
        alex.forward(40)
        alex.right(90)
        alex.forward(int(i))
        alex.left(90)
        alex.end_fill()
        alex.penup()
        alex.forward(10)
        alex.pendown()
    for x in chartValuesSplit:
        alex.backward(50)
    alex.color("black")


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
boxesButton = Button(text="Draw the Matryoshka Boxes!")
# boxesLabel = Label(text="Boxes Size:")
# boxOfBoxesSize = Text(height = 1, width = 10)
numOfBoxesLabel = Label(text="Number of Boxes:")
boxesNum = Text(height = 1, width = 10)
chartButton = Button(text="Draw a chart with custom values!")
chartValuesLabel = Label(text="""Values for the chart (separated by ","):""")
chartValues = Text(height = 1, width = 10)
chartColorLabels = Label(text="Values >= 200 will be red\nValues >= 100 && < 200 will be yellow\nValues < 100 will be green")
resetButton = Button(text="Reset the canvas. :(")

starButton.bind("<Button-1>", star)
turtleClockButton.bind("<Button-1>", turtleClock)
boxesButton.bind("<Button-1>", drawSquareOfSquares)
chartButton.bind("<Button-1>", createChart)
resetButton.bind("<Button-1>", resetCanvas)

starButton.pack()
turtleClockButton.pack()
boxesButton.pack()
# boxesLabel.pack()
# boxOfBoxesSize.pack()
numOfBoxesLabel.pack()
boxesNum.pack()
chartButton.pack()
chartValuesLabel.pack()
chartValues.pack()
chartColorLabels.pack()
resetButton.pack()
screen.listen()

screen.mainloop()