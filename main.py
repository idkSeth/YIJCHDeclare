import sys
from datetime import datetime

from School_Day import school_day

now = datetime.now()
dt = now.strftime("%d-%b-%Y %H:%M:%S")

def run(flag):
    if (school_day() == True) or (flag == "f"):
        exec(open("webbot_submit_1.py").read())
        print(f"main.py executed websubmit.py {dt}")
    else:
        print(f"main.py ran successfully, today is not a school day, not submmited. {dt}")

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