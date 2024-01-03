import RPi.GPIO as gpio
import time
from gpiozero import MotionSensor as mws
from datetime import datetime as t
import pytz
from gpiozero import TrafficLights

class trafficLights:
    def __init__(self):
        easter= pytz.timezone('Canada/Pacific')
        currtime=t.now(easter)

        after = (currtime.hour>=14)

        t_end = time.time() + 10*1

        gpio.setmode(gpio.BCM)
        light = TrafficLights(25,8,7)

        pirpin=14
        gpio.setwarnings(False)
        gpio.setup(25,gpio.OUT)
        gpio.setup(8,gpio.OUT)
        gpio.setup(7,gpio.OUT)

        gpio.setup(pirpin, gpio.IN)

        def lights(pirpin):
            print("Pedestrian detected")
            print("Lights on")
            light.green.off()
            light.amber.on()
            time.sleep(1)
            light.amber.off()
            light.red.on()
            time.sleep(3)
            light.red.off()
            light.green.on()

            
          

        print("Motion sensored alarmed")


        print("ready")

        try:
            if (after):
                light.green.on()
            
            
                gpio.add_event_detect(pirpin,gpio.RISING, callback=lights)
                light.green.on()
                while (time.time() < t_end):
                    time.sleep(5)
        except KeyboardInterrupt:
            print("Quit")
            gpio.cleanup()
        lights(pirpin)
#tl = trafficLights()