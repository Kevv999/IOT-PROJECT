
from machine import Pin
from gpio_lcd import GpioLcd
import dht
import machine
import time
import network
from secrets import secrets
import urequests as requests
from time import sleep


TOKEN = "BBFF-hBDvLjipyPN6whXe2aYKOrlHCwNW5Y" #Put here your TOKEN
DEVICE_LABEL = "PicoWBoard" # Assign the device label desire to be send
WIFI_SSID = secrets["ssid"] # Assign your the SSID of your network
WIFI_PASS = secrets["password"] # Assign your the password of your network


def connect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(WIFI_SSID, WIFI_PASS)  # Your WiFi Credential
        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip

def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None

def sendData(device, variable, value):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass

connect()

tempSensor = dht.DHT11(Pin(22))     # DHT11 Constructor 

# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(16),
              enable_pin=Pin(17),
              d4_pin=Pin(18),
              d5_pin=Pin(19),
              d6_pin=Pin(20),
              d7_pin=Pin(21),
              num_lines=2, num_columns=16)
 

while True:
    lcd.clear()
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        lcd.move_to(0,0)
        lcd.putstr('Temp is {}'.format(temperature))
        lcd.move_to(0,1)
        lcd.putstr('Hum is {}%'.format(humidity))
        sendData(DEVICE_LABEL, "Temperature",temperature)
        sendData(DEVICE_LABEL, "Humidity",humidity)
    except Exception as error:
        lcd.move_to(0,0)
        lcd.putstr('Could not read sensor')
        print("Exception occurred", error)
    time.sleep(20)