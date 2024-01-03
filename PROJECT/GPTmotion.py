import RPi.GPIO as gpio
import time
from datetime import datetime as t
import pytz


class GPTmotion:
    def __init__(self):
        easter= pytz.timezone('Canada/Pacific')
        currtime=t.now(easter)

        after = (currtime.hour>=17)

        t_end = time.time() + 10*1;

        gpio.setmode(gpio.BCM)
        led= 2
        pirpin=15
        gpio.setwarnings(False)
        gpio.setup(led,gpio.OUT)

        gpio.setup(pirpin, gpio.IN)

        def lights(pirpin):
            print("Motion detected")
            print("Lights on")
            gpio.output(led,gpio.HIGH)
         
            time.sleep(3)
            
            print("Light off")
            gpio.output(led,gpio.LOW)

        print("Motion sensored alarmed")


        print("ready")

        try:
            if (after):
                gpio.add_event_detect(pirpin,gpio.RISING, callback=lights)
                while(time.time()< t_end):
                #while 1:
                    time.sleep(1)
        except KeyboardInterrupt:
            print("Quit")
            
            gpio.cleanup()
        lights(pirpin)


