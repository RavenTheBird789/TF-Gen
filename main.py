# Main File
from UNGen import ungen
from PWGen import pwgen
import time
import os

def green(text: str) -> str:
    """Returns the given text wrapped in ANSI escape codes for green color."""
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    """Returns the given text wrapped in ANSI escape codes for red color."""
    return f"\033[91m{text}\033[0m"

def bold(text: str) -> str:
    """Returns the given text wrapped in ANSI escape codes for bold formatting."""
    return f"\033[1m{text}\033[0m"

# Global Variables
equalSign = "="
x = 5
y = 3

# Trademark Decorator
def trademark(func):
    def wrapper():
        print(green(equalSign * 20))
        print(green(bold("Text File Generators")))
        print(green(equalSign * 20))
        print(red("By: RavenTheBird789"))
        print(green(equalSign * 20))
        func()
    return wrapper

# Main Function
@trademark
def main(): 
    print(green("Please select a choice from the menu below:"))
    print(green("1. Username Generator"))
    print(green("2. Password Generator"))
    print(green("3. Exit"))
    choice = input(green("Enter your choice (1-3): "))
    if choice == "1":
        os.system('clear')
        ungen();
    elif choice == "2":
        os.system('clear')
        pwgen();
    elif choice == "3":
        os.system('clear')
        print(green("Thanks for using my Text File Generation Tool! Have a nice day!"))
        time.sleep(x)
        os.system('clear')
        os._exit(0);
    else:
        os.system('clear')
        print(red("Invalid input"))
        time.sleep(y)
        os.system('clear')
main();