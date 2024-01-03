import RPi.GPIO as GPIO
import sys
import urllib.request as urllib2
import Adafruit_DHT
import time

class humidity:
    def __init__(self):
        #api key
        myAPI = 'YULQKFZEJGS2J2LL'

        #readKey = 'K5EABMKHIXQI3IHG'

        baseURL = 'https://api.thingspeak.com/update?api_key=%s' %myAPI 
        t_end = time.time() + 20*1

        dht_sensor= Adafruit_DHT.DHT11
        dht_pin=4

        def dht11_data():
            humidity, temperature =Adafruit_DHT.read_retry(dht_sensor, dht_pin)
            return humidity, temperature


        while (time.time() < t_end):
            try:
                humidity, temperature = dht11_data()
            
                if isinstance(humidity, float) and isinstance(temperature, float):
                    humidity = '%.2f' % humidity
                    temperature = '%.2f' % temperature
                    
                    conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temperature, humidity))
                    print(conn.read())
                    
                    conn.close()
                else:  
                    print('Running...')
            

                
            except Exception as E:
                print(E)
        dht11_data()
c = humidity()

