# import the libraries
#import RPi.GPIO as GPIO
# setmode something
#GPIO.setmode(GPIO.BCM)

class Relay:
    def __init__(self, pin, name, status=0):
        self.pin = pin
        self.name = name
        self.status = status
        try:
            GPIO.setup(pin, GPIO.OUT)
        except:
            print(f'Error occurred when trying to init relay on pin ' + str(pin))
            exit()

    def toggle(self):
        if self.status == 1:
            GPIO.output(self.pin, 0)
            self.status = 0
        else:
            GPIO.output(self.pin, 1)
            self.status = 1

    def set(self, fstat):
        GPIO.output(self.pin, fstat)
        self.status = fstat

light = Relay(26, "Desk Light")
print(light.name, light.pin, light.status)
