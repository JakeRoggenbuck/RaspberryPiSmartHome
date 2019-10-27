# import the libraries
#import RPi.GPIO as GPIO

# setmode something
#GPIO.setmode(GPIO.BCM)

# lists the GPIO pins in list for easy acsses
relayList = [26, 19, 13, 6, 3, 22, 27, 17]

relayState = []

def RelaySetup(pin, state, num):
    #GPIO.setup(pin, GPIO.OUT)
    relayState.append(state)
    print("Relay on pin " + str(pin) + " number " + str(num) + " is " + str(state))

def RelayLoop(setState):
    for x in range(len(relayList)):
        RelaySetup(relayList[x], setState, x)

def setMode():
    print("Set Mode")
    setWhat = int(input("What relay would you like to set? 0-8 "))
    if relayState[setWhat] == True:
        #GPIO.output(relayList[setWhat], GPIO.LOW)
        print("Relay " + str(setWhat) + " on pin " + str(relayList[setWhat]) + " has been set LOW")
        relayState[setWhat] = False 
    elif relayState[setWhat] == False:
        #GPIO.output(relayList[setWhat], GPIO.HIGH)
        print("Relay " + str(setWhat) + " on pin " + str(relayList[setWhat]) + " has been set HIGH")
        relayState[setWhat] = True
    else:
        print("Not Valid")

def checkMode():
    for x in range(len(relayList)):
        print("Relay " + str(x) + " on pin " + str(relayList[x]) + " is " + str(relayState[x]))

def stopMode():
    sure = input("Are you sure you want to close? Y/n ")
    if sure == "Y" or sure == "y":
        print("Relays Off")
        print("Closed")
        exit()
    else:
        print("Returning")

RelayLoop(True)
print("Relays Powered")

while(True):
    commandInput = input("$ ")
    
    if commandInput[0:3] == "set":
        setMode()

    elif commandInput[0:4] == "stop":
        stopMode()

    elif commandInput[0:5] == "check":
        checkMode()
