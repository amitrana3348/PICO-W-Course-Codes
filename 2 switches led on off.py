from machine import Pin
import time
#led = Pin("LED", Pin.OUT)

sw1 = Pin(0, Pin.IN, Pin.PULL_UP)  # 13 number pin is input
sw2 = Pin(1, Pin.IN, Pin.PULL_UP)  # 13 number pin is input

#sw = Pin(13, Pin.IN)  # 13 number pin is input

#sw = Pin(13, Pin.IN, Pin.PULL_DOWN)  # 13 number pin is input

while True:	# infinite loop
    a = sw1.value()
    b = sw2.value()
    if a == 0:
        led.value(1)
    
    if b == 0:
        led.value(0)
    