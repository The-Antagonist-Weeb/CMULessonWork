#-------------------------------------------------------------------
# Written by Carter Stickler, September 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
#I really wanted to do this assignment with an array, but I know we're supposed to be using if statements. I'll have a super short script with that below just because I wanted to do it that way, and then the official script after that one.
# weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

# numberOfWeek = input("Which number of the week would you like me to identify for you? (Ex: 0, 1, 2, 3, 4, 5, 6):")

# print("That day is called: " + weekdays[int(numberOfWeek)])

def getDayOfWeek(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"

dayOfWeek = getDayOfWeek(int(input("Which number of the week would you like me to identify for you? (Ex: 0, 1, 2, 3, 4, 5, 6):")))# This little one liner may have been a bit excessive, but it works, and I like the efficiency. Hope that's alright, haha.

print("The day is called: " + dayOfWeek)