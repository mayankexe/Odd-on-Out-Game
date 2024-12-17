# importing the module
import tkinter
import tkinter.messagebox
from tkinter import *
import random
# importing the module



# initialising tkinter
class window(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
# initialising tkinter



# creating the window
root = Tk()
app = window(root)
root.geometry("630x630")
root.title('Odd Even Game')

C = Canvas(root, bg="blue", height=0, width=300)
filename = PhotoImage(file = "BG.png")
background_label = Label(root,image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

frame = Frame(root)
frame.pack()
# creating the window



# player details
name = " "
score = 0
def score_update():
    global score
    score = score + 1 
player_det = []
# player details




# image
level_1e = "mario1.png"
level_1o = "marioe.png"
level_2e = "raiden1.png"
level_2o = "raidene.png"
level_3e = "mgmn1.png"
level_3o = "mgmne.png"
level_4e = "sans1.png"
level_4o = "sanse.png"
level_5e = "kirby1.png"
level_5o = "kirbye.png"
level_6e = "link1.png"
level_6o = "linke.png"
level_7e = "pika1.png"
level_7o = "pikae.png"
# image




# built-functions for visuals
def create_cards(odd_image,even_image,next_level,fno,order,suc,err,w,h):
    rx = random.randint(0,order-1)
    ry = random.randint(0,order-1)
    
    for i in range(0,order):
        for j in range(0,order):
            if i == rx and j == ry:
                create_button(i,j,suc,odd_image,next_level,fno,odd_image,w,h)
            else:
                create_button(i,j,err,even_image,next_level,fno,odd_image,w,h)



def second_level(fno):
    fno.pack_forget()
    frame2 = Frame(root)
    frame2.pack()
    suc = "Congratulations! You have cleared level 2..Time to increase the difficulty!"
    err = "Wrong Answer..Don't give up yet!"
    create_cards(level_2o,level_2e,third_level,frame2,3,suc,err,210,210)

def third_level(fno):
    fno.pack_forget()
    frame3 = Frame(root)
    frame3.pack()
    suc = "Congratulations! You have cleared level 3..Keep Going Buddy!"
    err = "Wrong Answer..Don't give up yet!"
    create_cards(level_3o,level_3e,fourth_level,frame3,4,suc,err,157.5,157.5)

def fourth_level(fno):
    fno.pack_forget()
    frame4 = Frame(root)
    frame4.pack()
    suc = "Congratulations! You have cleared level 4..Amazing gameplay!"
    err = "Wrong Answer..Please Try again !!"
    create_cards(level_4o,level_4e,fifth_level,frame4,5,suc,err,126,126)

def fifth_level(fno):
    fno.pack_forget()
    frame5 = Frame(root)
    frame5.pack()
    suc = "Woohoo! One more to go"
    err = "Wrong Answer..Keep Trying !!"
    create_cards(level_5o,level_5e,sixth_level,frame5,6,suc,err,105,105)

def sixth_level(fno):
    fno.pack_forget()
    frame6 = Frame(root)
    frame6.pack()
    suc = "Congratulations! You have successfully finished the gamey"
    err = "Wrong Answer..Keep Trying !!"
    create_cards(level_6o,level_6e,seventh_level,frame6,7,suc,err,90,90)

def seventh_level(fno):
    fno.pack_forget()
    frame7 = Frame(root)
    frame7.pack()
    suc = "Congratulations! You have successfully finished the game"
    err = "Wrong Answer..Keep Trying !!"
    create_cards(level_7o,level_7e,final_level,frame7,8,suc,err,78.75,78.75)

def final_level(fno):
    fno.pack_forget()
    frame6 = Frame(root)
    frame6.pack()
    canvas1 = Canvas(root, width = 630, height = 630)
    canvas1.pack() 
    entry1 = tkinter.Entry (root) 
    canvas1.create_window(310,140 , window=entry1)

    def getName():
        global name
        name = entry1.get()
        msg = name,"scored",score
        label1 = tkinter.Label(root, text = msg)
        canvas1.create_window(300, 400, window=label1)
        pl_name = name

    
    button1 = tkinter.Button(text='Submit', command = getName ).place(relx = 0.45, rely = 0.35)
    canvas1.create_window(200, 180, window=button1)

def create_button(x,y,msg,picture,next_level,fno,odd,w,h):
    if picture == odd:
        image = PhotoImage(file=picture)
        click = Button(fno, image=image, width= w, height=h, bd = 0,command = lambda : [score_update(),next_level(fno),tkinter.messagebox.showinfo( "Odd One Out Project",msg)])
        click.image = image
        click.grid( row = x, column = y)
        
    else:
        image = PhotoImage(file=picture)
        click = Button(fno, image=image, width= w, height=h, bd = 0,command = lambda : [next_level(fno),tkinter.messagebox.showinfo( "Odd One Out Project",msg)])
        click.image = image
        click.grid( row = x, column = y)


def create_frame(fno):
    root.geometry("630x630")
    fno.pack_forget()
    frame = Frame(root)
    frame.pack()
    suc = "Congratulations! You have cleared level 1"
    err = "Wrong Answer..Please Try again !!"
    create_cards(level_1o,level_1e,second_level,frame,2,suc,err,315,315)

def intro():
    root.geometry("630x630")
    frame0 = Frame(root)
    frame0.place(relx = 0.45 ,rely = 0.35)

    click = Button(frame0,text="Start!!", width = 5 , height = 2,command = lambda : [create_frame(frame0),tkinter.messagebox.showinfo( "Odd One Out Project","The game has begun!!")]).pack()

# built-functions for visuals 




# executing intro() to start the game
intro()
# executing intro() to start the game



# starting the widget
root.mainloop()
# starting the widget

# saving a list for use in scoreboard
player_det = [name,score]
# saving a list for use in scoreboard
