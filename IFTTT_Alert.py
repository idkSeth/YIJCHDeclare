import requests

iftttdeets = open(r"C:\Users\setho\Desktop\YIJCHDeclare\deets.txt", mode = "r")
iftttdeetsex = iftttdeets.readlines()
beta = False

if (iftttdeetsex[0])[7:11] == "True" :
    beta = True
    alpha = (iftttdeetsex[2])[0:-1]

def IFTTT_Alert(first, second, third):
    if beta == True :
        report = {}
        report["value1"] = first
        report["value2"] = second
        report["value3"] = third
        requests.post(alpha, data=report)