import random
import tkinter as tk
import sys
def Other():
    trials: int =int(e1.get())
    w.destroy()
    i = 0
    One: int = 0
    Two: int = 0
    Three: int = 0
    Four: int = 0
    Five: int = 0
    Six: int = 0
    while i < trials:
        test = 0
        test = random.randint(1,6)
        if test == 1:
            print("One")
            One = One + 1
        elif test ==2:
            print("Two")
            Two = Two + 1
        elif test ==3:
            print("Three")
            Three = Three + 1
        elif test ==4:
            print("Four")
            Four = Four + 1
        elif test ==5:
            print("Five")
            Five = Five + 1
        elif test ==6:
            print("Six")
            Six = Six + 1
        else:
            sys.exit("Internal error!")
        i= i+1
    print("done")
    #WINDOW TIME!!!
    a= str(One)
    b = str(Two)
    c=str(Three)
    d=str(Four)
    e=str(Five)
    f=str(Six)
    root = tk.Tk()
    root.title("Results")
    one = tk.Label(root,text = ("Heads appeard "+a+" times!")).pack()
    two = tk.Label(root,text = ("Tails appeared "+b+" times!")).pack()
    three = tk.Label(root,text = ("Tails appeared "+c+" times!")).pack()
    four = tk.Label(root,text = ("Tails appeared "+d+" times!")).pack()
    five = tk.Label(root,text = ("Tails appeared "+e+" times!")).pack()
    six = tk.Label(root,text = ("Six appeared "+f+" times!")).pack()
    button = tk.Button(root,text = "Quit", command =lambda:exit(0)).pack()
    root.mainloop()
def ND():
    global w 
    w = tk.Tk()
    label = tk.Label(w, text ="Number of trials: ")
    global e1
    e1= tk.Entry(w)
    e1.grid(column ="1",row = "1")
    label.grid(column="1",row ="0")
    button = tk.Button(w,text = "Enter",command=lambda:Other()).grid(column="1",row="2")
    w.mainloop()