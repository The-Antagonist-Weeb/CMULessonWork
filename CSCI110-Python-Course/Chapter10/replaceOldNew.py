#-------------------------------------------------------------------
# Written by Carter Stickler, December 2023.
#
# Anyone may freely copy or modify this program. 
#   Assuming you can find it in my hidden github. 
#   Or if you're the instructor, and I wound up handing this to you.
#-------------------------------------------------------------------
string = "This is a testing string. Test god. Test myself. Test everything."

def replace(s, old, new):
    splitResult = s.split(old)
    joinResult = new.join(splitResult)
    return joinResult

print(replace(string, "Test", "Cheese"))