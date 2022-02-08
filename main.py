import sys
from School_Day import *
from IFTTT_Alert import *
from datetime import date
from datetime import datetime

today = date.today()
date = today.strftime("%d-%b-%Y")

def run(flag):
    if (school_day() == True) or (flag == "f"):
        exec(open("webbot_submit_1.py").read())
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date_time = date + " " + time
        IFTTT_Alert("main.py executed websubmit.py", date_time, "" )
        print("main.py executed websubmit.py", date_time, "")
    else:
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date_time = date + " " + time
        IFTTT_Alert("main.py ran successfully, today is not a school day, websubmit.py not executed", date + " " + time, "")
        print("main.py ran successfully, today is not a school day, websubmit.py not executed", date + " " + time, "")

def edit():
    deets = open(r"logindeets.txt", "r")
    deetsex = deets.readlines()
    user_login = (deetsex[0])
    PW = (deetsex[1])
    deets.close()
    print("Login: " + user_login)
    print("Password: " + PW)
    print("Edit Login:1  Edit PW:2  Run:3  Exit:4 ")
    cmd = input("")
    if cmd == "1":
        new_login = input("New login: ")
        deets = open(r"logindeets.txt", "w")
        deets.write(new_login + "\n" + PW)
        deets.close()
        edit()
    elif cmd == "2":
        new_pw = input("New PW: ")
        deets = open(r"logindeets.txt", "w")
        deets.write(user_login + "\n" + new_pw)
        deets.close()
        edit()
    elif cmd == "3":
        run(None)
    elif cmd == "4":
        quit()
    else:
        print("Invalid Input")
        edit()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        run(None)
    else:
        try:    
            cmd = sys.argv[1]
            if cmd == "-r":
                try:
                    mod = sys.argv[2]
                    if mod == "-i":
                        count = 0
                        while True:
                            run(None)
                            count += 1
                            print(count)
                    else:
                        mod = int(mod)
                        for x in range(mod):
                            run(None)
                except IndexError:
                    run(None) 
            elif cmd == "-s":       #setup
                print("Setup")
                edit()
            elif cmd == "-f": 
                try:
                    mod = sys.argv[2]
                    if mod == "-i":
                        count = 0
                        while True:
                            run("f")
                            count += 1
                            print(count)
                    else:
                        mod = int(mod)
                        for x in range(mod):
                            run("f")
                except IndexError:
                    run("f") 
        except IndexError:
            run(None)
    