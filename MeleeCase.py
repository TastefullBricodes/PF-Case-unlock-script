import random
import time

Caseopens = 0
Casetotalcost = 150
casestartingchance = 1/100
caseincrementalchance = 0.25/100
meleesunlocked = 0

def openacase():
    global Caseopens
    global Casetotalcost
    global casestartingchance
    global caseincrementalchance
    global meleesunlocked
    Caseopens += 1
    if random.random() < casestartingchance:
        global meleesunlocked
        meleesunlocked += 1
        print("You have unlocked " + str(meleesunlocked) + " melee(s) at attempt " + str(Caseopens) + "Current spending until melee:" + str(Casetotalcost*Caseopens))
    else:
        print("Nope,Current attemps:" + str(Caseopens) + " Current Chance: " + str(casestartingchance + (caseincrementalchance*Caseopens)*100))
    casestartingchance += caseincrementalchance

i = 0
for i in range(1, 1000):
    openacase()
    time.sleep(0.1)
    i += 1
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







