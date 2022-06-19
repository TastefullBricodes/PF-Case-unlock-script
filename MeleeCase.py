import random
import time

Caseopens = 0
Casetotalcost = 150
casestartingchance = 1/100
caseincrementalchance = 0.25/100
meleesunlocked = 0

####################################################
#User Controls
attempts = 100 #how many cases you want to open
rununtilmelee = 1 # Boolean Operation, loop will stop when you get a melee
####################################################

def generatereport():
    print("----------------------------------------------------------------------------------")
    time.sleep(1)
    print("Generating Report...")
    time.sleep(0.3)
    print("----------------------------------------------------------------------------------")
    print("total spent: " + str(Casetotalcost * Caseopens))
    print("total attempts: " + str(Caseopens))
    print("total melee unlocked: " + str(meleesunlocked))
    print("total melee unlocked per attempt: " + str(meleesunlocked/Caseopens))
    print("----------------------------------------------------------------------------------")

def openacase():
    global Caseopens
    global Casetotalcost
    global casestartingchance
    global caseincrementalchance
    global meleesunlocked
    global rununtilmelee
    Caseopens += 1
    if random.random() < casestartingchance:
        global meleesunlocked
        meleesunlocked += 1
        print("Sucsess, You have unlocked " + str(meleesunlocked) + " melee(s) at attempt " + str(Caseopens) + "Current spending until melee:" + str(Casetotalcost*Caseopens))
        if rununtilmelee == 1:
            print("You have unlocked all melee weapons, please close this window")
            generatereport()
            time.sleep(5)
            exit()
    else:
        print("Failed,Current attemps:" + str(Caseopens) + " Current Chance: " + str(casestartingchance + (caseincrementalchance*Caseopens)*100))
    casestartingchance += caseincrementalchance

i = 0
for i in range(1, attempts):
    openacase()
    time.sleep(0)
    i += 1
generatereport()
