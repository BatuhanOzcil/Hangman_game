import time
name = input("Please enter your name: ")
time.sleep(0.5)
print(f"Hello {name} welcome to the hangman !")
time.sleep(0.5)
word=("spiderman")
guesses=""
turns=10
while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed += 1
    if failed ==0:
        print( f"\nYou win {name} !")
        print(f"The word is: {word} ")
        break
    print()
    guess=input("Guess a letter: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong,you have "+str(turns),"guesses left")
        if turns == 0:
            print(f"You lost {name} :( ")