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
