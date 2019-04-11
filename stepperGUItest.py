#!/usr/bin/env python
from tkinter import *
from pirc522 import RFID
from pydub import AudioSegment
from pydub.playback import play
import serial
import time
port = "/dev/ttyACM0"
rdr = RFID()
root = Tk()
mainW=500
mainH=400
fmain = Frame(root,width=mainW,height=mainH)
fmain.grid(row=0,column=0,sticky='news')
root.title("Test")
root.geometry('500x400')
mainT = Label(fmain,text="RFID TO RUN",font=('Helvetica', 40, 'bold'))
mainT.place(relx=0.5, y=50,anchor=CENTER)

s1 = serial.Serial(port,9600)
s1.flushInput()


def runMotors():
    print("Motors Running1")
    inputValue=s1.readline()
    print(inputValue)
    n = str(1)
    n = n.encode()
    s1.write(n)
    print("Motors Running2")
def stopMotors():
    n = str(0)
    n = n.encode()
    s1.write(n)
    print("Motors Stopping")

def rfidCheck(i):
    time.sleep(2)
    print("waiting")
    rdr.wait_for_tag()
    (error, tag_type) = rdr.request()
    if not error:
        print("Tag detected")
        (error, uid) = rdr.anticoll()
        if not error:
          print("UID: " + str(uid))
          # Select Tag is required before Auth
          if not rdr.select_tag(uid):
            # Auth for block 10 (block 2 of sector 2) using default shipping key A
            if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
              # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
              print("Reading block 10: " + str(rdr.read(10)))
              # Always stop crypto1 when done working
              rdr.stop_crypto()
          if(i==0):
              print("run")
              return True
          elif(i==1):
              print("stop")
              return False
 
i=0
while True:
    print(i)
    root.update()
    if rfidCheck(i):
        song = AudioSegment.from_wav("jump.wav")
        song = song-5
        play(song)
        runMotors()
        i = 1
    elif not rfidCheck(i):
        stopMotors()
        i = 0
    
rdr.cleanup()