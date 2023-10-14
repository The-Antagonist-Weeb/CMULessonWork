#-------------------------------------------------------------------
# Written by Carter Stickler, October 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
def print_triangular_numbers(n):
    for i in range(1, n + 1):   
        print("n = " + str(i) + ", triangle = " + str((i ** 2 + i)//2)) #I would have preferred to use a .format() function here, but I don't think we've covered that in this course yet if I'm remembering correctly. Program is relatively self explanatory other than that.

print_triangular_numbers(5)