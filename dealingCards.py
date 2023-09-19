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

    numberOfDrawing = 2

    while True:
        for i in range(numberOfDrawing):
            cardUser = random.choice(list(components.cards.keys()))
            usersHand.append(cardUser)

            cardDealer = random.choice(list(components.cards.keys()))
            dealersHand.append(cardDealer)

        print(usersHand)
        print(dealersHand)
        cardsSum = 0
        for j in range(2):
            if j == 0:
                hand = usersHand
            else:
                # after the cycle goes off for the second round, this will be asigned for user, as the total is calculated in first round
                usersSum = cardsSum
                hand = dealersHand

            cardsSum = 0
            for i in hand:
                if type(i) is int:
                    cardsSum += i
                else:
                    if i == 'J' or i == 'Q' or i == 'K':
                        cardsSum += 10
                    else:
                        if cardsSum > 10:
                            cardsSum += 1
                        else:
                            cardsSum += 11
            # this one will be assigned twice, but as this for with 'j' will go twice, the second one will be for dealer
            dealersSum = cardsSum

        print(f"Users sum = {usersSum}")
        print(f"Dealers sum = {dealersSum}")

        print("Dealer: ???")
        print(functions.cardsRender("blank, " + str(dealersHand[0])))
        print(f"You: {usersSum}")
        print(functions.cardsRender(str(usersHand[0]) + ", " + str(usersHand[1])))
        break