from humidity import * 
from multiprocessing import Process
from ultra_garbage import *
from firedetector import *
from GPTmotion import *
from Parking_test import *

from trafficLights import *
from readingDataFromOpenAi import *
      
#import tkinter as tk
#import subprocess
#ht = humidity()
tl = trafficLights()
gm = GPTmotion()
fs = flamedetector()

ug = garbage()
pk = parking()
#data = dataAI()

if __name__ == "__main__":
       
       #def on_button_click():    
    while(1):
       # process1 = Process(target = humidity)
        process2 = Process(target=trafficLights)
        process3 = Process(target = GPTmotion)
        process4 = Process(target = flamedetector)
       
        process5 = Process(target = garbage)
        process6 = Process(target = parking)
     #   process7 = Process(target = dataAI)
            
#         """root = tk.Tk()
#         root.title("Tkinter button click")
# 
#         button = tk.Button(root, text = "run External Script", command=on_button_click)
# 
#         button.pack()
#         root.mainloop()"""
        
        



    
