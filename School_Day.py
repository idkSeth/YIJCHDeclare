from datetime import *

today = date.today() #date
day = datetime.weekday(today) #Checks the day and outputs 0 for Monday, 6 for Sunday
date = today.strftime("%d/%m/%Y") #date in DD/MM/YYYY format
year = today.strftime("%Y")

file = r"{}_holidays.txt".format(year)

holidays_file = open(file, mode = "r")

holidays = holidays_file.readlines()

def holiday():
    x = 0
    while x != 65 :
        if date == (holidays[x])[0:-1]:
            return True
        x = x + 1
    else:
        return False


def school_day():
    if day == 3 or day == 5 or day == 6 :
        #print("Today is a Thursday, Saturday or Sunday. " + day)
        return False

    elif holiday() == True :
        #print("Today is a holiday")
        return False

    else:
        return True