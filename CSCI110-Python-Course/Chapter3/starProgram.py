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
alex = turtle.Turtle()

alex.right(110) #For the sake of orientation only

for i in range(5): #simple for loop
    alex.forward(50)
    alex.left(145)

wn.mainloop()