import random

def numGen(x):       # Game 1: Computer generates random number which the user tries to figure out.
    global random_number
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_number:
            print("Woah Woah there too high!")
        elif guess < random_number:
            print("Alright a little higher bud...")
    print(f"Correct !!!! You have guessed the number {random_number} correctly!!")

def compGuess(x):    # Game 2: User creates a number which the computer tries to guess
    global low 
    global high 
    global feedback
    low = 1
    high = x
    feedback = ""
    print(f"Guess a number between 1 and {x}...")
    gotIt = input("Got it? Y/N: ").upper()
    if gotIt != "Y":
        return
    while feedback != "Y":
        guess = random.randint(low,high)
        feedback = input(f"Was {guess} the correct number? Y/N: ").upper()
        if feedback == "N":
            feedback = input(f"Is {guess} too high or low? H/L: ").upper()
            if feedback == "H":
                high = guess - 1 
            elif feedback == "L":
                low = guess - 1
    print("Congrats! You have proven a computer has telepathy!!! ")


def gameSel():     # Last function to let the user decide which game they want to play
    print("                      THE GUESS GAME!")
    print("1. The computer will pick a number which you have to guess.")
    print("2. You choose a number which the computer will telepathically guess.")
    x = 100
    whichGame = input("   Which game would you like to play? 1 or 2: ")
    if whichGame == "1":
        print(numGen(x))
    elif whichGame == "2":
        print(compGuess(x))
    else :
        return

objectOne = gameSel()
print(objectOne)


