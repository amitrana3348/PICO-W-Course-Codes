import network
from time import sleep
import urequests
import dht
from machine import Pin
led = Pin("LED", Pin.OUT)


# Define the ThingSpeak channel and API key

api_key = "R8EHEQ0XP69NB8VB"

def blink():
    for i in range(0,5):
        led.value(1)
        sleep(0.3)
        led.value(0)
        sleep(0.3)

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("Robotics Lab", "Robotics@321")
    print('Waiting for connection...')
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print('wifi connected ...')
    print(wlan.ifconfig())

connect()
sensor = dht.DHT22(Pin(0)) 

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature: {0}°C   Humidity: {1}% ".format(temp, hum))
    
    data = "field1={0}&field2={1}".format(temp, hum)
    # Send data to ThingSpeak
    print(data)
    
    
    url = "https://api.thingspeak.com/update?api_key=R8EHEQ0XP69NB8VB&"+ data
    
    print("\n\n")
    print(url)
    response = urequests.get(url)
    ## Print the response from ThingSpeak
    print(response.status_code)
    response.close()
    
    blink()
    
    sleep(15)

