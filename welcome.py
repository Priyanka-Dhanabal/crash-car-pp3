from colorama import Fore


def welcome_page():
    print(Fore.CYAN + r"""
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║ ░█▀▀░█░█░▀█▀░░░░░▀▀▄░░░░░█▀▀░█░█░█▀█░█▀▀░█▀▀ ║
    ║ ░█░░░█░█░░█░░▄▄▄░▄▀░░▄▄▄░█░░░█▀█░█▀█░▀▀█░█▀▀ ║
    ║ ░▀▀▀░▀▀▀░░▀░░░░░░▀▀▀░░░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀ ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """)
    print(Fore.RESET)


def instructions():
    print("""
    ╔═════════════════════════════════════════════════════════════════════╗
    ║                         INSTRUCTIONS:                               ║
    ║                                                                     ║
    ║  1. You are on a run while the police are chasing you.              ║
    ║  2. Your goal is to guess the brand of a car within 5 tries.        ║
    ║  3. Guess the car brand and escape, or the police will catch you.   ║
    ║  4. Every time you guess a wrong letter, the police car gets closer.║
    ║  5. You can guess only one letter at a time.                        ║
    ╚═════════════════════════════════════════════════════════════════════╝
    \n""")
