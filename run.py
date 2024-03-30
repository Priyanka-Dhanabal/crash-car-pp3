# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from car_brand import CAR_BRAND
from welcome import *
import time
import art
import sys
import os


def typewriter_effects(text):
    '''
    Create typing effect to improve user experience.
    '''
    for letter in text:
        if letter == '\n':
            print("\n")
        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
        time.sleep(0.06)
    print()


def clear_screen():
    '''
    To clear screen after ever round to enhance user experience
    '''
    while True:
        typewriter_effects("Press C to clear the screen")
        clear = input("").lower()
        if clear == 'c':
            os.system("clear")
            break 


def initial_game_rules():
    '''
    Requesting user to provide input whether
    user wants to read the game rules.
    '''
    while True:
        user_input = input("Do you want to read the rules?(Y/N)\n").lower()
        if user_input == 'y':
            time.sleep(1)
            print()
            instructions()
            return True
        elif user_input == 'n':
            print("GOOD, Lets Start!\n")
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
        print()
        letter = input("Please enter a letter: \n").upper()
        if letter in allowed_letter and len(letter) == 1:
            print(f"You have entered: {letter}")
            break
        else:
            print(f"""Only one letter is allowed to be entered.
            It must be an alphabet or '-'.
            You entered {letter}. Try again!!""")
    return letter


def display_secret_word(word, letters_guessed):
    '''
    Shows the initial state of the word.
    unknown letter are shown as underscore and
    guessed letter will be displayed.
    '''
    secret_word = ''
    for letter in word:
        if letter in letters_guessed:
            secret_word += letter
        else:
            secret_word += ("_")
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
    attempts = 6
    guess = False
    letters_guessed = set()
    print(art.stages[attempts-1])
    print()
    print(display_secret_word(word, letters_guessed))
    while not guess and attempts > 1:
        letter = get_single_letter()
        if letter in letters_guessed:
            typewriter_effects(f"You already guessed the letter before.\n")
            attempts -= 1
            print(art.stages[attempts-1])
        elif letter in word:
            typewriter_effects(f"Great!!! {letter} that is in the word.\n")
        else:
            typewriter_effects(f"{letter} is not in the word. TRY AGAIN!\n")
            attempts -= 1
            print(art.stages[attempts-1])
        letters_guessed_update(letters_guessed, letter)
        # print(f"Check out the letters guessed: {letters_guessed}")
        secret_word = display_secret_word(word, letters_guessed)
        #print(f"You have {attempts} attempts left.\n")
        
        print(secret_word)
        print()
        print(f"Guessed letters are: {', '.join(letters_guessed)}")
        if word == secret_word:
            guess = True
    if guess:
        typewriter_effects("\nYOU WON..!\n")
    else:
        typewriter_effects(f"\nYOU LOSE..! The word was {word}\n")


def play_again():
    '''
    Function to choose if the user wants to play again or quit the game
    '''
    while True:       
        try:
            user_choice = input("Do you wish to play again? (Y/N) \n").upper()
            if user_choice == 'Y':
                typewriter_effects("Awesome!, Lets try again.")
                return True
            elif user_choice == 'N':
                return False
        except ValueError:
            print("Invalid choice. Please enter 'Y' or 'N'.")


def main():
    '''
    Function to call all other functions.
    start the game with welcome and interacts with the user.
    Requests user if they want to play again.
    '''
    welcome_page()
    typewriter_effects("WELCOME TO CUT-2-CRASH")
    typewriter_effects("coded by Priyanka\n")
    time.sleep(1)
    typewriter_effects("You are one the run from a heist!")
    typewriter_effects("Try not to get caught, GOOD LUCK !!\n")
    time.sleep(1)
    while True:
        user_name = input("What is your name? \n")
        if user_name == "":
            typewriter_effects("""You dont want to disclose your name?\n
            HMMM... lets say 'CHAMP'""")
            user_name = "Champ"
            break
        elif not user_name.isalpha():
            typewriter_effects("We need a valid name!")
        else:
            break
    typewriter_effects(f"""\nGREAT!! Hi {user_name.upper().strip()},
    Ready to DRIVE !!\n""")
    time.sleep(1)
    initial_game_rules()
    time.sleep(1)
    while True:
        random_word = choose_random_word(CAR_BRAND)
        clear_screen()
        start_game(random_word)
        if not play_again():
            typewriter_effects(f"Thanks for playing {user_name}!")
            sys.exit("Please click Run Program to run again!")


main()
