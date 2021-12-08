import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly choses from the list
    while '-' in word or ' ' in word: # if the word has a space or a dash keep guessing until we have a single word
        word = random.choice(words)

    return(word).upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #lettters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 9

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        # ''.join(['a','b','cd']) ---> ' a b cd '
        print('You have', lives, 'lives left \nYou have used these letters: ',' '.join(used_letters))

        # what current word is (ie ---> W _ R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]                
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 #takes away a life if wrong
                print('\nYour letter,', user_letter,'is not in the word')
                    
        elif user_letter in used_letters:
            print('\nYou have already used that character. Please try again')

        else:
            print('\nInvalid character. Please try again.')

    # gets here when len(word_letters) == 0 or when lives == 0

    if lives == 0:
        print('You have died :(')

    print('You guessed the word', word, '!!')

hangman()

