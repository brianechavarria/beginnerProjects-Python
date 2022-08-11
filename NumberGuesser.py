import random


def game():
    tries=0
    guess=-1
    goal=random.randint(0,100)
    done=0
    print("""The computer has selected a random number between 0 and 100,
          you're job is to guess the number within 10 tries.""")
    while done==0:
        guess=int(input("Please enter your guess..."))
        response=test(guess, goal)
        if response==1:
            print("You guessed correctly")
            done=1
        if response==2:
            print("You guessed too low")
        if response==3:
            print("You guessed too high")
        tries+=1
        if tries==10:
            print("You ran out of guesses")
            done=1
            


def test(guess, goal):
    testValue=guess
    value=goal
    if value==testValue:
        return 1
    if value>testValue:
        return 2
    if value<testValue:
        return 3
    

    

game()