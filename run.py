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

def get_single_letter():
    '''
    requests and checks if the user input is valid,
    one letter and if alphabet is provided
    '''
    allowed_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXZY-'
    while True:
        letter = input("Please enter a letter: \n").upper()
        if letter in allowed_letter and len(letter) == 1:
            print(f"You have entered: {letter}")
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
    for letter in word:
        if letter in letters_guessed:
            secret_word+=letter
        else:
            secret_word+=("_")
    
    return secret_word.upper()

def letters_guessed_update(letters_guessed, letter):
    """
    This functions add two args the guess that the player guessed so far
    to the set of guessed letters.
    """
    letters_guessed.add(letter)


def start_game(word):
    '''
    this function manages the game, updates the word status
    and provide required feedback for bthe user
    '''

    attempts = 7
    guess = False
    letters_guessed = set()

    print(display_secret_word(word, letters_guessed))

    while not guess and attempts > 0:
        letter = get_single_letter()
        if letter in letters_guessed:
            print(f"You already guessed the letter before. Check out the letters guessed: {letters_guessed}")
        elif letter in random_word:
            print(f"Great!!! {letter} that is in the word.")
        else:
            print(f"{letter} is not in the word. TRY AGAIN!\n")
            attempts -= 1
            
        letters_guessed_update(letters_guessed, letter)

        secret_word = display_secret_word(word, letters_guessed)
        print(f"You have {attempts} attempts left.\n")
        print(secret_word)

        print(f"Guessed letters are: {', '.join(letters_guessed)}")

        if word == secret_word:
            guess = True
        
    if guess == True:
        print("\nYOU WON..!\n")
    else:
        print(f"\nYOU LOSE..! The word was {word}\n")   


random_word = choose_random_word(CAR_BRAND)
game = start_game(random_word)

print(game)
