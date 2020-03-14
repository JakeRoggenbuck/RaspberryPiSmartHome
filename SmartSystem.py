class Relay:
    def __init__(self, pin, name, status='LOW'):
        self.pin = pin
        self.name = name
        self.status = status
        try:
            GPIO.setup(pin, GPIO.OUT)
            print('OK')
        except:
            print(f'Error occurred when trying to init relay on pin {pin}')
            exit()

    def toggle(obj):
        if obj.status == 'HIGH':
            PIO.output(obj.pin, GPIO.LOW)
            obj.status = 'LOW'
        else:
            PIO.output(obj.pin, GPIO.HIGH)
            obj.status = 'HIGH'

    def set(obj, fstat):
        PIO.output(obj.pin, GPIO.fstat)
        obj.status = fstat


light = Relay(26, "Desk Light")
print(light.name, light.pin, light.status)

light.set('HIGH')
print(light.name, light.pin, light.status)

light.toggle()
print(light.name, light.pin, light.status)
