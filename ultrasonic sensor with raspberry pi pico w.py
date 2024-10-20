from machine import Pin
import utime
trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
signaloff = 0
signalon = 0
while True:
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us() # 150
   while echo.value() == 1:
       signalon = utime.ticks_us()  #  350
   duration = signalon - signaloff
   distance = duration * 0.01715
   print("The distance from object is ",distance,"cm")
   utime.sleep(3)
