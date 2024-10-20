from machine import Pin
led = Pin("LED", Pin.OUT)

sw = Pin(0, Pin.IN, Pin.PULL_UP)  # 13 number pin is input
import time
#sw = Pin(13, Pin.IN)  # 13 number pin is input

#sw = Pin(13, Pin.IN, Pin.PULL_DOWN)  # 13 number pin is input

while True:
    a = sw.value()
    #print(a)
    if(a == 0):
        led.value(1)
    else:
        led.value(0)
    #time.sleep(1)