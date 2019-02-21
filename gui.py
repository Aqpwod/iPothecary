

from tkinter import *
import time

#all commands go here
def raise_frame(frame):
    frame.tkraise()
    
def click():
    raise_frame(fsettings)

def click2():
    raise_frame(fmain)

def clickST():
    raise_frame(ftime)

def clickSo():
    raise_frame(fsound)

root = Tk()
mainW=400
mainH=300
fmain = Frame(root,width=mainW,height=mainH)
fsettings = Frame(root,width=mainW,height=mainH)
fadd = Frame(root,width=mainW,height=mainH)
ftime = Frame(root,width=mainW,height=mainH)
ftest = Frame(root,width=mainW,height=mainH)
fsound = Frame(root,width=mainW,height=mainH)

for frame in (fmain, fsettings, fadd, ftime, ftest,fsound):
    frame.grid(row=0,column=0,sticky='news')
    #frame.pack_propagate(0)
    
root.title("Test")
root.geometry('400x300+300+300')

#fmain stuff
mainT = Label(fmain,text="iPothecary",font=('Helvetica', 50, 'bold'))
mainT.grid(column=1,row=0)
btn = Button(fmain, text="Settings", command=click)
btn.grid(column=1, row=3)
time1 = ''
clock = Label(fmain, font=('Helvetica', 40, 'bold'))
clock.grid(column=1,row=1)

#fsettings stuff
l = Label(fsettings, text= "Settings",font=('Helvetica',20,'bold'))
l.pack(fill=X,pady=10)

btn1 = Button(fsettings, text="Set Time",font=('Helvetica',25),height=1,command=clickST)
btn1.pack(fill=X,pady=10)
btn2 = Button(fsettings, text="Sound",font=('Helvetica',25),height=1,command=clickSo)
btn2.pack(fill=X,pady=10)
btn3 = Button(fsettings, text="Text",font=('Helvetica',25),height=1)
btn3.pack(fill=X,pady=10)
btn4 = Button(fsettings, text="Language",font=('Helvetica',25),height=1)
btn4.pack(fill=X,pady=10)

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
btnS.grid(column=2, row= 2)


#fsound stuff
ls = Label(fsound, text= "Sound",font=('Helvetica',20,'bold'))
ls.grid(column=2,row=0)



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
