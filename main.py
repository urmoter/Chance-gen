import tkinter as tk
import unmanin as U
#window
root = tk.Tk()
root.title("Number Generator!")
b = tk.Button(
    root,
    text = "Submit",
    command = lambda:[root.destroy(),U.BAT()])
b.pack(side="top")
#packing
root.mainloop()