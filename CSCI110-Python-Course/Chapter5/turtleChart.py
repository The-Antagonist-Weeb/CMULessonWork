#-------------------------------------------------------------------
# Written by Carter Stickler, September 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

def draw_bar(t, height):
    if height >= 200: #almost all of the code here is copied and pasted here from the textbook, and this if statement is my method of solving problem #8.
        t.color("blue", "red")
        t.begin_fill()
    elif height >= 100:
        t.color("blue", "yellow")
        t.begin_fill()
    else:
        t.color("blue", "green")
        t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup() #Just to make it look good while it's building. Though, it will create these lines anyway when I do the "Strike through" sort of on line 44.
    t.forward(10)
    t.pendown()

for v in xs:
    draw_bar(tess, v)
for i in xs:
    tess.back(50)

wn.mainloop()