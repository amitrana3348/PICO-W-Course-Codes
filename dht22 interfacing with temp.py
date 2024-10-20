from machine import Pin
import time
import dht
 
sensor = dht.DHT22(Pin(0)) 
 
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature is {0} and humidity is {1}".format(temp,hum))
    time.sleep(2)
