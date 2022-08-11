import random

def select(filename):
    test_file=list(open(str(filename),"r"))
    word=str((random.choice(test_file)).strip())
    
    return word
    

def check(word,guess,output):
    length=len(word)
    loss=0
    done=0
    contains=0
    for x in range(length):
        if guess==word[x]:
            output=output[:x] + guess + output[x+1:]
            contains=1
            
    if contains==0:
        loss=1
    if output==word:
        done=1
            
    return output,loss,done
    


def play():
    print("Welcome to hangman you will have 6 lives to guess the word!")
    guess=str(input("Please enter your guess... "))
    done=0
    lives=6
    word=select("words.txt")
    length=len(word)
    output=("*")*(length)
    while done==0 and lives>0:
        output,loss,done=check(word,guess,output)
        lives=lives-loss
        if done==1:
            print("Congrats you won!! The word was " + word + ".")
            return
        if lives==0:
            print("You ran out of lives! Thanks for playing!")
            return
        print("This is what you have so far: " + output)
        print("You have " + str(lives) + " lives left.")
        if done==0:
            guess=str(input("Please enter your next guess... "))
    
    
    
play()