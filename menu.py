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
    balanceMenu = 0
    while True:
        menu = printMenu(1)
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
                while balanceMenu != 4:
                    balanceMenu = printMenu(2)


def printMenu(whichMenu: int):
    os.system("clear")
    functions.gameLogo()
    print(functions.formattingConsole("BLUE, BOLD"))
    if whichMenu is 1:
        print("MENU:")
        print(functions.formattingConsole("END"))
        print(functions.formattingConsole("YELLOW"))
        print("1 - Play Game")
        print("2 - My Balance")
        print("3 - Read Rules")
        print("4 - Exit Game")
    else:
        print("BALANCE MENU:")
        print(functions.formattingConsole("END"))
        print(functions.formattingConsole("YELLOW"))
        print("1 - See My Balance")
        print("2 - Top Up My Balance")
        print("3 - Withdraw")
        print("4 - Back To Main Menu")
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

def balanceStats(userName: str, usersBalance: float, usersDecision: int):
    match usersDecision:
        case 1:
            os.system("clear")
            functions.gameLogo()
            print(functions.formattingConsole("YELLOW"))
            print(f"Your balance is: {usersBalance} €")
            print(functions.formattingConsole("END"))
            input("Press enter to continue.")
        case 2:
            os.system("clear")
            functions.gameLogo()
            print(functions.formattingConsole("YELLOW"))
            print(f"Your current balance is: {usersBalance} €")
            print(functions.formattingConsole("END"))

            addMoney = input("How much € you want to top up?\t")
            usersBalance += addMoney
            functions.writeBalance(userName, usersBalance)

            print(functions.formattingConsole("BOLD, GREEN"))
            print("You have successfully topped up your balance!")
            print(functions.formattingConsole("END"))
            print(functions.formattingConsole("YELLOW"))
            print(f"Your new balance is: {usersBalance} €")
            print(functions.formattingConsole("END"))
            input("Press enter to continue.")
