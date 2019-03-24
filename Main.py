# import the libraries
import RPi.GPIO as GPIO

# setmode something
GPIO.setmode(GPIO.BCM)

# set relay GPIO pins
relayNumber1 = 26
relayNumber2 = 19

# set pins as outputs
GPIO.setup(relayNumber1, GPIO.OUT)
GPIO.setup(relayNumber2, GPIO.OUT)

#for loop to repeat
for x in range(0,1000):

	# ask for input
	commandInput = input("Command Key: ")

	# checks for input "DL 0" or "DL0"
	if commandInput == "DL 0" or commandInput == "DL0":
		GPIO.output(relayNumber1, GPIO.HIGH)
		print("Desk-Light Off")

	# checks for input "DL 1" or "DL1"
	if commandInput == "DL 1" or commandInput == "DL1":
		GPIO.output(relayNumber1, GPIO.LOW)
		print("Desk-Light On")

	# checks for input "CS 0" or "CS0"
	if commandInput == "CS 0" or commandInput == "CS0":
		GPIO.output(relayNumber2, GPIO.HIGH)
		print("Charger Station Off")

	# checks for input "CS 1" or "CS1"
	if commandInput == "CS 1" or commandInput == "CS1":
		GPIO.output( relayNumber2, GPIO.LOW)
		print("Charger Station On")

	# checks for input "Help" or "help"
	if commandInput == "Help" or commandInput == "help":
		# shows Commands
		print("""
		Commands:
		DL 0 or DL0
		DL 1 or DL1
		CS 0 or CS0
		CS 1 or CS1
		or more help
		""")

		# checks for input "more help" or "More Help"
		if commandInput == "more help" or commandInput == "More Help":
			# shows how to use commands
			print("""
			DL is desk-light
			CS is charger station
			use 1 0r 0 after to turn it on or off
			""")
