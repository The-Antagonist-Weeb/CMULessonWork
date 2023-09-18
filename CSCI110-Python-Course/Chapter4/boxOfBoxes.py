import turtle

def matryoshkaBoxes(turtle):
    boxesSize = 20
    turtle.penup() # for centering purposes! 
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.back(20)
    turtle.pendown()
    for i in range(5):
        for x in range(4):
            turtle.forward(boxesSize)
            turtle.right(90)
        turtle.left(90)
        turtle.penup()
        turtle.forward(10)
        turtle.right(90)
        turtle.back(10)
        turtle.pendown()
        boxesSize += 20
    turtle.penup() #For getting the arrow to the same destination as shown in the image.
    turtle.right(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function - Matryoshka Boxes!") # Kinda silly, but these boxes really reminded my of those Matryoshka Dolls for some reason, so I decided to let that be the title.

alex = turtle.Turtle()
alex.color("red")
alex.width(3)
matryoshkaBoxes(alex)
wn.mainloop()