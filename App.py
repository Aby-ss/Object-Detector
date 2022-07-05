from tkinter import *
from tkinter import ttk
from Live_Detection import start

def detect():
    start()

window = Tk()

button1 = Button(window, text = 'Live Video Capture', command = detect)
button1.pack(side = RIGHT)

window.mainloop()

