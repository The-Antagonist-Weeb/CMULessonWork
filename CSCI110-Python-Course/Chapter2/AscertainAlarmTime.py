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
#I just wanted to challenge myself to see what I can do with the assignment without reading the chapter yet. If you want to test it out,
#you can uncomment all of lines 16-91. 
#
#Something to note after making both scripts: I went way past scope for this assignment, haha. Either way, I had a lot of notes, and if 
#there's anything that can be improved, please let me know!
#-----------------------------------------------------------------------------------------------------------------------------------------
# import time
# import datetime

# print("\nWelcome. With this program, we will be able to determine the specific time that it will be when your alarm goes off. \nWhen you provide the current time (In hours) and the amount of time until it goes off (In hours) that is.\n")

# time.sleep(5) #Purely for the experience while using the terminal. Gives the user time to read the prompt before requesting input.

# currentTime = input("What is the current time? \nFormat: HH:MM \nEx: 8:00 AM, 10:00 PM, 14:00 \n").lower()

# currentHour = int(currentTime.split(":")[0])
# currentMinutes = 0

# if currentHour > 24: #Validating current time. Just in case. Don't want users to enter an invalid time.
#     print("\nYou have not entered a valid hour! Closing script.")
#     time.sleep(3)
#     exit()
# elif currentHour > 12 and "pm" in currentTime: #I actually got confused here. This was initially "and "pm" or "am" in currentTime". I'm not sure why it didn't work with the or statement. 
#     print("\nYou have not entered a valid hour! Closing script.")
#     time.sleep(3)
#     exit()
# elif currentHour > 12 and "am" in currentTime:
#     print("\nYou have not entered a valid hour! Closing script.")
#     time.sleep(3)
#     exit()

# timeLength = int(input("\nHow many hours will it be until the alarm goes off? \nFormat: HH \nEx: 55 \n"))

# today = datetime.date.today()

# DayLeft = 24

# if "pm" in currentTime: #...Definitely ineffecient to ensure proper data. Especially for something that likely isn't in the scope of this excercise. But so be it.
#     DayLeft = 12
#     currentMinutes = currentTime.split(":")[1].split(" ")[0]
# elif "am" in currentTime:
#     currentMinutes = currentTime.split(":")[1].split(" ")[0]
# else:
#     currentMinutes = currentTime.split(":")[1]

# DayLeft -= currentHour

# daysTotal = 0

# dayRemainder = 0

# loopFinished = False

# while loopFinished == False: #Changing raw hours into days and hours
#     timeLength -= 24

#     if "-" in str(timeLength): #This whole if statement is kind of a cheap inefficient trick to not have to deal with normal division. Decimal processing is tedious and I haven't figured out the best ways to deal with it yet. I'm guessing there's an efficent way to do it, and I'm overthinking it due to lack of python foundation. Likely will have to fix in the second script.
#         dayRemainder = timeLength + 24 #FOUND IT!!! The modulus operator! I'll be incorporating this in the next script. I realize if I had just searched google for finding the remainder of a division in Python, I would have found this way sooner. Exactly why I'm taking this course!!
#         loopFinished = True
#     else:
#         daysTotal += 1

# today += datetime.timedelta(days=daysTotal)

# finalHour = currentHour + dayRemainder
# finalAppend = ""

# if finalHour >= 12 and "pm" in currentTime: #Final handling (Proably not in the scope in the first place) for am/pm stuff
#     finalHour -= 12
#     today += datetime.timedelta(days=1)
#     finalAppend = " AM"
# elif finalHour >= 12 and "am" in currentTime:
#     finalHour -= 12
#     finalAppend = " PM"
# elif finalHour >= 24:
#     finalHour -= 24
#     today += datetime.timedelta(days=1)

# finalDateTime = str(today) + " " + str(finalHour) + ":" + currentMinutes + finalAppend

# print("The date and time that your alarm will go off is: " + finalDateTime)
# time.sleep(3)

#-------------------------------------------------------------------------------------------------------
#Okay! I know it's NOT efficient, but I'm still happy with the end result/functionality.
#Starting the chapter now, and below will be the code re-written with optimizations from what I learned.
#Uncomment the top if you want to see how it works there! I'm not sure how much it'll change from below.
#And there was one or two things that confused me commented out up there as well.
#-------------------------------------------------------------------------------------------------------

import time
import datetime
import re

today = datetime.date.today()
DayLeft = 24
finalAppend = ""

# def getDaysAndhours(hours): # I started using this originally since I indended to run this twice, but that became obsolete with the comment on line #147.
#     daysTotal = hours//24
#     hoursTotal = hours%24
#     return {
#         "days": daysTotal,
#         "hours": hoursTotal
#     }

print("\nWelcome. With this program, we will be able to determine the specific time that it will be when your alarm goes off. \nWhen you provide the current time (In hours) and the amount of time until it goes off (In hours) that is.\n")

#time.sleep(5) #Purely for the experience while using the terminal. Gives the user time to read the prompt before requesting input.

currentTime = input("What is the current time? \nFormat: HH:MM \nEx: 8:00 AM, 10:00 PM, 14:00 \n").lower()

currentHour = int(currentTime.split(":")[0])

if currentHour > 24: #Validating current time. Just in case. Don't want users to enter an invalid time.
    print("\nYou have not entered a valid hour! Closing script.")
    time.sleep(3)
    exit()
elif currentHour > 12 and re.search("pm|am", currentTime): #I realize why I got confused here, I kept thinking "or" and "|" would be the appropriate replacement for "||" from js, which is I was confused as to what else would do the job. Heck, maybe I'm still confused and there's a better way to do this than importing "re". But as you can see, a bit more research did the job. I thought the same with "and" and "&&" btw. The joys of learning two programming languages at the same time in the fires of a production environment!!
    print("\nYou have not entered a valid hour! Closing script.")
    time.sleep(3)
    exit()

timeLength = int(input("\nHow many hours will it be until the alarm goes off? \nFormat: HH \nEx: 55 \n"))

if "pm" in currentTime: #...Definitely ineffecient to ensure proper data. Especially for handling that likely isn't in the scope of this excercise. Please let me know if you have any recommendations to improve this!
    DayLeft = 12
    currentMinutes = currentTime.split(":")[1].split(" ")[0]
    finalAppend = " PM"
elif "am" in currentTime:
    currentMinutes = currentTime.split(":")[1].split(" ")[0]
    finalAppend = " AM"
else:
    currentMinutes = currentTime.split(":")[1]

DayLeft -= currentHour

timeLength += currentHour #not what I originally intended, but as I found and fixed flaws, it just wound up in this state of finding how many days/hours it would be from 0 hour on this date. Which I can see the logic in! I actually like this a lot, because I was really messing up with the variable of the current hour before. 

daysTotal = timeLength//24
finalHour = timeLength%24

today += datetime.timedelta(days=daysTotal)
print("Finalhour:",finalHour)
hourDef = [12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11]

if finalHour >= 12 and "PM" in finalAppend: #Final handling (Proably not in the scope in the first place) for am/pm stuff. Once again here, I feel like there is likely a better way to do this. If you have any recommendations for handling this kind of thing, anything would be appreciated!! I also notice that when inputting AM/PM, normally 12 AM and 12 PM are normal to see rather than 0:00 PM/AM. At least that is what most people are used to. I wonder if I can use an array or some similar definition to fix that so that it displays properly without four more if statements... Maybe an array like: [12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11] and use the final hour number to determine what item (hour) in the array to display? I'll try it
    finalAppend = " AM"
    today += datetime.timedelta(days=1)
    finalHour = hourDef[finalHour - 12] #Hey, that worked! Sorry for the super long comment above, it was me thinking through using the array like this. ...This may have become obsolete? With the way I redesigned some parts of this. Nevermind!! Just double checked, it still serves it's purpose of making 0 hour show as 12 when using AM/PM. It gets confusing when I keep re-doing this.
elif finalHour >= 12 and "PM" in finalAppend:
    finalAppend = " PM"
    finalHour = hourDef[finalHour - 12]
elif re.search("AM|PM", finalAppend):
    finalHour = hourDef[finalHour]

if finalHour == 0: #This is purely to have the second 0, because I like the details, haha. Pretty unnecessary, just as much of this likely is, but for this excercise, I think it's fine. Most likely this can be solved with a datetime hour calculation in just 10 lines or so... I'm guessing. Don't take my word for it. Might try it below this script... I didn't. I found out I definitely could, but I didn't want to go through AM/PM stuff again.
    finalHour = "00"

finalDateTime = str(today) + " " + str(finalHour) + ":" + currentMinutes + finalAppend

print("The date and time that your alarm will go off is: " + finalDateTime)
time.sleep(3)
#-------------------------------------------------------------------------------------------------------------------------
#Okay, after the above two scripts, I watched the video for the week...
#Sorry for overthinking so much. I'll probably simplify future scripts, but I am proud of these.
#I've been way ahead reading wise and class wise, so I'm finishing this as of Monday the week I'm submitting this.
#And I was honestly kinda bored, and this was super fun.
#Anyway, I would really appreciate it if you have recommendations on any of this code for how I can improve!
#I've been working in the industry for awhile, but I've never really had a peer able to teach me much due to circumstance.
#To be honest, I just got excited. Anyway, thanks for reviewing my script!!
#-------------------------------------------------------------------------------------------------------------------------