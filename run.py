# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from car_brand import CAR_BRAND

def initial_game_rules():
    '''
    Requesting user to provide input whether 
    user wants to read the game rules.
    '''

    while True:
        user_input = input("Do you want to read the rules for this game? (Y/N) \n").lower()
        if user_input == 'y':
            print("rules\n")
            return True

        elif user_input == 'n':
            print("Lets Start!\n")
            return False
        
        else:
            print("Invalid choice: Please enter 'Y' or 'N'.\n")

def choose_random_word(list_of_words):
    '''
    Selects random word from the list provided.
    '''
    return random.choice(list_of_words).upper()

def get_signle_letter():
    '''
    checks if the user input is valid,
    one letter and a alphabet is provided
    '''
    allowed_letter = 'abcdefghijklmnopqrstuvwxyz-'
    while True:
        letter = input("Please enter a letter: \n")
        if letter in allowed_letter and len(letter) == 1:
            break
        else:
            print(f"Only one letter is allowed to be entered and it must be an alphabet or '-'.\nYou entered {letter}. Try again!! \n")
        
    return letter

def display_secret_word(word, letters_guessed):
    '''
    Shows the initial state of the word.
    unknown letter are shown as underscore and guessed letter will be displayed.
    '''
    secret_word = ''
    
        


get_signle_letter()