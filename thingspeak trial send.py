import network
from time import sleep
import urequests

# Define the ThingSpeak channel and API key

api_key = "M8IT5P0M76HAXHBT"
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

while True:
    data = "field1=30.5&field2=65.7"
    # Send data to ThingSpeak
    url = "https://api.thingspeak.com/update?api_key={}&{}".format(api_key, data)
    response = urequests.get(url)
    # Print the response from ThingSpeak
    print(response.status_code)
    
    sleep(200)
