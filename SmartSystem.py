# import the libraries
import RPi.GPIO as GPIO
# setmode something
GPIO.setmode(GPIO.BCM)

class Relay:
    def __init__(self, pin, name, status='LOW'):
        self.pin = pin
        self.name = name
        self.status = status
        try:
            GPIO.setup(pin, GPIO.OUT)
            print('OK')
        except:
            print('Error occurred when trying to init relay on pin ' + str(pin))
            exit()

    def toggle(obj):
        if obj.status == 'HIGH':
            GPIO.output(obj.pin, GPIO.LOW)
            obj.status = 'LOW'
        else:
            GPIO.output(obj.pin, GPIO.HIGH)
            obj.status = 'HIGH'

    def set(obj, fstat):
        GPIO.output(obj.pin, eval(GPIO.fstat)
        obj.status = fstat


light = Relay(26, "Desk Light")
print(light.name, light.pin, light.status)

light.set('HIGH')
print(light.name, light.pin, light.status)

light.toggle()
print(light.name, light.pin, light.status)
