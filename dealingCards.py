import functions
import components
import random
import os

def dealingCards(usersBet: float):
    usersHand = []
    dealersHand = []

    os.system("clear")
    functions.gameLogo()

    print(functions.formattingConsole("YELLOW"))
    print(f"Your bet: {usersBet}€")
    functions.keyHint()
    print(functions.formattingConsole("END"))

    for i in range(2):
        cardUser = random.choice(list(components.cards.keys()))
        usersHand.append(cardUser)

        cardDealer = random.choice(list(components.cards.keys()))
        dealersHand.append(cardDealer)

    print("Dealer: ???")