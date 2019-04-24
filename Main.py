# import the libraries
import RPi.GPIO as GPIO

# setmode something
GPIO.setmode(GPIO.BCM)

# lists the GPIO pins in list for easy acsses
relayList = [26, 19, 13, 6, 3, 22, 27, 17]

# sets up the relays
for reley in range(1, 8):
	# sets relayNumber + relay or the number of the relay to the corrisponding GPIO port
	# e.g. relayNumber1 = 26
	relayName = "relayNumber" + relay
	relayLocation = relayList[reley - 1]
	relayName = relayLocation
	# sets the Status of each relay name to False for recall later
	relayNameStatus = relayName + Status
	relayNameStatus = False
	# sets the GPIO output of relayNumber + relay
	GPIO.setup(relayName, GPIO.OUT)

# for loop to repeat
for x in range(0,1000):

	# ask for input
	commandInput = input("Command Key: ")

	# checks if commandInput character number 1 is h
	if commandInput[1] == "h":
		# sets the relayNumber of character number 0 to HIGH
		# e.g. GPIO.output(relayNumber7, GPIO.HIGH)
		relayNameLocation0 = "relayNumber" + commandInput[0]
		GPIO.output(relayNameLocation0, GPIO.HIGH)
		# prints the character number 0 e.g. 7 prints it to be High e.g. 7HIGH
		print(commandInput[0] + "HIGH")
		# sets relayNumber + character number 0 e.g. 7 + Status to True For later recall
		relayNameLocation0Status = relayNameLocation0 + Status
		relayNameLocation0Status = True

	# checks if commandInput character number 1 is l
	if commandInput[1] == "l":
		# sets the relayNumber of character number 0 to Low
		# e.g. GPIO.output(relayNumber3, GPIO.LOW)
		relayNameLocation0 = "relayNumber" + commandInput[0]
		GPIO.output(relayNumber + commandInput[0], GPIO.LOW)
		# prints the character number 0 e.g. 3 prints it to be LOW e.g. 3LOW
		print(commandInput[0] + "LOW")
		# sets relayNumber + character number 0 e.g. 3 + Status to False For later recall
		relayNameLocation0Status = relayNameLocation0 + Status
		relayNameLocation0Status = True

	# checks for input "on"
	if commandInput == "on":
		# turns all relays on
		for relay in range(1, 8):
			relayName = "relayNumber" + relay
			# relayNumber + relay e.g. GPIO.output(relayNumber5, GPIO.High)
			GPIO.output(relayName, GPIO.High)
			# sets the relayNumber + relay + Status to True for later recall
			relayNameStatus = relayName + Status
			relayNameStatus = True
			# prints "All One" doh!
			print("All One")

	# checks for input "off"
	if commandInput == "off":
		for relay in range(1, 8):
			relayName = "relayNumber" + relay
			# relayNumber + relay e.g. GPIO.output(relayNumber6, GPIO.LOW)
			GPIO.output(relayName, GPIO.LOW)
			# sets the relayNumber + relay + Status to False for later recall
			relayNameStatus = relayName + Status
			relayNameStatus = False
			# prints "All Off" doh!
			print("All Off")

	# checks for input "?" or "/"
	if commandInput == "?" or commandInput == "/":
		# prints the status of all relays
		for relay in range(1, 8):
			relayName = "relayNumber" + relay
			relayNameStatus = relayName + Status
			print("relayNumber" + relay + ":" + str(relayNameStatus))
