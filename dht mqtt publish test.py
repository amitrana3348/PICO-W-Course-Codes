import network
import time
from machine import Pin
from umqtt.simple import MQTTClient
import os
import dht
sensor = dht.DHT22(Pin(0)) 

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



random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')


ADAFRUIT_IO_URL = 'io.adafruit.com' 
ADAFRUIT_USERNAME = 'amitrana3348'
ADAFRUIT_IO_KEY = '3e359482c74e59509c3f50ab76e3a80958f55033'
ADAFRUIT_IO_FEEDNAME = 'picow'


mqtt_humidity = 'amitrana3348/feeds/humidity'
mqtt_temp = 'amitrana3348/feeds/temp'

def mqtt_connect():
    client = MQTTClient(client_id=mqtt_client_id, 
                    server=ADAFRUIT_IO_URL, 
                    user=ADAFRUIT_USERNAME, 
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)
    
    client.connect()
    print('Connected to adafruit MQTT Broker')
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature is {0} and humidity is {1}".format(temp,hum))
        time.sleep(1)
        
        client.publish(mqtt_humidity,str(hum), qos=0)
        client.publish(mqtt_temp,str(temp), qos=0)  
        print('published')
        time.sleep(5)
    except:
        print("can't read from sensor")
