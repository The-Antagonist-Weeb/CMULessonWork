#---------------------------------------------------------------------
# Written by Carter Stickler, August 2023.
#
# Anyone may freely copy or modify this program. 
#   - Assuming you can find it in my hidden github. 
#   - Or if you're the instructor, and I wound up handing this to you.
#---------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------
#The following code is how I would have solved this before reading the chapter for this week (Chapter 2)
#For context, I've been working in the tech industry and I taught myself Python, Javascript, and a few other basics. Primarily Javascript.
#After reading the chapter, I'll recreate the program using the best standards I learn through the chapter, and comment this code all out!
#I just wanted to challenge myself to see if I can figure out the assignment without reading the chapter yet.
#-----------------------------------------------------------------------------------------------------------------------------------------
import time
import datetime

print("\nWelcome. With this program, we will be able to determine the specific time that it will be when your alarm goes off. \nWhen you provide the current time (In hours) and the amount of time until it goes off (In hours) that is.\n")

#time.sleep(5) #Purely for the experience while using the terminal. Gives the user time to read the prompt before requesting input.

currentTime = input("What is the current time? \nFormat: HH:MM \nEx: 8:00 AM, 10:00 PM, 14:00 \n").lower()

currentHour = int(currentTime.split(":")[0])
currentMinutes = 0

if currentHour > 24: #Validating current time. Just in case. Don't want users to enter an invalid time.
    print("\nYou have not entered a valid hour! Closing script.")
    time.sleep(3)
    exit()
elif currentHour > 12 and "pm" in currentTime: #I actually got confused here. This was initially "and "pm" or "am" in currentTime". I'm not sure why it didn't work with the or statement. 
    print("\nYou have not entered a valid hour! Closing script.")
    time.sleep(3)
    exit()
elif currentHour > 12 and "am" in currentTime:
    print("\nYou have not entered a valid hour! Closing script.")
    time.sleep(3)
    exit()

timeLength = int(input("\nHow many hours will it be until the alarm goes off? \nFormat: HH \nEx: 55 \n"))

today = datetime.date.today()

DayLeft = 24

if "pm" in currentTime: #...Definitely ineffecient to ensure proper data. Especially for something that likely isn't in the scope of this excercise. But so be it.
    DayLeft = 12
    currentMinutes = currentTime.split(":")[1].split(" ")[0]
elif "am" in currentTime:
    currentMinutes = currentTime.split(":")[1].split(" ")[0]
else:
    currentMinutes = currentTime.split(":")[1]

DayLeft -= currentHour

daysTotal = 0

dayRemainder = 0

loopFinished = False

while loopFinished == False: #Changing raw hours into days and hours
    timeLength -= 24

    if "-" in str(timeLength): #Kind of a cheap inefficient trick to not have to deal with normal division. Likely will have to fix in the second script.
        dayRemainder = timeLength + 24
        loopFinished = True
    else:
        daysTotal += 1

today += datetime.timedelta(days=daysTotal)

finalHour = currentHour + dayRemainder
finalAppend = ""

if finalHour >= 12 and "pm" in currentTime: #Final handling (Proably not in the scope in the first place) for am/pm stuff
    finalHour -= 12
    today += datetime.timedelta(days=1)
    finalAppend = " AM"
elif finalHour >= 12 and "am" in currentTime:
    finalHour -= 12
    finalAppend = " PM"
elif finalHour >= 24:
    finalHour -= 24
    today += datetime.timedelta(days=1)

finalDateTime = str(today) + " " + str(finalHour) + ":" + currentMinutes + finalAppend

print("The date and time that your alarm will go off is: " + finalDateTime)
time.sleep(3)

#-------------------------------------------------------------------------------------------------------
#Okay! I know it's NOT efficient, but I'm still happy with the end result/functionality.
#Starting the chapter now, and below will be the code re-written with optimizations from what I learned.
#Uncomment the top if you want to see how it works there! I'm not sure how much it'll change from below.
#And there was one or two things that confused me commented out up there as well.
#-------------------------------------------------------------------------------------------------------