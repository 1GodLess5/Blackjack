import random
import components
import gameRules
import time
import os
import random

def cardsRender(cardToDraw: str, numberOfcards: int):
    cards = cardToDraw.split(", ")
    print(cards)
    renderedCard = ''''''
    j = 0

    # TODO, YOU FINISHED HERE, HAVE TO THINK ABOUT HOW YOU GONNA RENDER THE CARDS IN ONE LINE, INSTEAD OF EACH CARD ON ITS LINE
    if cards[0] == "blank":
        for i in range(numberOfcards):
            renderedCard += f''' ___  '''
        renderedCard += "\n"
        for i in range(numberOfcards):
            if i == 0:
                renderedCard += "|## |"
            else:
                renderedCard += f" |{cards[i]}  |"
        renderedCard += "\n"
        for i in range(numberOfcards):
            if i == 0:
                renderedCard += "|###|"
            else:
                renderedCard += f""

    # cardShape = components.cardShapes[random.randint(0, 7)]
    # renderedCard = f''' ___\n|{cardToDraw}  |\n| {cardShape} |\n|__{cardToDraw}|'''
    print(renderedCard)
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
    print("Available actions: (H)it\t(S)tand\t\t(D)ouble\t(F) to surrender\t(E)ven money")

def usersBet(usersBalance: float):
    print("The lowest bet at this table is 25€.")
    print(f"Your remaining balance is {usersBalance}€.")

    while True:
        try:
            bet = float(input("How much would you like to bet?\t"))
            if bet < 25:
                print(formattingConsole("BOLD, RED"))
                print("The lowest bet at this table is 25€.")
                print(formattingConsole("END"))

                continue
            elif bet > usersBalance:
                print(formattingConsole("BOLD, RED"))
                print("Your balance is lower than your bet.")
                print(formattingConsole("END"))

                continue
            break
        except ValueError:
            print(formattingConsole("BOLD, RED"))
            print("You have entered invalid input.")
            print("Please try it again.")
            print(formattingConsole("END"))

    return bet

def dealingCards(usersBet: float):
    usersHand = []
    dealersHand = []

    os.system("clear")
    gameLogo()

    print(formattingConsole("YELLOW"))
    print(f"Your bet: {usersBet}€")
    keyHint()
    print(formattingConsole("END"))

    for i in range(2):
        cardUser = random.choice(list(components.cards.keys()))
        usersHand.append(cardUser)

        cardDealer = random.choice(list(components.cards.keys()))
        dealersHand.append(cardDealer)

    print("Dealer: ???")
    # TODO: FINISH THIS FUNCTION, BUT FIRST FINISH THE RENDERING :)

cardsRender("blank, 1", 2)
# dealingCards(150)



