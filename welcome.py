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


def instructions():
    print("="*80)
    print("*" * 33 + " INSTRUCTIONS " + "*" * 33)
    print("""
    1. You are on a run while the police are chasing you.
    2. Your goal is to guess the brand of a car within 5 tries.
    3. Try to guess the car brand and escape, or the police will catch you.
    """)
    print("*" * 80)
    print("="*80)
    print("\n")
