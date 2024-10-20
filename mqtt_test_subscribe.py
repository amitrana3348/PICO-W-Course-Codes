import network
import time
from machine import Pin
from umqtt.simple import MQTTClient
import os

random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')


ADAFRUIT_IO_URL = 'io.adafruit.com' 
ADAFRUIT_USERNAME = 'amitrana3348'
ADAFRUIT_IO_KEY = '3e359482c74e59509c3f50ab76e3a80958f55033'
ADAFRUIT_IO_FEEDNAME = 'picow'


mqtt_feedname = 'amitrana3348/feeds/humidity'
mqtt_relay1 = 'amitrana3348/feeds/relay1'
mqtt_relay2 = 'amitrana3348/feeds/relay2'

def sub_cb(topic, msg):
    topic = topic.decode('utf-8')
    msg = msg.decode('utf-8')
    #print("Topic : ",topic, end = "=")
    if topic == "amitrana3348/feeds/relay1" and msg == "ON":
        print("relay1 can be turned ON")
    if topic == "amitrana3348/feeds/relay1" and msg == "OFF":
        print("relay1 can be turned OFF")
        
    if topic == "amitrana3348/feeds/relay2" and msg == "ON":
        print("relay2 can be turned ON")
    if topic == "amitrana3348/feeds/relay2" and msg == "OFF":
        print("relay2 can be turned OFF")
    

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


client.set_callback(sub_cb)      
client.subscribe(mqtt_relay1)
client.subscribe(mqtt_relay2)  
PUBLISH_PERIOD_IN_SEC = 10 
SUBSCRIBE_CHECK_PERIOD_IN_SEC = 0.5



while True:
    '''
    if sensor.value() == 0:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
    else:
        pass
        '''
    client.check_msg()
    time.sleep(2)


