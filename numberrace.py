import random

number = random.randint(1, 10)
tries = 1

uname = input("Hello, What is your username?")

print("Hello", uname + ".", )

question = input("Would you like to play a game? [Y/N]")
if question == "n":
    print("oh... okay")

if question == "y":
    print("Ok, I'm thinking of a number between 1 and 9...")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess lower...")
if guess < number:
    print("Guess higher...")
while guess != number:
    tries += 1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess higher")
if guess == number:
    print("You are right: you win! The number was", number, \
          "and it only", tries, "tries!")
          
           