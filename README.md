# Robot Barkeeper

Robot Barkeeper is an IoT project powered by Raspberry Pi 4 and built with Django Framework. Therefore it is monolithic and follows the Model-View-Controller coding pattern. HTTP is the project's communication protocol so it is based on response-request communication between the client and server. This repository is meant for beginners in the IoT field and is not recommended for scaling.

## Hardware Requirements
The hardware requirements depend on your learning goals.

Overall
1. Raspberry Pi 4
2. SD Card
2. Raspberry Pi4 accessories found [here](https://magpi.raspberrypi.com/articles/set-up-raspberry-pi-4)

Robot App
1. Raspberry Pi 4
2. MG996R servo motors - 15kg torque x 3
3. Micro Servos x 2
4. 5-DOF robotic arm model
5. Breadboard Power Supply Module 5V MB102

Load Cell
5. Single Point Load Cell
6. HX711 Load Cell Amplifier

Camera App
6. Raspberry Pi Camera Module 2

## Set-Up Instructions
1. Install Raspbian OS in the microcontroller
2. Follow the circuit diagram
3. Clone this repository
4. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements

```bash
pip install - r requirements.txt
```
5. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements

```bash
cd django-iot
```

```bash
python3 manage.py runserver
```

## Software and Apps Overview

Project folder overview:

```
./barkeeper/
./barkeeper/api/ # REST API design implemntation found here
./barkeeper/api/serializers.py
./barkeeper/api/viewsets.py
./barkeeper/api/pagination.py
./barkeeper/api/urls.py

./barkeeper/models.py #the data being stored by the app
./barkeeper/utils.py  #forward and inverse kinematics solver found here
./barkeeper/views.py  #web request and return found here
./barkeeper/tests.py

./camera/           #this submodule is for testing the camera
./camera/api
./camera/utils.py   #camera functions found here
./camera/views.py.  #web request and return found here

./iot               #this is the main project folder

./loadcell          #this submodule is for testing weight sensor
./robot/utils.py    #load cell functions here
./robot/views.py.   #web request and return found here

./robot             #this submodule is for testing each motor
./robot/utils.py    #motor functions found here
./robot/views.py.   #web request and return found here

```

## Resources:
* To be added

## License
[MIT](https://choosealicense.com/licenses/mit/)
