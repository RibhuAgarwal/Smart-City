import tkinter as tk
import subprocess

def on_button_click():
    subprocess.run(["python", "Integrated.py"])
    
root = tk.Tk()
root.title("Tkinter button click")

button = tk.Button(root, text = "run External Script", command=on_button_click)

button.pack()
root.mainloop()
