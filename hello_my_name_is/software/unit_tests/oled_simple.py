import machine
from ssd1306 import SSD1306_I2C

oled_rst = machine.Pin(15, machine.Pin.OUT)
oled_rst.high()
i2c0 = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
oled = SSD1306_I2C(128, 64, i2c0)

oled.text("Mitchell Stride", 0, 0)
oled.show()