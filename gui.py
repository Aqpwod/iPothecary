#imports
from tkinter import *
from pirc522 import RFID
from pydub import AudioSegment
from pydub.playback import play
import time
import digitalio
import board
import adafruit_matrixkeypad


#setup RFID
#rdr = RFID()

#setup keypad
cols = [digitalio.DigitalInOut(x) for x in (board.D26, board.D20, board.D21)]
rows = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13, board.D19)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
 

#all commands go here
def raise_frame(f):
    f.tkraise()
    #song = AudioSegment.from_wav("jump.wav")
    #song = song-10
    #play(song)

def scan():
    while True:
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
    # Calls GPIO cleanup
    rdr.cleanup()


root = Tk()
mainW=500
mainH=400
fmain = Frame(root,width=mainW,height=mainH)
fsettings = Frame(root,width=mainW,height=mainH)
fadd = Frame(root,width=mainW,height=mainH)
ftime = Frame(root,width=mainW,height=mainH)
ftest = Frame(root,width=mainW,height=mainH)
fsound = Frame(root,width=mainW,height=mainH)
fpills = Frame(root,width=mainW,height=mainH)

for frame in (fmain, fsettings, fadd, ftime, ftest,fsound,fpills):
    frame.grid(row=0,column=0,sticky='news')
    #frame.pack_propagate(0)
    
root.title("Test")
root.geometry('500x400')

#fpills stuff

#fmain stuff
mainT = Label(fmain,text="iPothecary",font=('Helvetica', 40, 'bold'))
mainT.place(relx=0.5, y=50,anchor=CENTER)

btn = Button(fmain, text="Settings", command=lambda:raise_frame(fsettings),font=('Helvetica', 10))
btn.place(relx=0.5, y=300,anchor=CENTER)
time1 = ''
clock = Label(fmain, font=('Helvetica', 40, 'bold'))
clock.place(relx=0.5, y=150,anchor=CENTER)
noticeT = Label(fmain,text= "Next pill time is at _ for _.",font=('Helvetica',15,'bold'))
noticeT.place(relx=0.5, y=100,anchor=CENTER)

pillB = Button(fmain, text="Pills",font=('Helvetica', 10))
pillB.place(relx= 0.2,y =300, anchor =CENTER)
newB = Button(fmain, text="+",command=lambda:raise_frame(fadd),font=('Helvetica', 10))
newB.place(relx= 0.8,y =300,anchor =CENTER)


#fadd stuff
addT = Label(fadd,text="Add User",font=('Helvetica', 30, 'bold'))
addT.place(relx=0.5, y=50,anchor=CENTER)

addButton = Button(fadd,text = "Add",font=('Helvetica', 15))
addButton.place(relx= 0.6, y=350,anchor=CENTER)
Bbtn = Button(fadd, text="Cancel", font=('Helvetica',15),command=lambda:raise_frame(fmain))
Bbtn.place(relx= 0.4, y=350,anchor=CENTER)

#fsettings stuff
l = Label(fsettings, text= "Settings",font=('Helvetica',20,'bold'))
l.pack(fill=X,pady=10)

btn1 = Button(fsettings, text="Set Time",font=('Helvetica',25),height=1,command=lambda:raise_frame(ftime))
btn1.pack(fill=X,pady=5)
btn2 = Button(fsettings, text="Sound",font=('Helvetica',25),height=1,command=lambda:raise_frame(fsound))
btn2.pack(fill=X,pady=5)
btn3 = Button(fsettings, text="Text",font=('Helvetica',25),height=1)
btn3.pack(fill=X,pady=5)
btn4 = Button(fsettings, text="Language",font=('Helvetica',25),height=1)
btn4.pack(fill=X,pady=5)
btn5 = Button(fsettings, text="Return", font=('Helvetica',25),height=1,command=lambda:raise_frame(fmain))
btn5.pack(pady=5)

#ftime stuff
lt = Label(ftime, text= "Set Time",font=('Helvetica',20,'bold'))
lt.grid(column=2,row=0)
txtHour = Entry(ftime,font=('Helvetica',40),width=5)
txtHour.grid(column=1,row=1,padx = 10)
colon = Label(ftime,text=" : ",font=('Helvetica',40,'bold'))
colon.grid(column=2,row=1)
txtMinute = Entry(ftime,font=('Helvetica',40),width=5)
txtMinute.grid(column=3,row=1)
btnS = Button(ftime, text = "Apply", font=('Helvetica',20,'bold'))
btnS.grid(column=1, row= 2)
btnBack = Button(ftime,text="Return",font=('Helvetica',20,'bold'),command=lambda:raise_frame(fsettings))
btnBack.grid(column=3,row=2)
#need an alert for the time being changed

#fsound stuff
ls = Label(fsound, text= "Sound",font=('Helvetica',20,'bold'))
ls.grid(column=2,row=0)
btnBackS = Button(fsound,text="return",font=('Helvetica',20,'bold'),command=lambda:raise_frame(fsettings))
btnBackS.grid(column=1,row=1)


def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
raise_frame(fmain)

root.mainloop(  )
