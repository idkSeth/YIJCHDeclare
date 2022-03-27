"""Use school_day which returns a bool if the current day is a school day."""

from datetime import datetime

now = datetime.now()
day = datetime.weekday(now) 
date = now.strftime("%d/%m/%Y") 
year = now.strftime("%Y")

file = r"{}_holidays.txt".format(year)

with open(file, mode = "r") as f:
    holidays = f.readlines()

def _holiday():
    for day in holidays:
        if date == day[:-1]:
            return True
    return False

def school_day():
    if day in (3,5,6):
        return False
    elif _holiday():
        return False
    else:
        return True