import os
from dotenv import load_dotenv
from datetime import datetime

if os.getenv("use_bot") == "True":
    from telegram_bot import send_image, stop, send_text
from School_Day import school_day

load_dotenv()

now = datetime.now()
dt = now.strftime("%d-%b-%Y %H:%M:%S")
date = now.strftime("%d-%b-%Y")
location = r"SS/{}.png".format(date)


def run(flag):
    if (school_day() == True) or (flag == "f"):
        exec(open("webbot_submit_1.py").read())
        print(f"Ran webbot submit code {dt}")
        if os.getenv("use_bot") == "True":
            chat_id = os.getenv("chat_id")
            send_text(chat_id, f"Ran webbot submit code {dt}")
            send_image(chat_id, location)
    else:
        print(f"main.py ran successfully, today is not a school day, not submmited. {dt}")
        if os.getenv("use_bot") == "True":
            chat_id = os.getenv("chat_id")
            send_text(chat_id, f"main.py ran successfully, today is not a school day, not submmited. {dt}")

if __name__ == "__main__":
    run(None)
    if os.getenv("use_bot") == "True":
        stop()
    exit()
