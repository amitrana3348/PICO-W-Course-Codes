import time
from machine import Pin, PWM
# Construct PWM object, with LED on Pin(25).
pwm1 = PWM(Pin(0))
# Set the PWM frequency.
pwm1.freq(1000)
# Set the Duty Cycle Value between 0 – 65535 i.e. 16 bit value.

while True:
    for i in range(0,65535,50):
        pwm1.duty_u16(i)
        time.sleep(0.01)
    
    print("100% ON")
    time.sleep(2)
    
    for i in range(65535, 0, -50):
        pwm1.duty_u16(i)
        time.sleep(0.01)
    
    print("100% OFF")
    time.sleep(2)
