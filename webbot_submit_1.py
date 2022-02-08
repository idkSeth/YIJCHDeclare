from webbot import Browser
from datetime import *
from time import *
from IFTTT_Alert import *

deets = open(r"logindeets.txt", mode = "r")
deetsex = deets.readlines()
user_login = (deetsex[0])
PW = (deetsex[1])


portal = "https://portal.yijc.edu.sg/"

today = date.today()
date = today.strftime("%d-%b-%Y")
now = datetime.now()
time = now.strftime("%H:%M:%S")
date_time = date + " " + time

location = r"Health Dec SS"

#Browser(showWindow = False , proxy = None)

web = Browser()
web.go_to(portal)
sleep(5)
web.type(user_login, id = "login")
sleep(1)
web.type(PW, id = "password")
sleep(1)
web.click(text="Sign in", id = "btn_submit")
sleep(1)
web.go_to("https://portal.yijc.edu.sg/index.html#~/com.form.submit.html?id=3bffc6b977244b6b396b89eac2e8f071 ")

web.click(id="ui-form-submit-6bdc7c2e36648f86587e46bd4f4353ca-value")                   #Cell 1, "Temperature and Health Delecration"
web.click(text = "yes", id = "ui-form-submit-56efd8bffefe8ceb5c5e4ab0b755996f-value")   #Cell 2, "Yes"
web.click(id="ui-form-submit-dd9b93625c0f09b95a0e3d73c61fcbd1-value", number = 2)       #Cell 3, "No"
web.click(id="ui-form-submit-c9cc9d24d1832243bae3d15deac824aa-value", number = 2)       #Cell 4, "No"
web.click(id="ui-form-submit-db37b6582df352a0b56ed8719035bc24-value", number = 2)       #Cell 5, "No"

web.click(id="ui-form-submit-84a7e5d37733d403bdf70ba7a5bb5e81")                         #Certify Shit
sleep(1)
web.click(text = "Submit")
web.save_screenshot(location + "\\" + date + ".png")
IFTTT_Alert("websubmit.py ran successfully", date_time, "")
web.quit()
