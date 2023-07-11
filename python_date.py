from datetime import datetime as dt
# OR
import time
# The strftime() function is used to convert date and time objects to their string representation.
# It takes one or more input of formatted code and returns the string representation.


t = time.strftime("%H:%M:%S")
print(t)

a = dt.now()
print(a)
tm = a.strftime("%H:%M:%S")
print(tm)

hour = int(a.strftime("%H"))
print(hour)
minute = a.strftime("%M")
print(minute)
second = a.strftime("%S")
print(second)

if(hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<16):
    print("Good Afternoon")
elif(hour>=16 and hour<19):
    print("Good Evening!")
else:
    print(("Good Night!"))









