import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

relayNumber1 = 37
relayNumber2 = 35
relayNumber3 = 33
relayNumber4 = 31
relayNumber5 = 29
relayNumber6 = 15
relayNumber7 = 13
relayNumber8 = 11

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
