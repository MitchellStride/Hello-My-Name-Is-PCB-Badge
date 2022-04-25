from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(27), scl=Pin(28), freq=400000)  #fix pins
oled = SSD1306_I2C(128, 64, i2c)

oled.text("Mitchell Stride", 0, 0)
oled.show()