import functions
import components
import random
import os

def dealingCards(usersBet: float):
    usersHand = []
    dealersHand = [5, 4, 'J']

    os.system("clear")
    functions.gameLogo()

    print(functions.formattingConsole("YELLOW"))
    print(f"Your bet: {usersBet}€")
    print(functions.formattingConsole("END"))

    numberOfDrawing = 2

    dealersCards(True, dealersHand)

    # while True:
    #     for i in range(numberOfDrawing):
    #         cardUser = random.choice(list(components.cards.keys()))
    #         usersHand.append(cardUser)
    #
    #         cardDealer = random.choice(list(components.cards.keys()))
    #         dealersHand.append(cardDealer)
    #
    #     print(usersHand)
    #     print(dealersHand)
    #     cardsSum = 0
    #     for j in range(2):
    #         if j == 0:
    #             hand = usersHand
    #         else:
    #             # after the cycle goes off for the second round, this will be asigned for user, as the total is calculated in first round
    #             usersSum = cardsSum
    #             hand = dealersHand
    #
    #         cardsSum = 0
    #         for i in hand:
    #             if type(i) is int:
    #                 cardsSum += i
    #             else:
    #                 if i == 'J' or i == 'Q' or i == 'K':
    #                     cardsSum += 10
    #                 else:
    #                     if cardsSum > 10:
    #                         cardsSum += 1
    #                     else:
    #                         cardsSum += 11
    #         # this one will be assigned twice, but as this for loop with 'j' will go twice, the second one will be for dealer
    #         dealersSum = cardsSum
    #
    #     print(f"Users sum = {usersSum}")
    #     print(f"Dealers sum = {dealersSum}")
    #
    #
    #
    #     print(f"You: {usersSum}")
    #     print(functions.cardsRender(str(usersHand[0]) + ", " + str(usersHand[1])))

    #    functions.keyHint()
        # TODO to think: Change the dealing for dealer so he right away gets all the cards, because it doesnt matter
        # TODO           I mean, only user decided where to stand and where not, pc has to get cards if the sum is lower than 17 anyway :)        # TODO 1: ADD usersFunctionality() here
        # TODO 2: change value of numberOfDrawing to 1, think how you will divide the drawing between user and dealer as
        # TODO    dealer has different rules
    #    break

def dealersCards(isPlayerDone: bool, dealersHand: list):
    count = 0

    while count < 17 and isPlayerDone == False:
        cardDealer = random.choice(list(components.cards.keys()))
        dealersHand.append(cardDealer)

        count = countingCards(dealersHand)
        print(dealersHand)
        print(count)

    if isPlayerDone == False:
        print("Dealer: ???")
        print(functions.cardsRender("blank, " + str(dealersHand[0])))

        return dealersHand
    else:
        count = countingCards(dealersHand)
        print(f"Dealer: {count}")
        printCardsFromList(dealersHand)

def countingCards(hand: list):
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

    return cardsSum

def printCardsFromList(cardList: list):
    stringToPrint = ""
    count = len(cardList)

    for i in cardList:
        count -= 1
        stringToPrint += str(i)

        if count != 0:
            stringToPrint += ", "

    print(stringToPrint)

    return stringToPrint
