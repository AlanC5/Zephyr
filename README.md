# Zephyr
Smart Fan Prototype in Python3

## Installing Libraries (Make sure to install in same directory)
### Adafruit DHT11 Library (Temperature/Humditiy Sensor)
- git clone https://github.com/adafruit/Adafruit_Python_DHT.git
- cd Adafruit_Python_DHT
- sudo apt-get install build-essential python-dev
- sudo python3 setup.py install

## Run
- virtualenv venv
- source venv/bin/activate
- pip3 install -r requirements.txt
- python3 main.py

## pylint
pip install pylint
pylint {filename/directory}

