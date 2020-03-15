import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Relay:
    def __init__(self, pin, name, status=0):
        self.pin = pin
        self.name = name
        self.status = status
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    def toggle(self):
        self.status = 0 if self.status else 1
        GPIO.output(self.pin, self.status)

    def set(self, fstat):
        GPIO.output(self.pin, fstat)
        self.status = fstat
