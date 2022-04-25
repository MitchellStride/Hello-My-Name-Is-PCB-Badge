import machine
import utime

button = machine.Pin(0, machine.Pin.IN) #gpio 0 or 1

while True:
    if button.value() == 0:
    print("You pressed the button!")
    utime.sleep(2)