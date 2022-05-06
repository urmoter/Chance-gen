import random
import time
import sys
def CT():
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
        print("Heads appeard: ",Head," times!")
        print("Tails appeared: ",Tails," times!")