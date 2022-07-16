"""***********************************************************
PROGRAM NAME:   badge_test.py
PROGRAMMER:     M. STRIDE, 2022-04-24
DESCRIPTION:    Tests the 'hello my name is' pcb badge
to verify all parts are functional.
TODO:           
BUGS:           
***********************************************************"""

import machine
import utime

#SETUP

#PINS
button_SW4_UP = machine.Pin(1, machine.Pin.IN)
button_SW5_DOWN = machine.Pin(0, machine.Pin.IN) 
sensor_RP2040_die_temp = machine.ADC(4)

#GLOBAL VARS
adc_conversion_factor = 3.3 / (65535)
button_c = 0
prev_button_press = 0

#FUNCTIONS
def button_test():
    print('Press any front button...')
    while True:
        if button_SW4_UP.value() == 0:
            print("You pressed the UP button")
        if button_SW5_DOWN.value() == 0:
            print("You pressed DOWN Button")
        utime.sleep(0.1)

def button_UP_pressed(pin):   #ISR
    global button_c, prev_button_press
    new_time = utime.ticks_ms()
    if (new_time - prev_button_press) > 250:    #debounce
        button_c +=1
        print(f'UP Button Presses: {button_c}')
        prev_button_press = new_time

def button_DOWN_pressed(pin):   #ISR
    global prev_button_press
    new_time = utime.ticks_ms()
    if (new_time - prev_button_press) > 250:    #debounce
        print(f'RP2040 Die Temp: {read_temp():.1f}')
        prev_button_press = new_time

def read_temp():
    data = sensor_RP2040_die_temp.read_u16() * adc_conversion_factor
    # Typically, Vbe = 0.706V @ 27°C, with a slope of -1.721mV (0.001721) per degree. 
    RP2040_die_temp = 27 - (data - 0.706)/0.001721
    return RP2040_die_temp

def unit_test():
    #button_test()
    #button_test_irq()
    read_temp()

#---------------------------MAIN-----------------------------------
def main():
    utime.sleep(1)   #wait for serial terminal
    print("'Hello my name is' PCB badge unit test")
    button_SW4_UP.irq(trigger=machine.Pin.IRQ_FALLING,  handler=button_UP_pressed)
    button_SW5_DOWN.irq(trigger=machine.Pin.IRQ_FALLING,  handler=button_DOWN_pressed)
    
    #unit_test()

if __name__ == "__main__":
    main()
#------------------------------------------------------------------
'''
OLED 'Are RGB LEDs working, press up?'
OLed 'Are lights green press down?'
'''