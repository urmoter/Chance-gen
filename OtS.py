import random
import time
import sys
def ND():
    trials: int = int(input("How many trials?: "))
    if trials <= 0:
        sys.exit("invalid input!")
    else:
        print("Loading...")
        for i in range(101):
            print(i,"%")
            i = i+1
            time.sleep(0.1)
        print("Loaded!")
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
        print("One appeard: ",One," times!")
        print("Two appeared: ",Two," times!")
        print("Three appeard: ",Three," times!")
        print("Four appeared: ",Four," times!")
        print("Five appeard: ",Five," times!")
        print("Six appeared: ",Six," times!")