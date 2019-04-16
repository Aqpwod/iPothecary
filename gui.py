#imports
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

from tkinter import *
import os
import MySQLdb
from tkinter import ttk
from tkinter import font

from PIL import Image,ImageTk
from pirc522 import RFID
from pydub import AudioSegment
from pydub.playback import play
import time

#setup mysql
db = MySQLdb.connect(host="localhost",  # your host 
                     user="cory",       # username
                     passwd="ipothecary",     # password
                     db="pills")   # name of the database
cur = db.cursor()

#setup RFID
rdr = RFID()

#setup keypad

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
    if name and rfid and age:
        cur.execute("INSERT INTO users (name,RFID,age) VALUES (%s,%s,%s)",
            (name,rfid,age)) #DayOfWeekHourMinute
        db.commit()
        
def findD():
    rows = cur.execute("SELECT * FROM Table_name")
    
        
def rfidScan(widget,scanOn):
    print("Hi")
    scanCode = ""
    while scanCode == "" and scanOn:
        print("waiting")
        rdr.wait_for_tag()
        (error, tag_type) = rdr.request()
        if not error:
            print("Tag detected")
            (error, uid) = rdr.anticoll()
            if not error:
                print("UID: " + str(uid))
                scanCode=str(uid)
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
    widget.configure(text="Success!")
    return str(uid)
    
def keyboard(frame,widget):
    keys = ["q","w","e","r","t","y","u","i","o","p",
            "a","s","d","f","g","h","j","k","l",":",
            "z","x","c","v","b","n","m",",",".","Back"]
    k=0
    kbtn = [[0 for x in range(10)] for x in range(10)]
    for y in range(0,3):
        for x in range(0,10):
            kbtn[x][y] = ttk.Button(frame, text=keys[k],compound="top",command=lambda k=k:insertText(keys[k],widget),width=4,style='TButton')
            kbtn[x][y].grid(row=y+2,column=x,pady=5)
            if k!=29:
                k=k+1


def keypad(frame,widget):
    keys = ["1","2","3","4","5","6","7","8","9","-","0","Back"]
    k=0
    kbtn = [[0 for x in range(4)] for x in range(4)]
    for y in range(0,4):
        for x in range(0,3):
            kbtn[x][y] = ttk.Button(frame, text=keys[k],compound="top",command=lambda k=k:insertText(keys[k],widget),width=6,style='TButton')
            kbtn[x][y].grid(row=y+2,column=x+1,pady=10)
            print(k)
            if k!=11:
                k=k+1
                
                
def insertText(key,widget):
    prevText = widget.get()
    if key == "Back" and prevText:
        widget.delete(len(prevText)-1,len(prevText))
    elif key != "Back"and len(prevText) != 10:
        widget.insert(END,key.upper())          
    
        
        
def cText(size):
    ft = "helvetica " + str(size)
    s = ttk.Style()
    s.configure('TButton',font=ft)
    d = ttk.Style()
    d.configure('TLabel', font=ft)
    
    


def pillFrames(x,y):
    containerT.configure(text="Container " +str(x)+" "+str(y))
    raise_frame(fcont)

root = Tk()
root.wm_attributes('-type','splash')

mainW=1300
mainH=775
fmain = Frame(root,width=mainW,height=mainH)
fsettings = Frame(root,width=mainW,height=mainH)
fadd = Frame(root,width=mainW,height=mainH)
fadd1 = Frame(root,width=mainW,height=mainH)
fabout = Frame(root,width=mainW,height=mainH)
fadd2 = Frame(root,width=mainW,height=mainH)
fadd3 = Frame(root,width=mainW,height=mainH)
fadd35 = Frame(root,width=mainW,height=mainH)
fadd4 = Frame(root,width=mainW,height=mainH)
ftime = Frame(root,width=mainW,height=mainH)
fusers = Frame(root,width=mainW,height=mainH)
fPillTime = Frame(root,width=mainW,height=mainH)
ftest = Frame(root,width=mainW,height=mainH)
fsound = Frame(root,width=mainW,height=mainH)
ftext = Frame(root,width=mainW,height=mainH)
flanguage = Frame(root,width=mainW,height=mainH)
fpills = Frame(root,width=mainW,height=mainH)
fcont= Frame(root,width=mainW,height=mainH)

#STYLES
s = ttk.Style()
s.configure('TButton',foreground="white",activebackground="#4286f4",background="#4286f4",font='helvetica 25',relief='flat')
d = ttk.Style()
d.configure('TLabel', background="#595959",foreground="white",font='helvetica 25')


#Create Frames
for frame in (fmain, fsettings, fadd, fadd1,fadd2,fadd3, fadd35, fadd4, ftime, ftest,fsound, fPillTime,
              fpills,fabout,flanguage,ftext,fusers,fcont):
    frame.grid(row=0,column=0,sticky='news')
    frame.configure(bg="#595959")
    frame.configure(cursor="none")
    #frame.pack_propagate(0)
fsettings.columnconfigure(0,weight=1)
fsettings.columnconfigure(1,weight=1)
fsettings.columnconfigure(2,weight=1)

for col in range(0,10):
    fadd1.columnconfigure(col,weight=1)

for col in range(0,5):
    fadd2.columnconfigure(col,weight=1)

root.title("Test")
root.geometry('1300x775')
bigfont = font.Font(family="Helvetica",size=20)
root.option_add("*TCombobox*Listbox*Font",bigfont)

#fpills stuff
fpills.columnconfigure(0,weight=1)
fpills.columnconfigure(1,weight=1)
fpills.columnconfigure(2,weight=1)

imW = int(mainW/8)
imH = int(mainH/5)
contI = Image.open("cont.png")
imageA = contI.resize((imW,imH),Image.ANTIALIAS)
contImage = ImageTk.PhotoImage(imageA)

pillT = ttk.Label(fpills,text="All Pills",style='TLabel')
pillT.grid(row=0,column=1)


pbtn = [[0 for x in range(5)] for x in range(5)]
for x in range(0,3):
    for y in range(1,4):
        pbtn[x][y] = ttk.Button(fpills, text=str(x)+","+str(y),image=contImage,compound="top",command=lambda x=x, y=y: pillFrames(x,y),style='TButton')
        pbtn[x][y].grid(row=y,column=x,pady=2)

        
Pbtn = ttk.Button(fpills, text="Cancel", style='TButton',command=lambda:raise_frame(fmain))
Pbtn.grid(row=4,column=1,pady=10)


#fmain stuff
addI = Image.open("add.png")
imageS = addI.resize((150,150),Image.ANTIALIAS)
addImage = ImageTk.PhotoImage(imageS)

pillsI = Image.open("pills.png")
imageS = pillsI.resize((150,150),Image.ANTIALIAS)
pillsImage = ImageTk.PhotoImage(imageS)

pillI = Image.open("pill.png")
imageS = pillI.resize((150,150),Image.ANTIALIAS)
pillImage = ImageTk.PhotoImage(imageS)

mainT = Label(fmain,text="iPothecary",font=('Helvetica', 60),bg="#595959",fg="white")
mainT.place(relx=0.5, y=30,anchor=CENTER)

pillGet = ttk.Button(fmain, style='TButton',text="PILL TIME",image=pillsImage,compound="top",command=lambda:raise_frame(fPillTime))
pillGet.place(relx= 0.5,y=400, anchor =CENTER)
#pillGet.place_forget()

time1 = ''
clock = Label(fmain, font=('Helvetica', 50),bg="#595959",fg="white")
clock.place(relx=0.5, y=195,anchor=CENTER)
noticeT = ttk.Label(fmain,style='TLabel',text= "Next pill time is at _ for _.")
noticeT.place(relx=0.5, y=135,anchor=CENTER)

pillB = ttk.Button(fmain, style='TButton',text="Pills",image=pillImage,compound="top",command=lambda:raise_frame(fpills))
pillB.place(relx= 0.2,y =400, anchor =CENTER)
newB = ttk.Button(fmain, style='TButton',text="Settings",image=addImage,compound="top",command=lambda:raise_frame(fsettings))
newB.place(relx= 0.8,y =400,anchor =CENTER)


#fcont Stuff
containerT = ttk.Label(fcont,text="Container ",style='TLabel')
containerT.place(relx=0.5, y=50,anchor=CENTER)

noticeT = ttk.Label(fcont,style='TLabel',text= "Pills and crap")
noticeT.place(relx=0.5, y=125,anchor=CENTER)

Backbtn = ttk.Button(fcont, text="Back", style='TButton',command=lambda:raise_frame(fmain))
Backbtn.place(relx= 0.2, y=300,anchor=CENTER)
    

#fPillTime Stuff
addT = ttk.Label(fPillTime,text="Pill Time!",style='TLabel')
addT.place(relx=0.5, y=50,anchor=CENTER)

noticeT = ttk.Label(fPillTime,style='TLabel',text= "Pills for User")
noticeT.place(relx=0.5, y=125,anchor=CENTER)

addButton = ttk.Button(fPillTime,text = "Confirm",style='TButton')
addButton.place(relx= 0.5, y=300,anchor=CENTER)

#Another screen for RFID CONFIRMATION
#Another screen for dispensing
#addT = Label(fPillTime1,text="Please Scan RFID",font=('Helvetica', 50),fg="white")


#fadd stuff
addT = ttk.Label(fadd,text="Add User",style='TLabel')
addT.place(relx=0.5, y=50,anchor=CENTER)

addButton = ttk.Button(fadd,text = "Add",style='TButton',command=lambda:addUser(nameText.get(),rfidText.get(),ageText.get()))
addButton.place(relx= 0.8, y=300,anchor=CENTER)
Bbtn = ttk.Button(fadd, text="Cancel", style='TButton',command=lambda:raise_frame(fmain))
Bbtn.place(relx= 0.2, y=300,anchor=CENTER)

#fusers
la = ttk.Label(fusers, text= "Users",style='TLabel')
la.place(relx=0.5, y=50,anchor=CENTER)

btnAdd = ttk.Button(fusers,text="Add User",style='TButton',command=lambda:raise_frame(fadd1))
btnAdd.place(relx=0.5, y=150,anchor=CENTER)
btnBack = ttk.Button(fusers,text="Return",style='TButton',command=lambda:raise_frame(fsettings))
btnBack.place(relx=0.8, y=450,anchor=CENTER)

#fadd1 stuff
addT = ttk.Label(fadd1,text="Name",style='TLabel')
addT.grid(row=0,column=4,columnspan=3,pady=5)

nameText = Entry(fadd1,width=10, font=('Helvetica', 30))
nameText.grid(row=1,column=4,columnspan=3,sticky=W)

keyboard(fadd1,nameText)
Cbtn = ttk.Button(fadd1, text="Cancel", style='TButton',command=lambda:raise_frame(fsettings))
Cbtn.grid(row=5,column=2,pady=5,columnspan=3)
addButton = ttk.Button(fadd1,text = "Next",style='TButton',command=lambda:raise_frame(fadd2))
addButton.grid(row=5,column=5,pady=5,columnspan=3)


#fadd2 stuff
addT = ttk.Label(fadd2,text="Date of Birth",style='TLabel')
addT.grid(row=0,column=2,pady=5)
dobText = Entry(fadd2,width=10, font=('Helvetica', 30))
dobText.grid(row=1,column=2)

keypad(fadd2,dobText)

Cbtn = ttk.Button(fadd2, text="Cancel", style='TButton',command=lambda:raise_frame(fsettings))
Cbtn.grid(row=6,column=1,pady=30)
addButton = ttk.Button(fadd2,text = "Next",style='TButton',command=lambda:raise_frame(fadd35))
addButton.grid(row=6,column=3,pady=30)

#fadd35 stuff
addT = ttk.Label(fadd35,text="Allergies?",style='TLabel')
addT.place(relx=0.5, y=50,anchor=CENTER)
amo=IntVar()
amp=IntVar()
asp=IntVar()
ibu=IntVar()
ins=IntVar()

Checkbutton(fadd35,text="Amoxicillin",variable=amo).place(relx=0.2, y=100,anchor=CENTER)
Checkbutton(fadd35,text="Ampicillin",variable=amp).place(relx=0.2, y=150,anchor=CENTER)
Checkbutton(fadd35,text="Aspirin",variable=asp).place(relx=0.2, y=200,anchor=CENTER)
Checkbutton(fadd35,text="Ibuprofen",variable=ibu).place(relx=0.2, y=250,anchor=CENTER)
Checkbutton(fadd35,text="Insulin",variable=ins).place(relx=0.2, y=300,anchor=CENTER)

addButton = ttk.Button(fadd35,text = "Next",style='TButton',command=lambda:raise_frame(fadd3))
addButton.place(relx=0.5, y=400,anchor=CENTER)

#fadd3 stuff
addT = ttk.Label(fadd3,text="Scan RFID",style='TLabel')
addT.place(relx=0.5, y=50,anchor=CENTER)

RFIDT = ttk.Label(fadd3,text="Please scan your RFID Chip now!",style='TLabel')
RFIDT.place(relx=0.5, y=150,anchor=CENTER)

succT = ttk.Label(fadd3,text="",style='TLabel')
succT.place(relx=0.5, y=275,anchor=CENTER)

finButton = ttk.Button(fadd3,text = "Finish",style='TButton',command=lambda:raise_frame(fadd4))
finButton.place(relx= 0.8, y=350,anchor=CENTER)

scanB = ttk.Button(fadd3,text = "SCAN",style='TButton',command=lambda:rfidScan(succT,True))
scanB.place(relx=0.5, y=200,anchor=CENTER)




#fadd4 stuff
cText = ttk.Label(fadd4,text="Confirm Information",style='TLabel')
cText.place(relx=0.5, y=50,anchor=CENTER)

name = "Name: " +nameText.get()
dob = "Date of Birth: " +dobText.get()

nT = ttk.Label(fadd4,text=name,style='TLabel')
nT.place(relx=0.5, y=125,anchor=CENTER)
dobT = ttk.Label(fadd4,text=dob,style='TLabel')
dobT.place(relx=0.5, y=175,anchor=CENTER)

finButton = ttk.Button(fadd4,text = "Finish",style='TButton')
finButton.place(relx= 0.8, y=350,anchor=CENTER)


#fsettings stuff
l = ttk.Label(fsettings, text= "Settings",style='TLabel')
l.grid(row=0,column=1,pady=10)

imW = int(mainW/8)
imH = int(mainH/4.5)

timeI = Image.open("clock.png")
imageT = timeI.resize((imW,imH),Image.ANTIALIAS)
timeImage = ImageTk.PhotoImage(imageT)

aboutI = Image.open("about.png")
imageA = aboutI.resize((imW,imH),Image.ANTIALIAS)
aboutImage = ImageTk.PhotoImage(imageA)

langI = Image.open("lang.png")
imageL = langI.resize((imW,imH),Image.ANTIALIAS)
langImage = ImageTk.PhotoImage(imageL)

soundI = Image.open("sound.png")
imageS = soundI.resize((imW,imH),Image.ANTIALIAS)
soundImage = ImageTk.PhotoImage(imageS)

usersI = Image.open("users.png")
imageU = usersI.resize((imW,imH),Image.ANTIALIAS)
usersImage = ImageTk.PhotoImage(imageU)

textI = Image.open("text.png")
imageT = textI.resize((imW,imH),Image.ANTIALIAS)
textImage = ImageTk.PhotoImage(imageT)

btn1 = ttk.Button(fsettings, text="Set Time",image=timeImage,compound="top",style='TButton',command=lambda:raise_frame(ftime))
btn1.grid(row=1,column=0,pady=5)
btn2 = ttk.Button(fsettings, text="Sound",image=soundImage,compound="top",style='TButton',command=lambda:raise_frame(fsound))
btn2.grid(row=1,column=1,pady=5)
btn3 = ttk.Button(fsettings, text="Text",image=textImage,compound="top",style='TButton',command=lambda:raise_frame(ftext))
btn3.grid(row=1,column=2,pady=5)
btn4 = ttk.Button(fsettings, text="Language",image=langImage,compound="top",style='TButton',command=lambda:raise_frame(flanguage))
btn4.grid(row=2,column=0,pady=5)
btn5 = ttk.Button(fsettings, text="Users", image=usersImage,compound="top",style='TButton',command=lambda:raise_frame(fusers))
btn5.grid(row=2,column=1,pady=5)
btn6 = ttk.Button(fsettings, text="About", image=aboutImage,compound="top",style='TButton',command=lambda:raise_frame(fabout))
btn6.grid(row=2,column=2,pady=5)
btn7 = ttk.Button(fsettings,text="Return", style='TButton',command=lambda:raise_frame(fmain))
btn7.grid(row=3,column=1,pady=30)


#fabout stuff
la = ttk.Label(fabout, text= "About",style='TLabel')
la.place(relx=0.5, y=50,anchor=CENTER)

la = ttk.Label(fabout, text= "iPothecary",style='TLabel')
la.place(relx=0.5, y=100,anchor=CENTER)
la1 = ttk.Label(fabout, text= "Created By:",style='TLabel')
la1.place(relx=0.5, y=200,anchor=CENTER)
la2 = ttk.Label(fabout, text= "Christian Puerta, Cory Ye",style='TLabel')
la2.place(relx=0.5, y=250,anchor=CENTER)
la3 = ttk.Label(fabout, text= "Elijah Shultz and Yeil Choi",style='TLabel')
la3.place(relx=0.5, y=300,anchor=CENTER)
la3 = ttk.Label(fabout, text= "For Senior Design 2018-2019",style='TLabel')
la3.place(relx=0.5, y=350,anchor=CENTER)
btnBack = ttk.Button(fabout,text="Return",style='TButton',command=lambda:raise_frame(fsettings))
btnBack.place(relx=0.8, y=450,anchor=CENTER)


#ftime stuff
comboH = ttk.Combobox(ftime, values = ["Hawaii","Alaska","Pacific","Mountain","Central","Eastern"],font=('Helvetica',40),width=8)
comboH.place(relx=0.5, y=120,anchor=CENTER)
lt = ttk.Label(ftime, text= "Set Time",style='TLabel')
lt.place(relx=0.5, y=50,anchor=CENTER)

btnBack = ttk.Button(ftime,text="Return",style='TButton',command=lambda:raise_frame(fsettings))
btnBack.place(relx=0.5, y=250,anchor=CENTER)
#need an alert for the time being changed

#fsound stuff
ls = ttk.Label(fsound, text= "Sound",style='TLabel')
ls.place(relx= 0.5, y=50,anchor=CENTER)
btnBackS = ttk.Button(fsound,text="Return",style='TButton',command=lambda:raise_frame(fsettings))
btnBackS.place(relx= 0.5, y=250,anchor=CENTER)
sScale = Scale(fsound,from_=0, to=100,orient=HORIZONTAL,width = 30,bg="white")
sScale.place(relx=0.5,y=150,anchor=CENTER)
sScale.bind("<ButtonRelease-1>",playSound)


#ftext stuff
lt = ttk.Label(ftext, text= "Text",style='TLabel')
lt.place(relx= 0.5, y=50,anchor=CENTER)

btnSmall= ttk.Button(ftext,text="Small",style='TButton',command=lambda:cText(10))
btnSmall.place(relx= 0.5, y=150,anchor=CENTER)
btnMed= ttk.Button(ftext,text="Normal",style='TButton',command=lambda:cText(20))
btnMed.place(relx= 0.5, y=225,anchor=CENTER)
btnLarge= ttk.Button(ftext,text="Large",style='TButton',command=lambda:cText(30))
btnLarge.place(relx= 0.5, y=300,anchor=CENTER)

btnBackS = ttk.Button(ftext,text="Return",style='TButton',command=lambda:raise_frame(fsettings))
btnBackS.place(relx= 0.5, y=400,anchor=CENTER)

#flanguage stuff
ll = ttk.Label(flanguage, text= "Language",style='TLabel')
ll.place(relx= 0.5, y=50,anchor=CENTER)
btnBackS = ttk.Button(flanguage,text="return",style='TButton',command=lambda:raise_frame(fsettings))
btnBackS.place(relx= 0.5, y=350,anchor=CENTER)

def tick():
    global time1
    # get the current local time from the PC
    os.environ['TZ'] = "US/"+comboH.get()
    time.tzset()
    time2 = time.strftime('%H:%M:%S')
    #print (time2)
    
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    
    if time2 == "15:40:00":
        noticeT.config(text="PILLTIMES")
        pillGet.place(relx= 0.5,y=350, anchor =CENTER)
    if time2 == "15:50:00":
        miss = 1
        
    clock.after(200, tick)



alarm=0
tick()
raise_frame(fmain)

root.mainloop()
