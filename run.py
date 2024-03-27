# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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


initial_game_rules()
