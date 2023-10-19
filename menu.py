import time
import functions
import os
import dealingCards

# welcome message, do you have an account?
# no -> age verification, rules verification, create account
# yes -> login, main menu -> 1) Play Game
#                            2) Balance (> see my balance, top out my balance, withdraw)
#                            3) Exit Game


def main(userName: str, usersBalance: float):
    # TODO match of the printMenu() decision\
    while True:
        menu = printMenu()
        match menu:
            case 1:
                os.system("clear")
                functions.gameLogo()
                # getting user's bet for this round
                usersBet = functions.usersBet(usersBalance)
                usersBalance = dealingCards.dealingCards(usersBet, usersBalance)
                print(functions.formattingConsole("BOLD, YELLOW"))
                print(f"Your new balance: {usersBalance}")
                print(functions.formattingConsole("END"))
                functions.writeBalance(userName, usersBalance)
                input("Press enter to continue.")
            case 2:
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

            if usersDecision < 1 or usersDecision > 4:
                print(functions.formattingConsole("BOLD, RED"))
                print("Invalid input!")
                print(functions.formattingConsole("END"))
                continue
        except ValueError:
            print(functions.formattingConsole("BOLD, RED"))
            print("Invalid input!")
            print(functions.formattingConsole("END"))
            continue
        break

    return usersDecision