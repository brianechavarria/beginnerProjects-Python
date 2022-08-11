import random

def computerPlayer():
    computerTurn=random.randint(1,3)
    return computerTurn

def check(playerTurn,computerTurn):
    test=playerTurn-computerTurn
    if playerTurn==computerTurn:
        return ("You drew with the computer.")
    if test==-2 or test==1:
        return ("Congratulations you beat the computer!")
    if test==2 or test==-1:
        return ("I'm sorry you lost to the computer.")
    

def play():
    print("""Hello welcome to this game of Rock Paper Scissors against
          the computer""")
    done=0
    while done==0:
        playerTurn=int(input("""Please enter a '1' for rock, a '2' for paper,
                             or a '3' for scissors... """))
        computerTurn=computerPlayer()
        output=check(playerTurn,computerTurn)
        print (output)
        done=int(input("""Enter a '0' if you want to play again,
                       or a '1' if you don't... """))
                         



play()
    