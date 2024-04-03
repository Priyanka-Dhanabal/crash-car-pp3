from colorama import Fore
import random
from constant import CAR_BRAND, MAX_ATTEPMTS
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
            typewriter_effects("Okay!, Lets Start!")
            typewriter_effects("Remember: secret word is based on Car Brands")
            return False
        else:
            typewriter_effects("Invalid choice: Please enter 'Y' or 'N'.\n")


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
            print(f"""*Only one letter is allowed to be entered.
It must be an alphabet or '-', Try again !*""")
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
            secret_word += (" _ ")
    return secret_word.upper()


def start_game(word):
    '''
    this function manages the game, updates the word status
    and provide required feedback for bthe user
    '''
    attempts = MAX_ATTEPMTS
    guess = False
    letters_guessed = set()
    print(Fore.YELLOW + art.stages[attempts-1])
    print(Fore.RESET)
    print()
    print(display_secret_word(word, letters_guessed))
    while not guess and attempts > 1:
        letter = get_single_letter()
        if letter in letters_guessed:
            typewriter_effects(f"You already guessed the letter before.\n")
            attempts -= 1
            print(Fore.YELLOW + art.stages[attempts-1])
            print(Fore.RESET)
        elif letter in word:
            typewriter_effects(f"Great!!! {letter} that is in the word.\n")
        else:
            typewriter_effects(f"{letter} is not in the word. TRY AGAIN!\n")
            attempts -= 1
            print(Fore.YELLOW + art.stages[attempts-1])
            print(Fore.RESET)
        letters_guessed.add(letter)
        secret_word = display_secret_word(word, letters_guessed)
        print(secret_word)
        print()
        print(f"Guessed letters are: {', '.join(letters_guessed)}")
        print(f"You have {attempts-1} attempts left.\n")
        if word == secret_word:
            guess = True
    if guess:
        print(Fore.GREEN + f"{win}\n")
    else:
        print(Fore.RED + f"{lost}\nThe word was {word}\n")
    print(Fore.RESET)

def play_again():
    '''
    Function to choose if the user wants to play again or quit the game
    '''
    while True:
        user_choice = input("Do you wish to play again? (Y/N) \n").upper()
        if user_choice == 'Y':
            typewriter_effects("Awesome!, Lets try again.")
            return True
        elif user_choice == 'N':
            return False
        else:
            typewriter_effects("Invalid choice. Please enter 'Y' or 'N'.")


def show_welcome_msg():
    """
    Display LOGO and initial welcome messages.
    """
    welcome_page()
    typewriter_effects("WELCOME TO CUT-2-CHASE")
    typewriter_effects("Coded by Priyanka Dhanabal\n")
    time.sleep(1)
    typewriter_effects("You are on the run from a heist!")
    typewriter_effects("Try not to get caught, GOOD LUCK !!\n")
    time.sleep(1)


def take_user_name_input():
    '''
    Function to request and check a user's name and return it.
    '''
    user_name = ''
    while True:
        user_name = input("What is your name? \n")
        if user_name == "":
            typewriter_effects("You dont want to disclose your name?\n")
            typewriter_effects("HMMM... lets say 'CHAMP'")
            user_name = "Champ"
            break
        elif not user_name.isalpha():
            typewriter_effects("We need a valid name!")
        else:
            break
    return user_name


def init_game(username):
    '''
    Function to generate a random word and provide it
    to the start game function. Also displays if user 
    wish to play again and exits.
    '''
    while True:
        random_word = choose_random_word(CAR_BRAND)
        clear_screen()
        start_game(random_word)
        if not play_again():
            typewriter_effects(f"Thanks for playing {username}!\n")
            sys.exit("Please click Run Program to Play again!")


def main():
    '''
    Function to call all other functions.
    '''
    show_welcome_msg()
    user_name = take_user_name_input()
    typewriter_effects(f"""\nGREAT!! Hi {user_name.upper().strip()},
Ready to DRIVE !!\n""")
    time.sleep(1)
    initial_game_rules()
    time.sleep(1)
    init_game(user_name)


main()
