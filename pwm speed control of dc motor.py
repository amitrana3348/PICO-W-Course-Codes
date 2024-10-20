import time
from machine import Pin, PWM
# Construct PWM object, with LED on Pin(25).
in1 = Pin(0,Pin.OUT)
in2 = Pin(1,Pin.OUT)
pwm1 = PWM(Pin(2))
# Set the PWM frequency.
pwm1.freq(1000)
# Set the Duty Cycle Value between 0 – 65535 i.e. 16 bit value.

while True:
   
    print("motor stopped")
    in1.value(0)
    in2.value(0)
    time.sleep(2)
    
    pwm1.duty_u16(32767)
    print("motor moving cclk")
    in1.value(1)
    in2.value(0)
    time.sleep(2)
    
    pwm1.duty_u16(65535)
    print("motor stopped")
    in1.value(0)
    in2.value(0)
    time.sleep(2)
    
    pwm1.duty_u16(10000)
    print("motor moving clk")
    in1.value(0)
    in2.value(1)
    time.sleep(3)
    