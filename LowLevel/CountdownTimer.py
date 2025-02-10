import time

timeUnit = input("Would you like to set a timer in seconds, minutes or hours?")
timeUnit = timeUnit.strip()
timeLength = int(input("How long would you like this timer to be?"))

#takes the input from any time unit and turns it so seconds
def convert_time():
    if timeUnit == "seconds" or timeUnit == "second":
        return timeLength
    elif timeUnit == "minutes" or timeUnit == "minute":
        return timeLength * 60

    elif timeUnit == "hours" or timeUnit == "hour":
        return timeLength * 3600
    else:
        print("Invalid Input, try again")
        exit()


print("You have selected ",timeLength ,timeUnit)
#converts all time to seconds for clear countdown
total_seconds = convert_time()
       
    
while total_seconds >= 0:
    print(total_seconds, end="\r")
    time.sleep(1)
    total_seconds -= 1


print("Time is Over!")




