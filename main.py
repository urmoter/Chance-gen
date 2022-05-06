import HnT as H
import OtS as O
import sys
import numpy
import tkinter as tk
A: int=int(input("Number dice(1) or coin flip (2): "))
if A==1:
    O.ND()
elif A==2:
    H.CT()
else:
    sys.exit("invalid input!")    