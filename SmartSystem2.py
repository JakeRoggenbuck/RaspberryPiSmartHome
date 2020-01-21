# import the libraries
#import RPi.GPIO as GPIO
import os
# setmode something
#GPIO.setmode(GPIO.BCM)

# lists the GPIO pins in list for easy acsses
relayList = [26, 19, 13, 6, 3, 22, 27, 17]

relayState = []

def RelaySetup(pin, state, num):
    #GPIO.setup(pin, GPIO.OUT)
    relayState.append(state)
    print(f"Relay on pin {pin} number {num} is {state}")


def RelayLoop(setState):
    for x in range(len(relayList)):
        RelaySetup(relayList[x], setState, x)


def setMode():
    print("Set Mode")
    setWhat = int(input("What relay would you like to set? 0-7 "))
    if relayState[setWhat] == True:
        #GPIO.output(relayList[setWhat], GPIO.LOW)
        print(f"Relay {setWhat} on pin {relayList[setWhat]} has been set LOW")
        relayState[setWhat] = False 
    elif relayState[setWhat] == False:
        #GPIO.output(relayList[setWhat], GPIO.HIGH)
        print(f"Relay {setWhat} on pin {relayList[setWhat]} has been set HIGH")
        relayState[setWhat] = True
    else:
        print("Not Valid")


def checkMode():
    for x in range(len(relayList)):
        print(f"Relay {x} on pin {relayList[x]} is {relayState[x]}")


def stopMode():
    sure = input("Are you sure you want to close? Y/n ")
    if sure == "Y" or sure == "y":
        RelayLoop(False)
        print("Relays Off\nClosed")
        exit()
    else:
        print("Returning")


RelayLoop(True)
print("Relays Powered")

while(True):
    commandInput = input("$ ")

    if commandInput[0:1] == "q":
        os.system("clear")
        stopMode()

    elif commandInput[0:2] == "ls":
        os.system("clear")
        checkMode()

    elif commandInput[0:3] == "set":
        os.system("clear")
        setMode()

