from datetime import *

today = date.today() #date
day = datetime.weekday(today) #Checks the day and outputs 0 for Monday, 6 for Sunday
date = today.strftime("%d/%m/%Y") #date in DD/MM/YYYY format
year = today.strftime("%Y")

file = r"{}_holidays.txt".format(year)

with open(file, mode = "r") as f:
    holidays = f.readlines()

def holiday():
    for d in holidays:
        if date == d[:-1]:
            return True
    return False


def school_day():
    if day in (3,5,6):
        return False
    elif holiday():
        return False
    else:
        return True