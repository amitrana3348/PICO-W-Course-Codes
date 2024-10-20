import time
import network
from machine import Pin
import BlynkLib
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Robotics Lab","Robotics@321")
 
BLYNK_AUTH = 'ozDgrBQOhQv0Hc-8z2oNHSIdscNyEHd6'
 
# Wait for network connection
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    ip = wlan.ifconfig()[0]
    print('IP: ', ip)
 
# Connect to Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
 
# Initialize the relay pins
relay1_pin = Pin(1, Pin.OUT)
led_pin = Pin("LED", Pin.OUT)

 
# Register virtual pin handler
@blynk.on("V1") #virtual pin V1
def v1_write_handler(value): #read the value
    if int(value[0]) == 1:
        relay1_pin.value(1) #turn the relay1 on
    else:
        relay1_pin.value(0) #turn the relay1 off
        

@blynk.on("V2") #virtual pin V1
def v2_write_handler(value): #read the value
    if int(value[0]) == 1:
        led_pin.value(1) #turn the relay1 on
    else:
        led_pin.value(0) #turn the relay1 off
 

 
while True:
    blynk.run()