# import the libraries
import RPi.GPIO as GPIO

# setmode something
GPIO.setmode(GPIO.BCM)

# set relay GPIO pins
relayNumber1 = 26
relayNumber2 = 19

# set relay GPIO pin Status
relayNumber1Status = False
relayNumber2Status = False

# set pins as outputs
GPIO.setup(relayNumber1, GPIO.OUT)
GPIO.setup(relayNumber2, GPIO.OUT)

# set pins to off to start
GPIO.output(relayNumber1, GPIO.HIGH)
GPIO.output(relayNumber2, GPIO.HIGH)

# for loop to repeat
for x in range(0,1000):

	# ask for input
	commandInput = input("Command Key: ")

	# checks for input "l0" or "L0"
	if commandInput == "l0" or commandInput == "L0":
		GPIO.output(relayNumber1, GPIO.HIGH)
		print("Desk-Light Off")
		relayNumber1Status = False

	# checks for input "l1" or "L1"
	if commandInput == "l1" or commandInput == "L1":
		GPIO.output(relayNumber1, GPIO.LOW)
		print("Desk-Light On")
		relayNumber1Status = True



	# checks for input "c0" or "C0"
	if commandInput == "c0" or commandInput == "C0":
		GPIO.output(relayNumber2, GPIO.HIGH)
		print("Charger Station Off")
		relayNumber2Status = False

	# checks for input "c1" or "C1"
	if commandInput == "c1" or commandInput == "C1":
		GPIO.output( relayNumber2, GPIO.LOW)
		print("Charger Station On")
		relayNumber2Status = True



	# checks for input "Off" or "off"
	if commandInput == "Off" or commandInput == "off":
		GPIO.output( relayNumber1, GPIO.HIGH)
		GPIO.output( relayNumber2, GPIO.HIGH)
		print("All Off")
		relayNumber1Status = False
		relayNumber2Status = False

	# checks for input "On" or "on"
	if commandInput == "On" or commandInput == "on":
		GPIO.output( relayNumber1, GPIO.LOW)
		GPIO.output( relayNumber2, GPIO.LOW)
		print("All On")
		relayNumber1Status = True
		relayNumber2Status = True

	# checks for input "?"
	if commandInput == "?" or commandInput == "/":
		print("relayNumber1/desk-light:" + str(relayNumber1Status))
		print("relayNumber2/charger station:" + str(relayNumber2Status))

	# checks for input "Help" or "help"
	if commandInput == "Help" or commandInput == "help":
		# shows Commands
		print("""
		Commands:
		"l0" or "L0"
		"l1" or "L1"
		"c0" or "C0"
		"c1" or "C1"
		or "more help"
		""")

		# checks for input "more help" or "More Help"
		if commandInput == "more help" or commandInput == "More Help":
			# shows how to use commands
			print("""
			L is desk-light
			C is charger station
			use 1 0r 0 after to turn it on or off
			""")
