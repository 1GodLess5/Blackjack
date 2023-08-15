import random
import components
import gameRules
import time
import os

def cardsRender(cardToDraw: str):
    cardShape = components.cardShapes[random.randint(0, 7)]
    renderedCard = f''' ___\n|{cardToDraw}  |\n| {cardShape} |\n|__{cardToDraw}|'''

    return renderedCard


def firstScreen():
    gameLogo()
    input("Press any key to continue.")


def gameLogo():
    print(formattingConsole("BLUE"))
    print("Blackjack, by GodLess https://github.com/1GodLess5/Blackjack")
    print(components.logo)
    print(formattingConsole("END"))


def rulesConfirmation():
    while True:
        os.system("clear")
        gameLogo()

        print(formattingConsole("BOLD, RED"))
        print(gameRules.rules)
        print(formattingConsole("END"))

        doesAgree = input("Do you agree to the rules?\n(y)es or (n)o:\t").lower()

        if doesAgree[0] == "y":
            print(formattingConsole("BOLD, GREEN"))
            print("Welcome aboard! Get ready to dive into the exciting world of blackjack with our Python game. Enjoy and good luck!")
            print("The game will start in 5 seconds...")
            print(formattingConsole("END"))
            time.sleep(5)

            break
        elif doesAgree[0] == "n":
            print(formattingConsole("BOLD, RED"))
            exit("I'm sorry, but in order to play the blackjack Python game, you must agree to and follow the rules provided.")
        else:
            print("You have made a mistake in your answer, please try it again.")
            time.sleep(3)



def formattingConsole(format: str):
    listOfRequirements = format.split(", ")
    counter = 0
    finalString = ""

    for requirement in listOfRequirements:
        if counter > 0:
            finalString += " + "

        finalString += f"components.Color.{requirement}"

        counter += 1

    return eval(finalString)

def enterBalance():
    usersBalance = 0

    os.system("clear")
    gameLogo()

    while True:
        try:
            usersBalance = float(input("Enter your balance in €:\t"))

            if usersBalance < 25:
                print(formattingConsole("BOLD, RED"))
                print("Sorry, but the lowest bet is 25 euro.")
                print(formattingConsole("END"))

                continue
            else:
                print(formattingConsole("BOLD, GREEN"))
                print(f"You have successfully topped up your balance to {usersBalance}€.")
                print("The game will start shortly...")
                print(formattingConsole("END"))
                time.sleep(5)

            break
        except ValueError:
            print(formattingConsole("BOLD, RED"))
            print("You have entered invalid input.\tPlease try it again.")
            print(formattingConsole("END"))

    return usersBalance

def keyHint():
    print("(H)it\t(S)tand\t(D)ouble\t(F) to surrender\t(E)ven money")












