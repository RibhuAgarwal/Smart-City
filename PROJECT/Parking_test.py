from Adafruit_IO import *
import RPi.GPIO as GPIO
from gpiozero import *
from time import *
import time
import urllib.request as urllib2
import ssl


class parking:
    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        GPIO_TRIGGER= 23
        GPIO_ECHO=18
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
         
        myAPI = 'YULQKFZEJGS2J2LL'

                #readKey = 'K5EABMKHIXQI3IHG'

        baseURL = 'https://api.thingspeak.com/update?api_key=%s' %myAPI

        #function for counting distance
        def distance():
            #sending sound from ultra sonic sensor
            GPIO.output(GPIO_TRIGGER, True)
            time.sleep(0.00001)
            
            t_end = time.time() + 40*1
            
            #stopping from sending sound from ultra sonic sensor
            GPIO.output(GPIO_TRIGGER, False)
            StartTime=time.time()
            StopTime= time.time()
            
            #getting start time 
            while GPIO.input(GPIO_ECHO)==0:
                StartTime=time.time()
            
            #getting end time
            while GPIO.input(GPIO_ECHO)==1:
                StopTime=time.time()
                
            #calculating elapsed time
            TimeElapsed=(StopTime-StartTime)
            
            #claculating distance with elapsed time
            distance= (TimeElapsed*34300)/2
            
            print("Findind a parking spot")
            try:
                while (time.time() < t_end):
                    spot_available = False
                    dist = (distance)/100
                    #print(dist)
                    if (dist<1.5):
                           print("Spot unavailable")
                           print("Rechecking!!")
                           conn = urllib2.urlopen(baseURL + '&field7=%s'% (0))
                           #print(conn.read())
                           conn.close()
                           if(not spot_available):
                               time.sleep(3)
                        #except Exception as e:
                            #print(e)
                    else:
                        print("Spot available.")
                        conn = urllib2.urlopen(baseURL + '&field7=%s'% (1))
#                         print(conn.read())
                        conn.close()
                    time.sleep(7)
            except KeyboardInterrupt:
                print("Measurement stop by user")
                GPIO.cleanup()
        distance()
#SP = parking()
    
            

    
        

