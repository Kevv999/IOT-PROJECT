# Temperature and humidity displayed on LCD
Kevin Eriksson / ke222yn

This project measures the temperature and humidity using a DH11 sensor and displays the results on a 16x2 LCD screen. By recreating the project it's possible to measure the temperature and humidity in a desired environment. 

Approximately 2-3 hours is the time to recreate this project.

## Objective
I choose this project to gain insight into indoor temperature and humidity. The purpose of this project is to create an easy way of viewing the indoor temperature and humidity using an LCD screen as well as viewing the data using a dashboard provided by Ubidots. This project provided new insights into indoor temperature and humidity, enabling me to keep track of and improve the indoor environment.

## Material

| Component  | Part of | Bought at | Price |
| ------------- | ------------- | ------------- | ------------- |
| Raspberry Pi Pico WH  | Start Kit – Applied IoT at LNU  | electrokit.com  | 109 SEK  |
| DHT11  | Start Kit – Applied IoT at LNU   | electrokit.com  | 49 SEK |
| Jumper Wires  | Start Kit – Applied IoT at LNU   | electrokit.com  | 49 SEK |
| Breadboard 840  | Start Kit – Applied IoT at LNU   | electrokit.com  | 69 SEK |
| Micro USB cable  | Start Kit – Applied IoT at LNU   | electrokit.com  | 39 SEK |
| LCD 2x16  |   | electrokit.com  | 99 SEK |

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*Figure 1:* Raspberry Pi Pico WH 

The Raspberry Pi Pico WH served as the main control unit in the project. It interfaced with the DHT11 sensor to measure temperature and humidity, displayed the data on the LCD screen, and communicated with the Ubidots platform for remote monitoring. Its compact size and low power consumption made it ideal for the project's requirements.

<img src="https://github.com/Kevv999/IOT-PROJECT/assets/100692756/42bfccef-79eb-4645-b154-69edf26f7476" alt="Image" width="200" height="200">



*Figure 2:* DHT11

The DHT11 sensor is used to obtain basic temperature and humidity data, and served the purpose of measuring temperature and humidity in the project.

<img src="https://github.com/Kevv999/IOT-PROJECT/assets/100692756/738ad017-cc38-4ede-9b99-ee6abf8c0d54" alt="Image" width="200" height="200">


*Figure 3:* Jumper Wires

Jumper Wires are used to establish electrical connections between different components. In the project, they were used to establish the necessary connection between the components.  

<img src="https://github.com/Kevv999/IOT-PROJECT/assets/100692756/4991874a-b2ed-4cd0-bb8b-737ec172b9d7" alt="Image" width="200" height="200">



*Figure 4:* Breadboard

The Breadboard is used to create temporary electrical connections. It consists of a plastic board with a grid of holes. The holes are used for easy insertions and connection of electronic components. In the project, the breadboard served as a platform for connecting and assembling electronic components.

<img src="https://github.com/Kevv999/IOT-PROJECT/assets/100692756/44c04729-c7b2-47c7-937e-bfe268f57442" alt="Image" width="200" height="200">


*Figure 5:* 2x16 LCD 

The 2x16 LCD is a display with two rows of 16 characters each. It is commonly used to provide visual output and display information. In the project, it served the purpose of displaying the temperature and humidity.

<img src="https://github.com/Kevv999/IOT-PROJECT/assets/100692756/79684c27-5038-4c34-aa06-ab7d35f8965e" alt="Image" width="200" height="200">

## Computer setup

I chose Visual Studio Code as my IDE for programming the Raspberry Pi Pico WH. The reason for this choice was based on my previous experience with the software. This is also how I uploaded the code, through Visual Studio Code.

## Steps

1. Micropython firmware
   
   Install micropython firmware from this [Link](https://micropython.org/download/rp2-pico-w/)<br>
   Copy and paste the firmware to the Raspberry Pi Pico WH storage.

2. Visual Studio Code

   Install Visual Studio Code from this [Link](https://code.visualstudio.com/)<br>
   Install Node.js from this [Link](https://nodejs.org/en)<br>
   Install PyMakr in Visual Studio Code

## Putting everything together

*Figure 6:* Wiring

![image](https://github.com/Kevv999/IOT-PROJECT/assets/100692756/c4ef0799-7569-4716-8ecd-32631855cd2d)

(The image is created in Wokwi which is an online platform that provides a virtual simulation environment for testing, designing and simulating. This is also the reason why this image uses a DH22 sensor instead of the DHT11 sensor, either way, both sensors work great for this project.)

This is how the wiring could look like, the DHT11 sensor is connected to the Raspberry Pi Pico Wh using jumper wires. The connections are for data, power(VCC), and ground (GND).
The LCD is also connected to the Raspberry Pi Pico WH using jumper wires to establish a connection for data and power.

In the circuit diagram, the GND of the DHT11 sensor is connected to the GND pin of the Raspberry Pi Pico WH. The SDA of the DHT11 is connected to GP22 of the Raspberry Pi Pico WH and the VCC of DHT11 is connected to the 3V3 of the Raspberry Pi Pico WH.

The LCD is connected to the Raspberry Pi Pico WH by connecting the GND of the RPPWH to the VSS, RW and K pins of the LCD. Then Connecting (D4,D5,D6,D7,E) from the LCD to (GP18,GP19,GP20,GP21,GP17), as well as VDD and V0 to the 3V3 pin of the RPPWH.


## Platform


Ubidots became a clear choice for the project as it didn’t need for self-hosting or additional costs for storing basic data such as temperature and humidity. Ubidots is a cloud-based platform that met my requirements. 
It's a platform that offers a range of functionality for managing and visualizing data. If I were to scale the idea further, then looking into a Ubidots Subscription plan would be a great choice. The reason why this would be a great choice is that using a familiar platform ensures a smooth transition, minimizing the learning curve to a new platform.


## The code 

To make the LCD work I used the libraries gpio_lcd and lcd_api from this [Link](https://www.circuitschools.com/interfacing-16x2-lcd-module-with-raspberry-pi-pico-with-and-without-i2c/)

Creating an object called tempSensor to interact with the DHT11 sensor. This object let us read temperature and humidity.
```py
tempSensor = dht.DHT11(Pin(22))
```

Creating an LCD Object with the help of the libraries gpio_lcd and lcd_api which can be found at the link above.
This object let us control the behavior of the connected LCD. This includes displaying text, such as the temperature and humidity.
```py
lcd = GpioLcd(rs_pin=Pin(16),
              enable_pin=Pin(17),
              d4_pin=Pin(18),
              d5_pin=Pin(19),
              d6_pin=Pin(20),
              d7_pin=Pin(21),
              num_lines=2, num_columns=16)
 
```
This while loop goes on forever and updates the LCD screen with the current temperature and humidity. This code snippet does also send temperature data and humidity data to Ubidots using the function called sendData.
```py
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
```

## Transmitting the data/connectivity

The line ```time.sleep(20) ``` in the code snippet above tells us that our temperature data and humidity data are sent every 20 seconds.
The chosen wireless protocol is WiFi because the Raspberry Pi Pico WH has wifi capabilities, which allow for communication through the network.
HTTPs post request is the transport protocol for data transmission.



Here you should add your token från Ubidots and add your wifi credentials.
```py
TOKEN = "YOURTOKEN" #Put here your TOKEN
DEVICE_LABEL = "PicoWBoard" # Assign the device label desire to be send
WIFI_SSID = secrets["ssid"] # Assign your the SSID of your network
WIFI_PASS = secrets["password"] # Assign your the password of your network
```
The code provided is a function called connect() that establishes a Wi-Fi connection.
```py
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
```
Creates a JSON object using a variable as the key and the value to the corresponding value.
```py
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None
```
sendData is a function that sends data to the Ubidots platform.
```py
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

```

## Presenting the data

Data is sent and saved every 20 seconds. The Data on the temperature and humidity is stored for an indefinite amount of time. As of right now, I use a 30-day trial on Ubidots. This could of course be extended further using a subscription plan.

### Temperature
This is how the temperature is presented in the dashboard.
The widgets that are used in the dashboard for displaying the temperature are the line chart and the thermometer widget.<br>
*Figure 7:* Temperature
![image](https://github.com/Kevv999/IOT-PROJECT/assets/100692756/e7d3ac99-297c-4874-b978-61e89940bcf6)


### Humidity
This is how the humidity is presented in the dashboard.
The widgets that are used in the dashboard for displaying the humidity are the line chart and the metric widget.<br>
*Figure 8:* Humidity
![image](https://github.com/Kevv999/IOT-PROJECT/assets/100692756/01bceb69-d65b-4476-bd41-1f1671f97de0)

### Full view of the dashboard
*Figure 9:* Dashboard
![image](https://github.com/Kevv999/IOT-PROJECT/assets/100692756/bc69e65b-5c17-465a-ab7c-37aeece3fef0)

## Finalizing the design

I am very satisfied with the outcome of this project, as it turned out better than expected and I gained additional knowledge about IoT. The [road map](https://github.com/Kevv999/IOT-PROJECT/blob/main/1DT305_Roadmap_Part_3.pdf) and the [GitHub link](https://github.com/iot-lnu/applied-iot) from the course 1DT305 were very helpful, as I frequently found myself referring back to the road map and GitHub throughout the project.

### Space for improvements
Something that could improve the project or could be done in another way is to add an I2C-interface to the project. Adding the I2C-interface would create more space and be better for cable management. The space would make it easier to add more sensors/components to the project and remove the overwhelming jump wires that could potentially make newcomers feel intimidated to re-create the project.

#### I2C-interface
| Component  | Where to buy | Price|
| ------------- | ------------- | ------------- |
| I2C-interace  | electrokit.com  | 39 SEK  |

*Figure 10:* I2C-interface 

<img src="https://github.com/Kevv999/IOT-PROJECT/assets/100692756/b62351aa-5182-4dfc-bca7-9e6875974977" alt="Image" width="200" height="200">
![image](https://github.com/Kevv999/IOT-PROJECT/assets/100692756/955c3e8e-c135-4c1f-8ab8-e476f432ffe5)


