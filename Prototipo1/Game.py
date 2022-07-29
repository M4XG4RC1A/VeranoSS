import json
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, color
import json
import random

from numpy import imag

root = Tk()

root.title("Game")
root.geometry("700x500")

global Pixels
global models
global selection

selection = ""
models = json.load(open("Data.json"));
#list(models.keys())

sizePix = 500;
OptionsLength = 200;
nPix = 8;
buttonSize = 60;
roundPix= (sizePix-(buttonSize*nPix))/2;
pixel = PhotoImage(width=1,height=1);

global cNull,cOn,cDraw
cNull = "#FFFFFF";
cOn = "#FF0000";
cDraw = "#0000FF"


def Change(id, color=""):
    global selection
    if Mode.cget("text") == "Mode=write":
        Pixels[id].configure(bg=cOn)
    elif Mode.cget("text") == "Mode=erase":
        print(selection)
        print(models[selection]["Draw"][id])
        if models[selection]["Draw"][id] == 1:
            simpleChange(id,cDraw)
        else:
            simpleChange(id,cNull)

def simpleChange(id, color):
    Pixels[id].configure(bg=color)
    pass

def array2Image(sel):
    for i in range(64):
        if models[sel]["Draw"][i] == 1:
            simpleChange(i,cDraw)
        else:
            simpleChange(i,cNull)
    pass

def endGame():
    global selection

    sumCorrect = 0
    sumIncorrect = 0

    print("Aqui")
    print(Pixels[1].cget("bg"))

    for i in range(64):
        if Pixels[i].cget("bg") == cOn:
            if models[selection]["Map"][i] == 1:
                sumCorrect+=1;
            else:
                sumIncorrect+=1;
        Pixels[i].configure(bg=cNull)

    total = sum(models[selection]["Map"])
    messagebox.showinfo(message= "Correct: "+str(sumCorrect)+" ("+str(sumCorrect/total*100)+"%)"+\
                                "\nIncorrect: "+str(sumIncorrect)+\
                                "\nTotal: "+str(sumCorrect-sumIncorrect)+" ("+str((sumCorrect-sumIncorrect)/total*100)+"%)", title="Game Finished")
    Mode.configure(text="No Game")
    pass

def defImg():
    global selection

    print("Img")
    vals = list(models.keys())
    sel = random.randint(0,len(vals)-1)

    print(sel)
    selection = vals[sel]

    print(selection)

    array2Image(selection)

    Mode.configure(text="Mode=write")
    pass

def changeMod():
    print(Mode.cget("text"))
    if Mode.cget("text") == "Mode=write":
        Mode.configure(text="Mode=erase")
    elif Mode.cget("text") == "Mode=erase":
        Mode.configure(text="Mode=write")

img = PhotoImage("Back.png")

PixelsPanel = Frame(root,bg="#000000", width=sizePix, height=sizePix)
PixelsPanel.place(x=0,y=0)
OptionsPanel = Frame(root, bg="#0000FF", width=OptionsLength, height=sizePix)
OptionsPanel.place(x=sizePix,y=0)

lab = Label(OptionsPanel, image= img)
lab.place(x=0,y=0)

wSet = 100;
xSet = (OptionsLength-wSet)/2 - 4;

setImg = Button(OptionsPanel, text="Start Game", bd= -3, bg="#0000BB", image=pixel, width=wSet, height= 30, command=lambda:defImg(), compound="c"); setImg.place(x=xSet,y=100)
Mode = Button(OptionsPanel, text="No Game", bd= -3, bg="#0000BB", image=pixel, width=wSet, height= 30, command=lambda:changeMod(), compound="c"); Mode.place(x=xSet,y=200)
Finish = Button(OptionsPanel, text="End Game", bd= -3, bg="#0000BB", image=pixel, width=wSet, height= 30, command=lambda:endGame(), compound="c"); Finish.place(x=xSet,y=400)

yspace = roundPix/2+2
xspace = roundPix/2+2; Pix00 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(0)); Pix00.place(x=xspace,y=yspace)
xspace += buttonSize; Pix01 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(1)); Pix01.place(x=xspace,y=yspace)
xspace += buttonSize; Pix02 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(2)); Pix02.place(x=xspace,y=yspace)
xspace += buttonSize; Pix03 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(3)); Pix03.place(x=xspace,y=yspace)
xspace += buttonSize; Pix04 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(4)); Pix04.place(x=xspace,y=yspace)
xspace += buttonSize; Pix05 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(5)); Pix05.place(x=xspace,y=yspace)
xspace += buttonSize; Pix06 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(6)); Pix06.place(x=xspace,y=yspace)
xspace += buttonSize; Pix07 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(7)); Pix07.place(x=xspace,y=yspace)

yspace += buttonSize
xspace = roundPix/2+2; Pix10 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(8)); Pix10.place(x=xspace,y=yspace)
xspace += buttonSize; Pix11 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(9)); Pix11.place(x=xspace,y=yspace)
xspace += buttonSize; Pix12 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(10)); Pix12.place(x=xspace,y=yspace)
xspace += buttonSize; Pix13 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(11)); Pix13.place(x=xspace,y=yspace)
xspace += buttonSize; Pix14 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(12)); Pix14.place(x=xspace,y=yspace)
xspace += buttonSize; Pix15 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(13)); Pix15.place(x=xspace,y=yspace)
xspace += buttonSize; Pix16 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(14)); Pix16.place(x=xspace,y=yspace)
xspace += buttonSize; Pix17 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(15)); Pix17.place(x=xspace,y=yspace)

yspace += buttonSize
xspace = roundPix/2+2; Pix20 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(16)); Pix20.place(x=xspace,y=yspace)
xspace += buttonSize; Pix21 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(17)); Pix21.place(x=xspace,y=yspace)
xspace += buttonSize; Pix22 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(18)); Pix22.place(x=xspace,y=yspace)
xspace += buttonSize; Pix23 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(19)); Pix23.place(x=xspace,y=yspace)
xspace += buttonSize; Pix24 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(20)); Pix24.place(x=xspace,y=yspace)
xspace += buttonSize; Pix25 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(21)); Pix25.place(x=xspace,y=yspace)
xspace += buttonSize; Pix26 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(22)); Pix26.place(x=xspace,y=yspace)
xspace += buttonSize; Pix27 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(23)); Pix27.place(x=xspace,y=yspace)

yspace += buttonSize
xspace = roundPix/2+2; Pix30 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(24)); Pix30.place(x=xspace,y=yspace)
xspace += buttonSize; Pix31 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(25)); Pix31.place(x=xspace,y=yspace)
xspace += buttonSize; Pix32 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(26)); Pix32.place(x=xspace,y=yspace)
xspace += buttonSize; Pix33 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(27)); Pix33.place(x=xspace,y=yspace)
xspace += buttonSize; Pix34 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(28)); Pix34.place(x=xspace,y=yspace)
xspace += buttonSize; Pix35 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(29)); Pix35.place(x=xspace,y=yspace)
xspace += buttonSize; Pix36 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(30)); Pix36.place(x=xspace,y=yspace)
xspace += buttonSize; Pix37 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(31)); Pix37.place(x=xspace,y=yspace)

yspace += buttonSize
xspace = roundPix/2+2; Pix40 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(32)); Pix40.place(x=xspace,y=yspace)
xspace += buttonSize; Pix41 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(33)); Pix41.place(x=xspace,y=yspace)
xspace += buttonSize; Pix42 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(34)); Pix42.place(x=xspace,y=yspace)
xspace += buttonSize; Pix43 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(35)); Pix43.place(x=xspace,y=yspace)
xspace += buttonSize; Pix44 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(36)); Pix44.place(x=xspace,y=yspace)
xspace += buttonSize; Pix45 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(37)); Pix45.place(x=xspace,y=yspace)
xspace += buttonSize; Pix46 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(38)); Pix46.place(x=xspace,y=yspace)
xspace += buttonSize; Pix47 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(39)); Pix47.place(x=xspace,y=yspace)

yspace += buttonSize
xspace = roundPix/2+2; Pix50 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(40)); Pix50.place(x=xspace,y=yspace)
xspace += buttonSize; Pix51 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(41)); Pix51.place(x=xspace,y=yspace)
xspace += buttonSize; Pix52 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(42)); Pix52.place(x=xspace,y=yspace)
xspace += buttonSize; Pix53 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(43)); Pix53.place(x=xspace,y=yspace)
xspace += buttonSize; Pix54 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(44)); Pix54.place(x=xspace,y=yspace)
xspace += buttonSize; Pix55 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(45)); Pix55.place(x=xspace,y=yspace)
xspace += buttonSize; Pix56 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(46)); Pix56.place(x=xspace,y=yspace)
xspace += buttonSize; Pix57 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(47)); Pix57.place(x=xspace,y=yspace)

yspace += buttonSize
xspace = roundPix/2+2; Pix60 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(48)); Pix60.place(x=xspace,y=yspace)
xspace += buttonSize; Pix61 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(49)); Pix61.place(x=xspace,y=yspace)
xspace += buttonSize; Pix62 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(50)); Pix62.place(x=xspace,y=yspace)
xspace += buttonSize; Pix63 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(51)); Pix63.place(x=xspace,y=yspace)
xspace += buttonSize; Pix64 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(52)); Pix64.place(x=xspace,y=yspace)
xspace += buttonSize; Pix65 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(53)); Pix65.place(x=xspace,y=yspace)
xspace += buttonSize; Pix66 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(54)); Pix66.place(x=xspace,y=yspace)
xspace += buttonSize; Pix67 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(55)); Pix67.place(x=xspace,y=yspace)

yspace += buttonSize
xspace = roundPix/2+2; Pix70 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(56)); Pix70.place(x=xspace,y=yspace)
xspace += buttonSize; Pix71 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(57)); Pix71.place(x=xspace,y=yspace)
xspace += buttonSize; Pix72 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(58)); Pix72.place(x=xspace,y=yspace)
xspace += buttonSize; Pix73 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(59)); Pix73.place(x=xspace,y=yspace)
xspace += buttonSize; Pix74 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(60)); Pix74.place(x=xspace,y=yspace)
xspace += buttonSize; Pix75 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(61)); Pix75.place(x=xspace,y=yspace)
xspace += buttonSize; Pix76 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(62)); Pix76.place(x=xspace,y=yspace)
xspace += buttonSize; Pix77 = Button(PixelsPanel, bd= -3, bg=cNull, image=pixel, width=buttonSize, height= buttonSize, command=lambda:Change(63)); Pix77.place(x=xspace,y=yspace)

Pixels = [Pix00, Pix01, Pix02, Pix03, Pix04, Pix05, Pix06, Pix07,\
        Pix10, Pix11, Pix12, Pix13, Pix14, Pix15, Pix16, Pix17,\
        Pix20, Pix21, Pix22, Pix23, Pix24, Pix25, Pix26, Pix27,\
        Pix30, Pix31, Pix32, Pix33, Pix34, Pix35, Pix36, Pix37,\
        Pix40, Pix41, Pix42, Pix43, Pix44, Pix45, Pix46, Pix47,\
        Pix50, Pix51, Pix52, Pix53, Pix54, Pix55, Pix56, Pix57,\
        Pix60, Pix61, Pix62, Pix63, Pix64, Pix65, Pix66, Pix67,\
        Pix70, Pix71, Pix72, Pix73, Pix74, Pix75, Pix76, Pix77]

root.mainloop()