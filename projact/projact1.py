from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox
from PIL import Image , ImageTk

root = Tk()
root.title('Employee')
root.geometry('400x450')
root.resizable(False,False)
root.config(bg='#f5f5f5')




def welcome():
    music = AudioSegment.from_mp3('Audio\\welcom.mp3')
    play(music)

sond = pyttsx3.init()
vioses = sond.getProperty('voices')
sond.setProperty('reta',150)
sond.setProperty('voice',vioses[0].id)

def Speak(audio):
    sond.say(audio)
    sond.runAndWait()

def TakeComands():
    command = sr.Recognizer()
    with sr.Microphone() as mic:
        command.phrase_threshold = 0.1
        audio = command.listen(mic)
        try:
            query = command.recognize_google(audio, language='ar')
        except EXCEPTION as error:
            print(error)
        return query.lower()

        
def b1():
    query=TakeComands()
    name = query
    entry1.insert(0,name)

def b2():
    query=TakeComands()
    name = query
    entry2.insert(0,name)

def b3():
    query=TakeComands()
    name = query
    entry3.insert(0,name)

def Sv():
    nmaefile = e_save.get()
    name = entry1.get()
    co = entry2.get()
    job=entry3.get()
    saveinf=qrcode.make(name + co + job)
    saveinf.save('employee/'+nmaefile+'.jpg')
    messagebox.showinfo('save','save[' +nmaefile+ ']employee')



ph=Image.open(r'Designs\image.jpeg')
photo = ImageTk.PhotoImage(ph)
i_imgae=Label(root,image=photo)
i_imgae.place(x=2,y=1,width=395,height=220) 

text1 = Label(root,text="Emp Name  ",font=('Time New Roman',14))
text1.place(x=10,y=230)
entry1 = Entry(root,font=('Time New Roman',14))
entry1.place(x=130,y=230,height=30,width=200)

text2 = Label(root,text="Emp Country  ",font=('Time New Roman',14))
text2.place(x=10,y=270)
entry2 = Entry(root,font=('Time New Roman',14),
               )
entry2.place(x=130,y=270,height=30,width=200)

text3 = Label(root,text="Emp Job  ",font=('Time New Roman',14))
text3.place(x=10,y=310)
entry3 = Entry(root,font=('Time New Roman',14))
entry3.place(x=130,y=310,height=30,width=200)

b1=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b1)
b1.place(x=340,y=230,height=36,width=30)

b2=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b2)
b2.place(x=340,y=270,height=36,width=30)

b3=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b3)
b3.place(x=340,y=310,height=36,width=30)

l_save = Label(root,text='Save File',font=('Tajawal',14))
l_save.place(x=10,y=382)

e_save = Entry(root,font=('Tajawal',14))
e_save.place(x=100,y=382,width=190,height=30)

B_save=Button(root,text="Save💾",font=('Tajawal',12),bg='green',fg='black',command=Sv)
B_save.place(x=300,y=382,height=30,width=60)

root.mainloop()