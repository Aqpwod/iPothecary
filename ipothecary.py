import guizero as gui
import datetime
import RPi.GPIO as GPIO
import time as t
import keyboard

#def pushbuttom():

def pilltime():
    pilltxt.value = "Time for pills" 
    
    
def updatetime():
    now = datetime.datetime.now()
    timetxt.value = now.strftime("%H:%M:%S")
    
app = gui.App(title="iPothecary", width=300, height=200, layout="grid")

words = gui.Text(app, text="iPothecary",grid=[0,0],align="left")
timetxt = gui.Text(app, text = "00:00:00",grid=[0,1],size = 40,align="left")
timetxt.repeat(1000,updatetime)
pilltxt = gui.Text(app, text="Not time for pills yet.",grid=[0,2],align="left")

app.display()
