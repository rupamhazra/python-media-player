import os
import pygame
from mutagen.id3 import ID3

from tkinter.filedialog import askdirectory
from tkinter import *

root = Tk()
root.minsize(300,300)

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root, textvariable=v, width=35)

index = 0

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def playsong(event):
    pygame.mixer.music.play()
    updatelabel()

def pausesong(event):
    pygame.mixer.music.pause()
    updatelabel()

def resumesong(event):
    pygame.mixer.music.unpause()
    updatelabel()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files) # path : C:/asss/assssaaa.mp3
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)

    #print('listofsongs',listofsongs[0])

    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])

directorychooser()


label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()

playbutton = Button(root, text='Play Music')
playbutton.pack()

pausebutton = Button(root, text='Pause Music')
pausebutton.pack()

resumebutton = Button(root, text='Resume Music')
resumebutton.pack()

nextbutton = Button(root, text='Next Song')
nextbutton.pack()

previousbutton = Button(root, text='Previous Song')
previousbutton.pack()

stopbutton = Button(root, text='Stop Music')
stopbutton.pack()


playbutton.bind("<Button-1>", playsong)
resumebutton.bind("<Button-1>", resumesong)
pausebutton.bind("<Button-1>", pausesong)
nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)

songlabel.pack()


root.mainloop()