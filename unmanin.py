import sys
import OtS as O
import HnT as H
import tkinter as tk
def BAT():
    A: int=int(input("Number dice(1) or coin flip (2): "))
    if A==1:
        O.ND()
    elif A==2:
        H.CT()
    else:
        sys.exit("invalid input!")  