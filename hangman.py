import random

def play_again():
    answer = input('Would You like to play again? yes/n').lower()
    if answer == 'y' or 'yes':
        play_game()
    else:
        pass

def get_word():
    words = ('snake', 'car', 'boy', 'life', 'trash', 'punch', 'launch')
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False
    print('The word contains', len(word), 'letters.')
    print(len(word) * '*')
    while guessed == False and tries > 0:
        print('You have' + str(tries) + 'tries')
        guess = input('Please enter one letter or the full word.').lower()
        #1 - user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a letter.')
            elif guess in letters_guessed:
                print('You have already gussed this letter before')
            elif guess not in word:
                print('That letter is not part of the word: (')
                letters_guessed.append(guess)
                tries -=1 
            elif guess in word:
                print('Well done that letter exists in the word!')
                letters_guessed.append(guess)
            else:
                print('Please try it again')
        
        #2 - user inputs a full word
        elif len(guess) == len(word):
            if guess == word:
                print('Well done, You have guessed the word')
                guessed = True
            else:
                print('Sorry, that was not the word we were looking for! :(')
                tries -= 1

        #3 - user inputs letters where this total number of letters =/= total number of letters in the word.
        else:
            print('The lenght of your guess is not the same as the lenght of the word we\'re looking for.')

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print('Well done, You gussed the word!')
            guessed = True
        elif tries == 0:
            print('You have run out of guesses and you have not quessed the word.')

play_again()
    
play_game()
