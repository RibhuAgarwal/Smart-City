import RPi.GPIO as GPIO
from gpiozero import *
from time import *
import time
import smtplib
import ssl

class garbage: 
    def __init__(self):
        
        smtp_p = 465
        smt_ser = "smtp.gmail.com"

        email_from = "ribhu8661@gmail.com"
        email_to = "ribhubhartiya@gmail.com"
        passkey = "bchrvgizaotqaqor"


        message = "Garbage is full"

        simple_email_context = ssl.create_default_context()
        GPIO.setmode(GPIO.BCM)
        GPIO_TRIGGER= 26
        GPIO_ECHO=22
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)


#function for counting distance
        def distance():
    #sending sound from ultra sonic sensor
            GPIO.output(GPIO_TRIGGER, True)
            time.sleep(0.00001)
            t_end = time.time() + 10*1
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
            
            while (time.time() < t_end):
        
                dist = (distance)/100
                #print(dist)
                if (dist<50):
                    try:
                        #print("Connecting..")
                        server= smtplib.SMTP_SSL(smt_ser, smtp_p,context =simple_email_context)
                        
                        server.login(email_from, passkey)
                        #print("Connection done")
                        
                        server.sendmail(email_from,email_to,message)
                        print("Email sent for garbage collection.")
                        time.sleep(10)
                    except Exception as e:
                        print(e)
        
        distance()


    

    




