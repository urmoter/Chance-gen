import random
import tkinter as tk
import sys
def Other():
    trials:int= int(e1.get())
    w.destroy()
    if trials <= 0:
        sys.exit("invalid input!")
    else:
        i = 0
        Head: int = 0
        Tails: int = 0
        while i < trials:
            test = 0
            test = random.randint(1,2)
            if test == 1:
                print("Heads!")
                Head = Head + 1
            elif test ==2:
                print("Tails!")
                Tails = Tails + 1
            else:
                sys.exit("Internal error!")
            i= i+1
        print("done")
        a=str(Head)
        b=str(Tails)
        #WINDOW TIME!!!
        root = tk.Tk()
        root.title("Results")
        heads = tk.Label(root,text = ("Heads appeard "+a+" times!")).pack()
        tails = tk.Label(root,text = ("Tails appeared "+b+" times!")).pack()
        button = tk.Button(root,text = "Quit", command =lambda:exit(0)).pack()
        root.mainloop()
def CT():
    global w 
    w = tk.Tk()
    label = tk.Label(w, text ="Number of trials: ")
    global e1
    e1= tk.Entry(w)
    e1.grid(column ="1",row = "1")
    label.grid(column="1",row ="0")
    button = tk.Button(w,text = "Enter",command=lambda:Other()).grid(column="1",row="2")
    w.mainloop()
