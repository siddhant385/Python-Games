from tkinter import *
import tkinter.messagebox as tmsg
from random import choice



def stone():
    global i , Cwin, Uwin
    i+= 1
    if i < 10:
        print(i)
        lbox.delete(0,END)
        wbox.delete(0,END)
        Sbox.delete(0,END)
        Compchoice = choice(["Paper","Sessiors"])
        lbox.insert(END,f"Computer chooses: {Compchoice}")
        if "Paper" in Compchoice:
            wbox.insert(END,"Winner Computer")
            Cwin += 1
        else:
            wbox.insert(END,"You are winner")
            Uwin +=1
        Sbox.insert(END,f"Your points: {Uwin}")
        Sbox.insert(END,f"Computer poinsts: {Cwin}")
        
    else:
        Sbox.delete(0,END)
        Sbox.insert(END,f"Your points: {Uwin}")
        Sbox.insert(END,f"Computer poinsts: {Cwin}")
        if Cwin > Uwin:
            fbox.insert(END,"Winner Computer")
        elif Cwin == Uwin:
            fbox.insert(END,"Game Draw")
        else:
            fbox.insert(END,"Winner Winner Chicken Dinner")
        a = tmsg.askretrycancel("Game Over","Do you want to retry or close")
        if a is True:
            lbox.delete(0,END)
            wbox.delete(0,END)
            Sbox.delete(0,END)
            fbox.delete(0,END)
            i = 0
            Cwin = 0
            Uwin = 0
        if a is False:
            tmsg.showinfo("Quitting","The Game is Going to quit\nPlease Visit Again")
            quit()
def paper():
    global i , Cwin, Uwin
    i+= 1
    if i < 10:
        lbox.delete(0,END)
        wbox.delete(0,END)
        Sbox.delete(0,END)
        Compchoice = choice(["Stone","Sessiors"])
        lbox.insert(END,f"Computer chooses: {Compchoice}")
        if "Sessiors" in Compchoice:
            wbox.insert(END,"Winner Computer")
            Cwin += 1
        else:
            Uwin +=1
            wbox.insert(END,"You are winner")
        Sbox.insert(END,f"Your points: {Uwin}")
        Sbox.insert(END,f"Computer poinsts: {Cwin}")
    else:
        Sbox.delete(0,END)
        Sbox.insert(END,f"Your points: {Uwin}")
        Sbox.insert(END,f"Computer poinsts: {Cwin}")
        if Cwin > Uwin:
            fbox.insert(END,"Final Winner Computer")
        elif Cwin == Uwin:
            fbox.insert(END,"Game Draw")
        else:
            fbox.insert(END,"Winner Winner Chicken Dinner")
        a = tmsg.askretrycancel("Game Over","Do you want to retry or close")
        if a is True:
            lbox.delete(0,END)
            wbox.delete(0,END)
            Sbox.delete(0,END)
            fbox.delete(0,END)
            i = 0
            Cwin = 0
            Uwin = 0
        if a is False:
            tmsg.showinfo("Quitting","The Game is Going to quit\nPlease Visit Again")
            quit()
        
    
def sessiors():
    global i , Cwin, Uwin
    i+= 1
    if i < 10:
        lbox.delete(0,END)
        wbox.delete(0,END)
        Sbox.delete(0,END)
        Compchoice = choice(["Paper","Stone"])
        lbox.insert(END,f"Computer chooses: {Compchoice}")
        if "Stone" in Compchoice:
            wbox.insert(END,"Winner Computer")
            Cwin += 1
        else:
            Uwin +=1
            wbox.insert(END,"You are winner")
        Sbox.insert(END,f"Your points: {Uwin}")
        Sbox.insert(END,f"Computer poinsts: {Cwin}")
    else:
        Sbox.delete(0,END)
        Sbox.insert(END,f"Your points: {Uwin}")
        Sbox.insert(END,f"Computer poinsts: {Cwin}")
        if Cwin > Uwin:
            fbox.insert(END,"Final Winner Computer")
        elif Cwin == Uwin:
            fbox.insert(END,"Game Draw")
        else:
            fbox.insert(END,"Winner Winner Chicken Dinner")
        print("Game Over")
        a = tmsg.askyesno("Game Over","Do you want to retry or close")
        if a is "yes":
            lbox.delete(0,END)
            wbox.delete(0,END)
            Sbox.delete(0,END)
            fbox.delete(0,END)
            i = 0
            Cwin = 0
            Uwin = 0
        if a is "no":
            tmsg.showinfo("Quitting","The Game is Going to quit\nPlease Visit Again")
            quit()


i = 0
Cwin = 0
Uwin = 0 
root = Tk()
root.geometry("600x800")
root.minsize(600,700)
root.maxsize(700,900)
root.title("Stone Paper Sessiors")
Starting = Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
Label(Starting,text="Stone Paper Sessiors",font="Comicsans 30 bold").pack()
Label(root,text="",bg="green",borderwidth=10,relief=SUNKEN).pack(side=LEFT,fill=Y)
Label(root,text="",bg="green",borderwidth=10,relief=SUNKEN).pack(side=RIGHT,fill=Y)
Starting.pack(side=TOP,fill= X)
Label(root,text="Your Chance",font="Algerian 20 bold",borderwidth=4,relief=SUNKEN).pack(padx=20,pady=20)
Label(root,text="Total Rounds : 09",font="Algerian 10 bold",borderwidth=4,relief=SUNKEN).pack(padx=20,pady=20)
Userchance = Frame(root,bg="red",borderwidth=5,relief=SUNKEN)
Stone = Button(Userchance,text="Stone",command=stone).grid(row=0,column=0)
Paper = Button(Userchance,text="Paper",command=paper).grid(row=0,column=1)
Sessiors = Button(Userchance,text="Sessiors",command=sessiors).grid(row=0,column=2)
Userchance.pack(side=TOP,pady=15)

Label(root,text="Computer Chance",font="Algerian 20 bold").pack()
Computer = Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
lbox= Listbox(Computer,height=1,width=30)
lbox.pack()
Computer.pack(side=TOP,pady=15)


Label(root,text="Winner",font="Algerian 20 bold").pack()
Winner = Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
wbox = Listbox(Winner,height=1,width=30)
wbox.pack()
Winner.pack(side=TOP,pady=15)


Label(root,text="Scoreboard",font="Algerian 20 bold").pack()
Scoreboard = Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
Sbox = Listbox(Scoreboard,height=2,width=30)
Sbox.pack()
Scoreboard.pack(side=TOP,pady=15)


Label(root,text="Final Result",font="Algerian 20 bold").pack()
final = Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
fbox = Listbox(final,height=1,width=30)
fbox.pack()
final.pack(side=TOP,pady=15)


ending = Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
Label(ending,text="Created By ~ $!ddH@nt Sharma\nGithub Repo : https://www.github.com/siddhant385\nPlease rate us giving a star in gihtub",font="Comicsans 10 bold").pack()
ending.pack(side=BOTTOM,fill= X)
root.mainloop()