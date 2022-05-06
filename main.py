#package imports
import tkinter as tk
import unmanin as U

#window
root = tk.Tk()
root.title("Number Generator!")
b = tk.Button(
    root,
    text = "Begin!",
    command = lambda:[root.destroy(),U.main()])
b.pack(side = "top")

#creation
root.mainloop()