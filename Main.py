import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
 
relayNumber1 = 15
relayNumber2 = 16

GPIO.setup(relayNumber1, GPIO.OUT)
GPIO.setup(relayNumber2, GPIO.OUT)

for x in range(0,1000)

	commandInput = input("Command Key: ")

	if commandInput == "DL 0" or "DL0":
		GPIO.output(relayNumber1, GPIO.LOW)

	if commandInput == "DL 1" or "Dl1":
		GPIO.output(relayNumber1, GPIO.HIGH)

	if commandInput == "C 0" or "C0":
		GPIO.output(relayNumber2, GPIO.LOW)

	if commandInput == "C 1" or "C1":
		GPIO.output(relayNumber2, GPIO.HIGH)
