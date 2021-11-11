#pip install numpy
#pip install pyautogui
#pip install opencv-python
#pip install Pillow

from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

import numpy as np
import cv2
import pyautogui
import random

def snapshot():
    # take screenshot using pyautogui
    img = pyautogui.screenshot()
    
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    imge = cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
    number =random.randrange(0, 1000, 3)
    # writing it to the disk using opencv
    cv2.imwrite("slambook_image"+str(number)+".png", imge)
    messagebox.showinfo("showinfo", "Information")


colorBG='wheat'
txtBG='teal'
main_window=Tk()
main_window.title("My Slambook")
main_window.attributes('-fullscreen',True)
#main_window.geometry("1000x900")
main_window.configure(bg=colorBG)
#frame1 = Frame(main_window, highlightbackground="black", highlightthickness=1,width=600, height=100, bd= 1)

cursive = tkFont.Font(family="Brush Script MT",size=24)
heading=tkFont.Font(family="Comic Sans MS",size=30,weight="bold")
box= tkFont.Font(family="Helvetica",size=20)


#canvas = Canvas(main_window, width = 400, height = 100,background=colorBG,borderwidth=0)      
#canvas.grid(row=0,column=0,columnspan=4)  
#img = PhotoImage(file="about_you.jpeg")      
#canvas.create_image(0,0, anchor=NW, image=img)   

lblHeading = Label(main_window, text="All About you",font=heading,fg='purple',bg=colorBG)
lblHeading.grid(row=1,column=0,columnspan=2)

lblName = Label(main_window, text="Name:",font=cursive,fg='red',bg=colorBG)
lblName.grid(row=2,column=0)
txtName = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtName.grid(row=2,column=1)

lblNickname = Label(main_window, text="Nickname:",fg='red',bg=colorBG,font=cursive)
lblNickname.grid(row=3,column=0)
txtNickname = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtNickname.grid(row=3,column=1)


lblPronoun = Label(main_window, text="Pronoun:",fg='red',bg=colorBG,font=cursive)
lblPronoun.grid(row=4,column=0)
txtPronoun = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtPronoun.grid(row=4,column=1)


lblQuarantineFavs=Label(main_window,text="Quarantine Favs",fg='purple',bg=colorBG,font=heading)
lblQuarantineFavs.grid(row=6,column=0,columnspan=4)



lblFood = Label(main_window, text="Food:",fg='red',bg=colorBG,font=cursive)
lblFood.grid(row=7,column=0)
txtFood = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtFood.grid(row=7,column=1)

lblColorSmell = Label(main_window, text="Music:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=8,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=8,column=1)

lblColorSmell = Label(main_window, text="Celeb:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=9,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=9,column=1)

lblColorSmell = Label(main_window, text="Subject:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=10,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=10,column=1)

lblColorSmell = Label(main_window, text="Artist:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=11,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=11,column=1)

lblColorSmell = Label(main_window, text="Book:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=12,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=12,column=1)

lblColorSmell = Label(main_window, text="TV Show:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=13,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=13,column=1)

lblColorSmell = Label(main_window, text="Movie:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=14,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=14,column=1)


lblColorSmell = Label(main_window, text="Game:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=15,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=15,column=1)

lblColorSmell = Label(main_window, text="Hobby:",fg='red',bg=colorBG,font=cursive)
lblColorSmell.grid(row=16,column=0)
txtColorSmell = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtColorSmell.grid(row=16,column=1)

lblQuarantineFavs=Label(main_window,text="This or that??",fg='forestgreen',bg=colorBG,font=heading)
lblQuarantineFavs.grid(row=4,column=4,columnspan=2)

lbl=Label(main_window,text='ABC',fg=colorBG,bg=colorBG)
lbl.grid(row=4,column=3)


var1 = IntVar()
R1 = Radiobutton(main_window, text="Day", variable=var1, value=1,fg='blue',bg=colorBG,font=cursive)
R1.grid(row=5,column=4,sticky='e')
R2 = Radiobutton(main_window, text="Night", variable=var1, value=2,fg='blue',bg=colorBG,font=cursive)
R2.grid(row=5,column=5,sticky='w')

var2 = IntVar()
R3 = Radiobutton(main_window, text="Pepsi", variable=var2, value=1,fg='blue',bg=colorBG,font=cursive)
R3.grid(row=6,column=4,sticky='e')
R4 = Radiobutton(main_window, text="Coke", variable=var2, value=2,fg='blue',bg=colorBG,font=cursive)
R4.grid(row=6,column=5,sticky='w')

var3 = IntVar()
R5 = Radiobutton(main_window, text="Beauty", variable=var3, value=1,fg='blue',bg=colorBG,font=cursive)
R5.grid(row=7,column=4,sticky='e')
R6 = Radiobutton(main_window, text="Brains", variable=var3, value=2,fg='blue',bg=colorBG,font=cursive)
R6.grid(row=7,column=5,sticky='w')

var4 = IntVar()
R7 = Radiobutton(main_window, text="Save", variable=var4, value=1,fg='blue',bg=colorBG,font=cursive,justify="center")
R7.grid(row=8,column=4,sticky='e')
R8 = Radiobutton(main_window, text="Spend", variable=var4, value=2,fg='blue',bg=colorBG,font=cursive,justify="center")
R8.grid(row=8,column=5,sticky='w')

var5 = IntVar()
R9 = Radiobutton(main_window, text="Reality", variable=var5, value=1,fg='blue',bg=colorBG,font=cursive)
R9.grid(row=9,column=4,sticky='e')
R10 = Radiobutton(main_window, text="Fiction", variable=var5, value=2,fg='blue',bg=colorBG,font=cursive)
R10.grid(row=9,column=5,sticky='w')

var6 = IntVar()
R11 = Radiobutton(main_window, text="Stay in", variable=var6, value=1,fg='blue',bg=colorBG,font=cursive)
R11.grid(row=10,column=4,sticky='e')
R12 = Radiobutton(main_window, text="Go out", variable=var6, value=2,fg='blue',bg=colorBG,font=cursive)
R12.grid(row=10,column=5,sticky='w')

var7 = IntVar()
R13 = Radiobutton(main_window, text="Hot", variable=var7, value=1,fg='blue',bg=colorBG,font=cursive)
R13.grid(row=11,column=4,sticky='e')
R14 = Radiobutton(main_window, text="Cold", variable=var7, value=2,fg='blue',bg=colorBG,font=cursive)
R14.grid(row=11,column=5,sticky='w')

var8 = IntVar()
R15 = Radiobutton(main_window, text="Dogs", variable=var8, value=1,fg='blue',bg=colorBG,font=cursive)
R15.grid(row=12,column=4,sticky='e')
R16 = Radiobutton(main_window, text="Cats", variable=var8, value=2,fg='blue',bg=colorBG,font=cursive)
R16.grid(row=12,column=5,sticky='w')

lbl=Label(main_window,text="Get to know me...",fg='darkorange',bg=colorBG,font=heading)
lbl.grid(row=2,column=7,columnspan=2)


lbl=Label(main_window,text='ABC',fg=colorBG,bg=colorBG)
lbl.grid(row=3,column=6)

lblAboutYourself = Label(main_window, text="Tell me a bit about yourself",fg='mediumvioletred',bg=colorBG,font=cursive)
lblAboutYourself.grid(row=3,column=8)
txtAboutYourself = Entry(main_window, fg=txtBG,bg=colorBG,font=box,borderwidth=0)
txtAboutYourself.grid(row=4,column=8)

lblBucks = Label(main_window, text="What would you do with a billion bucks?",fg='mediumvioletred',bg=colorBG,font=cursive)
lblBucks.grid(row=5,column=8)
txtBucks = Entry(main_window,fg=txtBG,bg=colorBG,font=box)
txtBucks.grid(row=6,column=8)

lblSoulmate = Label(main_window, text="Do you believe in soulmate?",fg='mediumvioletred',bg=colorBG,font=cursive)
lblSoulmate.grid(row=7,column=8)
txtSoulmate = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtSoulmate.grid(row=8,column=8)

lblAdvice = Label(main_window, text="What's one piece of advice you'd give?",fg='mediumvioletred',bg=colorBG,font=cursive)
lblAdvice.grid(row=9,column=8)
txtAdvice = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtAdvice.grid(row=10,column=8)

lblLockdown = Label(main_window, text="Three things you will do after lockdown..",fg='mediumvioletred',bg=colorBG,font=cursive)
lblLockdown.grid(row=11,column=8)
txtLockdown = Entry(main_window, bd =0,fg=txtBG,bg=colorBG,font=box)
txtLockdown.grid(row=12,column=8)

lblHonest = Label(main_window, text="How honest do you think I am?",fg='mediumvioletred',bg=colorBG,font=cursive)
lblHonest.grid(row=13,column=8)
sbHonest = Spinbox(main_window, from_=0, to=10,fg=txtBG,bg=colorBG,font=cursive)
sbHonest.grid(row=14,column=8)

lblDressing = Label(main_window, text="Scale my way of styling..",fg='mediumvioletred',bg=colorBG,font=cursive)
lblDressing.grid(row=15,column=8)
var = DoubleVar()
scaleDressing = Scale( main_window, variable = var,orient=HORIZONTAL,fg=txtBG,bg=colorBG,font=cursive)
scaleDressing.grid(row=16,column=8)

btnSubmit=Button(main_window,text="Send",bg=colorBG,fg=colorBG,bd=0,font=cursive,relief='raised',command=snapshot)
btnSubmit.grid(row=16,column=5,sticky='W')

btnExit = Button(main_window, text="Exit", command=main_window.destroy)
btnExit.grid(row=17,column=5)


main_window.mainloop()
