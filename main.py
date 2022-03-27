from datetime import datetime

from telegram_bot import send_image, stop, send_text
from School_Day import school_day

now = datetime.now()
dt = now.strftime("%d-%b-%Y %H:%M:%S")
date = now.strftime("%d-%b-%Y")
location = r"SS/{}.png".format(date)


with open("telegram.txt") as f:
    chat_id = f.readlines()[1].strip()

def run(flag):
    if (school_day() == True) or (flag == "f"):
        exec(open("webbot_submit_1.py").read())
        print(f"main.py executed websubmit.py {dt}")
        send_text(chat_id, f"main.py executed websubmit.py {dt}")
        send_image(chat_id, location)
    else:
        print(f"main.py ran successfully, today is not a school day, not submmited. {dt}")
        send_text(chat_id, f"main.py ran successfully, today is not a school day, not submmited. {dt}")

if __name__ == "__main__":
   run(None)
   stop()
   exit()