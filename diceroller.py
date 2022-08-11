import random

def dice(sides):
    roll=str((random.randint(1,sides)))
    return ("You rolled a " + roll)
    

def play():
    again=1
    while again==1:
        sides=int(input("Please enter how many sides your die has..."))
        output=dice(sides)
        print (output)
        again=int(input("""Enter a '1' if you want to play again or a
                        '0' if you don't... """))


play()   