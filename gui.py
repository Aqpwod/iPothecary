#imports
from tkinter import *
import MySQLdb
from tkinter import ttk
from tkinter import font
from pirc522 import RFID
from pydub import AudioSegment
from pydub.playback import play
import time
import digitalio
import board
import adafruit_matrixkeypad

#setup mysql
db = MySQLdb.connect(host="localhost",  # your host 
                     user="cory",       # username
                     passwd="ipothecary",     # password
                     db="pills")   # name of the database
cur = db.cursor()


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
    #song = AudioSegment.from_wav("test.mp3")
    #song = song-10
    #play(song)
def playSound(event):
    #print(vol)
    song = AudioSegment.from_wav("jump.wav")
    #song = song+vol 
    play(song)

def addUser(name,rfid,age):
    cur.execute("INSERT INTO users (name,RFID,age) VALUES (%s,%s,%s)",
            (name,rfid,age)) #DayOfWeekHourMinute
    db.commit()

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
fadd1 = Frame(root,width=mainW,height=mainH)
fadd2 = Frame(root,width=mainW,height=mainH)
fadd3 = Frame(root,width=mainW,height=mainH)
ftime = Frame(root,width=mainW,height=mainH)
ftest = Frame(root,width=mainW,height=mainH)
fsound = Frame(root,width=mainW,height=mainH)
ftext = Frame(root,width=mainW,height=mainH)
flanguage = Frame(root,width=mainW,height=mainH)
fpills = Frame(root,width=mainW,height=mainH)

for frame in (fmain, fsettings, fadd, fadd1,fadd2,fadd3 ftime, ftest,fsound,fpills,flanguage,ftext):
    frame.grid(row=0,column=0,sticky='news')
    #frame.pack_propagate(0)
    
root.title("Test")
root.geometry('500x400')
bigfont = font.Font(family="Helvetica",size=20)
root.option_add("*TCombobox*Listbox*Font",bigfont)

#fpills stuff
pillT = Label(fpills,text="All Pills",font=('Helvetica', 30, 'bold'))
pillT.place(relx=0.5, y=50,anchor=CENTER)
Pbtn = Button(fpills, text="Cancel", font=('Helvetica',15),command=lambda:raise_frame(fmain))
Pbtn.place(relx= 0.5, y=350,anchor=CENTER)


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

pillB = Button(fmain, text="Pills",command=lambda:raise_frame(fpills),font=('Helvetica', 10))
pillB.place(relx= 0.2,y =300, anchor =CENTER)
newB = Button(fmain, text="+",command=lambda:raise_frame(fadd),font=('Helvetica', 10))
newB.place(relx= 0.8,y =300,anchor =CENTER)


#fadd stuff
addT = Label(fadd,text="Add User",font=('Helvetica', 30, 'bold'))
addT.place(relx=0.5, y=50,anchor=CENTER)

nameText = Entry(fadd,width=10, font=('Helvetica', 20))
nameText.place(relx = 0.2,y=150,anchor=CENTER)

rfidText = Entry(fadd,width=10, font=('Helvetica', 20))
rfidText.place(relx = 0.4,y=150,anchor=CENTER)
ageText = Entry(fadd,width=10, font=('Helvetica', 20))
ageText.place(relx = 0.6,y=150,anchor=CENTER)

addButton = Button(fadd,text = "Add",font=('Helvetica', 20),command=lambda:addUser(nameText.get(),rfidText.get(),ageText.get()))
addButton.place(relx= 0.8, y=300,anchor=CENTER)
Bbtn = Button(fadd, text="Cancel", font=('Helvetica',20),command=lambda:raise_frame(fmain))
Bbtn.place(relx= 0.2, y=300,anchor=CENTER)

#fadd1 stuff
addT = Label(fadd1,text="Name",font=('Helvetica', 30, 'bold'))
addT.place(relx=0.5, y=50,anchor=CENTER)

nameText = Entry(fadd1,width=20, font=('Helvetica', 20))
nameText.place(relx = 0.5,y=100,anchor=CENTER)
addButton = Button(fadd1,text = "Next",font=('Helvetica', 20),)
addButton.place(relx= 0.8, y=300,anchor=CENTER)

#fadd2 stuff
addT = Label(fadd2,text="Age",font=('Helvetica', 30, 'bold'))
addT.place(relx=0.5, y=50,anchor=CENTER)

nameText = Entry(fadd2,width=4, font=('Helvetica', 20))
nameText.place(relx = 0.5,y=100,anchor=CENTER)
addButton = Button(fadd2,text = "Next",font=('Helvetica', 20),)
addButton.place(relx= 0.8, y=300,anchor=CENTER)

#fadd3 stuff
addT = Label(fadd3,text="Scan RFID",font=('Helvetica', 30, 'bold'))
addT.place(relx=0.5, y=50,anchor=CENTER)

succT = Label(fadd3,text="",font=('Helvetica', 30, 'bold'))
succT.place(relx=0.5, y=200,anchor=CENTER)
finButton = Button(fadd2,text = "Finish",font=('Helvetica', 20),)
finButton.place(relx= 0.8, y=300,anchor=CENTER)

#fsettings stuff
l = Label(fsettings, text= "Settings",font=('Helvetica',20,'bold'))
l.pack(fill=X,pady=10)

btn1 = Button(fsettings, text="Set Time",font=('Helvetica',25),height=1,command=lambda:raise_frame(ftime))
btn1.pack(fill=X,pady=5)
btn2 = Button(fsettings, text="Sound",font=('Helvetica',25),height=1,command=lambda:raise_frame(fsound))
btn2.pack(fill=X,pady=5)
btn3 = Button(fsettings, text="Text",font=('Helvetica',25),height=1,command=lambda:raise_frame(ftext))
btn3.pack(fill=X,pady=5)
btn4 = Button(fsettings, text="Language",font=('Helvetica',25),height=1,command=lambda:raise_frame(flanguage))
btn4.pack(fill=X,pady=5)
btn5 = Button(fsettings, text="Return", font=('Helvetica',25),height=1,command=lambda:raise_frame(fmain))
btn5.pack(pady=5)

#ftime stuff
comboH = ttk.Combobox(ftime, values = ["01","02","03","04","05","06","07","08","09","10","11","12"],font=('Helvetica',40),width=3)
comboH.place(relx=0.2, y=120,anchor=CENTER)
comboM = ttk.Combobox(ftime, values = ["00","15","30","45"],font=('Helvetica',40),width=3)
comboM.place(relx=0.5, y=120,anchor=CENTER)
comboAP = ttk.Combobox(ftime, values = ["AM","PM"],font=('Helvetica',40),width=3)
comboAP.place(relx=0.75, y=120,anchor=CENTER)
lt = Label(ftime, text= "Set Time",font=('Helvetica',40,'bold'))
lt.place(relx=0.5, y=50,anchor=CENTER)
colon = Label(ftime,text=" : ",font=('Helvetica',40,'bold'))
colon.place(relx=0.35, y=120,anchor=CENTER)
btnS = Button(ftime, text = "Apply", font=('Helvetica',20,'bold'))
btnS.place(relx=0.2, y=250,anchor=CENTER)
btnBack = Button(ftime,text="Return",font=('Helvetica',20,'bold'),command=lambda:raise_frame(fsettings))
btnBack.place(relx=0.8, y=250,anchor=CENTER)
#need an alert for the time being changed

#fsound stuff
ls = Label(fsound, text= "Sound",font=('Helvetica',40,'bold'))
ls.place(relx= 0.5, y=50,anchor=CENTER)
btnBackS = Button(fsound,text="Return",font=('Helvetica',20,'bold'),command=lambda:raise_frame(fsettings))
btnBackS.place(relx= 0.5, y=250,anchor=CENTER)
sScale = Scale(fsound,from_=0, to=100,orient=HORIZONTAL,width = 30)
sScale.place(relx=0.5,y=150,anchor=CENTER)
sScale.bind("<ButtonRelease-1>",playSound)


#ftext stuff
lt = Label(ftext, text= "Text",font=('Helvetica',40,'bold'))
lt.place(relx= 0.5, y=50,anchor=CENTER)
btnBackS = Button(ftext,text="return",font=('Helvetica',20,'bold'),command=lambda:raise_frame(fsettings))
btnBackS.place(relx= 0.5, y=350,anchor=CENTER)

#flanguage stuff
ll = Label(flanguage, text= "Language",font=('Helvetica',40,'bold'))
ll.place(relx= 0.5, y=50,anchor=CENTER)
btnBackS = Button(flanguage,text="return",font=('Helvetica',20,'bold'),command=lambda:raise_frame(fsettings))
btnBackS.place(relx= 0.5, y=350,anchor=CENTER)

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
    
def keypress():
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    
    if keys == [0]:
        raise_frame(fsettings)
    else:
        fmain.after(200,keypress)


tick()
#keypress()
raise_frame(fmain)

root.mainloop(  )
