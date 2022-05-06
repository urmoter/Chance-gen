import sys
import OtS as O
import HnT as H
import tkinter as tk
def main():
    global w 
    w = tk.Tk()
    label = tk.Label(w, text ="Number dice(1) or coin flip (2): ")
    global e1
    e1= tk.Entry(w)
    e1.grid(column ="1",row = "1")
    label.grid(column="1",row ="0")
    button = tk.Button(w,text = "Enter",command=lambda:BAT()).grid(column="1",row="2")
    w.mainloop()
    
def BAT():
    t1=int(e1.get())
    if t1==1:
        w.destroy()
        O.ND()
    elif t1==2:
        w.destroy()
        H.CT()
    else:
        w.destroy()
        sys.exit("invalid input!") 