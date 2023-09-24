#-------------------------------------------------------------------
# Written by Carter Stickler, September 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def getGrade(mark):
    if mark >= 75:
        return "First"
    elif mark >= 70:
        return "Upper Second"
    elif mark >= 60:
        return "Second"
    elif mark >= 50:
        return "Third"
    elif mark >= 45:
        return "F1 Supp"
    elif mark >= 40:
        return "F2"
    else:
        return "F3"
    
for i in xs:
    print("Score: " + str(i) + " Receives the grade: " + getGrade(i))