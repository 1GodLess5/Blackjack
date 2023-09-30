import functions
import os


# welcome message, do you have an account?
# no -> age verification, rules verification, create account
# yes -> login, main menu -> 1) Play Game
#                            2) Balance (> see my balance, top out my balance, withdraw)
#                            3) Exit Game

def main():
    # TODO match of the printMenu() decision
    pass

def printMenu():
    os.system("clear")
    functions.gameLogo()
    print(functions.formattingConsole("BLUE, BOLD"))
    print("MENU:")
    print(functions.formattingConsole("END"))
    print(functions.formattingConsole("YELLOW"))
    print("1 - Play Game")
    print("2 - My Balance")
    print("3 - Read Rules")
    print("4 - Exit Game")
    print(functions.formattingConsole("END"))

    while True:
        try:
            usersDecision = int(input("Enter your choice: "))

            # TODO FINISH THIS ERROR HANDLING userDecision > 4 < 1
        except ValueError:
            print(functions.formattingConsole("BOLD, RED"))
            print("Invalid input!")
            print(functions.formattingConsole("END"))