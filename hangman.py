import random
from re import A
import string
from words import words


def valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = valid_word(words)
    word_letters = set(word) # letters in word
    letter = set(string.ascii_uppercase)
    used_letters = set() # letters used by user


    lives =6 


    while len(word_letters)>0 and lives>0:
        print('You have',lives,'lives left and','you have used these letters: ',' '.join(used_letters))
        word_list=[a if a in used_letters else '_' for a in word]
        print('Current word: ', ' '.join(word_list))
        
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in letter - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives=lives-1

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        
        else:
            print('Invalid input.')

    if lives:
        print('You have guessed the word',word,'!!')
    else:
        print('You failed, the word was',word)

    
hangman()