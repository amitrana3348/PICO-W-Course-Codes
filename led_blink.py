from machine import Pin
import time
led = Pin(26, Pin.OUT)

while True:
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(2)

