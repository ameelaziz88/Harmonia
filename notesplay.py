# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:31:47 2021

@author: stjoh
"""

from playsound import playsound
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


piano = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C","C#","D","D#","E","F","F#","G"]

def majorTriad(note):
    if note < 12:
        chord = ""
        chord += piano[note]
        chord += " - "
        chord += piano[note+4]
        chord += " - "
        chord += piano[note+7]
        return chord
    else:
        print("Out of bounds")

def minorTriad(note):
    if note < 12:
        chord = ""
        chord += piano[note]
        chord += " - "
        chord += piano[note+3]
        chord += " - "
        chord += piano[note+7]
        return chord
    else:
        print("Out of bounds")
    

major = True

def changeTypemaj():
    global major
    if major == False:
        major = True
        

def changeTypemin():
    global major
    if major == True:
        major = False


def isClickedc():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\c.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\cm.wav')
        
def isClickedcs():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\cs.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\pm.wav')
        
def isClickedd():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\d.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\dm.wav')
              
def isClickedds():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\ds.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\um.wav')

def isClickede():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\e.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\em.wav')
        
def isClickedf():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\f.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\fm.wav')
        
def isClickedfs():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\fs.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\xm.wav')
                
def isClickedg():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\g.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\gm.wav')
                
def isClickedgs():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\gs.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\ym.wav')
        
def isClickeda():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\a.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\am.wav')
        
def isClickedbf():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\bf.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\bb.wav')
        
def isClickedb():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\b.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\bm.wav')
        
def isClickedbc():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\cc.wav')
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\zm.wav')
        
    
             
        
        



canvas = tk.Canvas(root, width=1400, height=700, )

canvas.grid(columns=20,columnspan= 3,rowspan= 4)


piano = Image.open("piano.png")
piano_resize = piano.resize((960, 480))
newPiano = ImageTk.PhotoImage(piano_resize)
piano_label = tk.Label(image=newPiano)
piano_label.image = newPiano
piano_label.grid(columnspan = 3, column=0, row=1)


#logo_label.image = newLogo


instructions = tk.Label(root, text="Click a piano key and then either major or minor", font = ("Helvetica", 17))
instructions.grid(columnspan=3, column=0, row=3)

notesLabel = tk.Label(root, text="Notes that are in the piano and shit", font = ("Helvetica", 20))
notesLabel.grid(columnspan=3, column=0, row=2)

title = tk.Label(root, text="Harmonia", width =40, font = ("Rockwell", 25))
title.grid(columnspan=3, column=0, row=0)

logo = Image.open("Capture.PNG")
logo = logo.resize((300, 147))
newLogo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = newLogo).place(x=550, y =0)

button = Image.open("majorButton.png")
button = button.resize((200,45))
buttonImg = ImageTk.PhotoImage(button)

button1 = Image.open("minorButton.png")
button1 = button1.resize((200,45))
buttonImg1 = ImageTk.PhotoImage(button1)


major_btn = tk.Button(root, text="Major", width=200, height=45, image=buttonImg,command=changeTypemaj)
major_btn.grid(column=0, row = 2)

minor_btn = tk.Button(root, text="Minor", width=200, height=45, image=buttonImg1,command=changeTypemin)
minor_btn.grid(column=2, row = 2)

# Piano key Buttons
def hide_button(widget):
    widget.pack_forget()



buttonC1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedc).place(x=224,y=340)
buttonD1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedd).place(x=292,y=340)
buttonE1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickede).place(x=361,y=340)
buttonF1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedf).place(x=429,y=340)
buttonG1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedg).place(x=497,y=340)
buttonA1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickeda).place(x=566,y=340)
buttonB1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedb).place(x=635,y=340)

buttonC2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedbc).place(x=704,y=340)
buttonD2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8).place(x=773,y=340)
buttonE2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8).place(x=842,y=340)
buttonF2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8).place(x=910,y=340)
buttonG2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8).place(x=978,y=340)
buttonA2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8).place(x=1046,y=340)
buttonB2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8).place(x=1115,y=340)

buttonCS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedcs).place(x=273, y=179)
buttonDS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedds).place(x=341, y=179)
buttonFS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedfs).place(x=478, y=179)
buttonGS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedgs).place(x=546, y=179)
buttonAS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedbf).place(x=614, y=179)

buttonCS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10).place(x=753, y=179)
buttonDS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10).place(x=822, y=179)
buttonFS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10).place(x=958, y=179)
buttonGS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10).place(x=1026, y=179)
buttonAS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10).place(x=1094, y=179)



root.mainloop()
