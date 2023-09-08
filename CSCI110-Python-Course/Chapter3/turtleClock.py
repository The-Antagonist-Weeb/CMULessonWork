#-------------------------------------------------------------------
# Written by Carter Stickler, September 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape('turtle')
alex.penup()
for i in range(12): #Simple concept, similar to the star program, just more lines really. 
    alex.forward(150)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(20)
    alex.stamp()
    alex.back(180)
    alex.right(30)

wn.mainloop()