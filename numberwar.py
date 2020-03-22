import sys
import time
import random

#variables

score = 0
score1 = 0
target = 2

while 1:

    number = random.randint(1,5)

    guess = int(input("Player one : "))
    guess1 = int(input("Player two : "))

    print("")
    print("The number was ", number)
    print("")

    if guess == number:
        score = score + 1

        print("Player one score : ", score)
        print("Player two score : ", score1)

    elif guess1 == number:
        score1 = score1 + 1
        print("Player one score : ", score1)
        print("Player one score : ", score)

    else:
        print("")
        print("none of the guess were correct!")
        
    if score == target:
        print("")
        print("Player one has won the game")
        print("")
        sys.exit()

    elif score1 == target:
        print("")
        print("Player two has won the game")
        print("")
        sys.exit()