//temperature sensor with raspberry pi 

import Adafruit_DHT 
import time 
  
DHT_SENSOR = Adafruit_DHT.DHT11 
DHT_PIN = 4 
  
while True: 
    temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) 
    if temperature is not None: 
        print("Temprature = ".format(temperature, humidity)) 
    else: 
        print("Sensor failure. Check wiring."); 
    time.sleep(3); 
