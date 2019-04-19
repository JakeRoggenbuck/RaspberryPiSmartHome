import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

relayNumber1 = 26
relayNumber2 = 19
relayNumber3 = 13
relayNumber4 = 6
relayNumber5 = 5
relayNumber6 = 22
relayNumber7 = 27
relayNumber8 = 17

GPIO.setup(relayNumber1, GPIO.OUT)
GPIO.setup(relayNumber2, GPIO.OUT)

for x in range(0, 20):
    
    GPIO.output(relayNumber1, GPIO.HIGH);time.sleep(5)
    GPIO.output(relayNumber2, GPIO.HIGH);time.sleep(5)
    GPIO.output(relayNumber3, GPIO.HIGH);time.sleep(5)
    GPIO.output(relayNumber4, GPIO.HIGH);time.sleep(5)
    GPIO.output(relayNumber5, GPIO.HIGH);time.sleep(5)
    GPIO.output(relayNumber6, GPIO.HIGH);time.sleep(5)
    GPIO.output(relayNumber7, GPIO.HIGH);time.sleep(5)
    GPIO.output(relayNumber8, GPIO.HIGH);time.sleep(5)

    GPIO.output(relayNumber1, GPIO.LOW);time.sleep(5)
    GPIO.output(relayNumber2, GPIO.LOW);time.sleep(5)
    GPIO.output(relayNumber3, GPIO.LOW);time.sleep(5)
    GPIO.output(relayNumber4, GPIO.LOW);time.sleep(5)
    GPIO.output(relayNumber5, GPIO.LOW);time.sleep(5)
    GPIO.output(relayNumber6, GPIO.LOW);time.sleep(5)
    GPIO.output(relayNumber7, GPIO.LOW);time.sleep(5)
    GPIO.output(relayNumber8, GPIO.LOW);time.sleep(5)

