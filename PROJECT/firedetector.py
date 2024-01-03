import RPi.GPIO as GPIO
import time
import urllib.request as urllib2
from gpiozero import Buzzer

class flamedetector:
    def __init__(self):
        
        Pin = 21
        
        buzzer = Buzzer(20)
        
        myAPI = 'YULQKFZEJGS2J2LL'

        #readKey = 'K5EABMKHIXQI3IHG'

        baseURL = 'https://api.thingspeak.com/update?api_key=%s' %myAPI
        
        t_end = time.time() + 35*1
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        def detect_flame():
            
            if GPIO.input(Pin) == 0:
                return True
            else:
                return False

        try:
            while (time.time() < t_end):
                if detect_flame():
                    print("Flame detected!!!")
                    buzzer.on()
                    conn = urllib2.urlopen(baseURL + '&field6=%s'% (2))
                    #print(conn.read())
                    conn.close()
                else:
                    print("No flames detected!")
                    conn = urllib2.urlopen(baseURL + '&field6=%s' %(0))
                    #print(conn.read())
                    conn.close()
                time.sleep(5)
            buzzer.off()
            
        except KeyboardInterrupt:
            GPIO.cleanup()
        detect_flame()

