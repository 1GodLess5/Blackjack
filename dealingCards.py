import time
import functions
import components
import random
import os


# main function
def dealingCards(usersBet: float, usersBalance: float):
    usersBalance -= usersBet
    usersHand = []
    dealersHand = []

    os.system("clear")
    functions.gameLogo()

    print(functions.formattingConsole("YELLOW"))
    print(f"Your bet: {usersBet}€")
    print(functions.formattingConsole("END"))

    # init of user
    usersHand = userDealt(usersHand)
    # init of dealer and printing
    dealersHand = dealersCards(False, dealersHand)
    usersPrint(usersHand)

    # usersFunctionality() outcome
    functions.keyHint()
    count, outCome = usersFunctionality(usersHand, dealersHand, usersBet)

    # deciding who is the winner
    os.system("clear")
    functions.gameLogo()

    if outCome == "finished":
        usersBalance = outComeFinished(usersHand, dealersHand, usersBet, usersBalance)
    elif outCome == "double":
        usersBet = usersBet * 2
        usersBalance = outComeFinished(usersHand, dealersHand, usersBet, usersBalance)
    elif outCome == "surrender":
        usersBet = usersBet / 2
        usersBalance += usersBet
        print(functions.formattingConsole("GREEN, BOLD"))
        print(f"YOU DID SURRENDER, {usersBet}€ WILL BE REFUNDED.")
        print(functions.formattingConsole("END"))
    elif outCome == "even":
        usersBalance += usersBet
        print(functions.formattingConsole("BLUE, BOLD"))
        print(f"YOU CHOSE TO PLAY EVEN, {usersBet}€ WILL BE REFUNDED.")
        print(functions.formattingConsole("END"))

    # after finishing updating users balance based on who won
    time.sleep(3)
    return usersBalance


# function for dealing cards to dealer
def dealersCards(isPlayerDone: bool, dealersHand: list):
    count = 0

    while count < 17 and isPlayerDone == False:
        cardDealer = random.choice(list(components.cards.keys()))
        dealersHand.append(cardDealer)

        count = countingCards(dealersHand)

    if isPlayerDone == False:
        print("Dealer: ???")
        print(functions.cardsRender("blank, " + str(dealersHand[0])))
        # returns dealersHand for it to be stored outside the function and used later
        return dealersHand
    else:
        count = countingCards(dealersHand)
        print(f"Dealer: {count}")
        cardsToRender = functions.printCardsFromList(dealersHand)
        print(functions.cardsRender(cardsToRender))
        # returns count, because when user will be done, I will need to check for the scores to decide the winner
        return count


# function for counting cards
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


# deals 2 cards for user, "init" for user
def userDealt(usersHand: list):
    for i in range(2):
        cardUser = random.choice(list(components.cards.keys()))
        usersHand.append(cardUser)

    return usersHand


# prints out users count and his cards
def usersPrint(usersHand: list):
    usersCardsToPrint = functions.printCardsFromList(usersHand)
    usersCount = countingCards(usersHand)

    print(f"You: {usersCount}")
    print(functions.cardsRender(usersCardsToPrint))


# this function is used for users game -> hit, double etc.
def usersFunctionality(usersHand: list, dealersHand: list, usersBet: float):
    count = countingCards(usersHand)

    while True:
        move = input("What do you want to do, according to hint? ").lower()

        match move[0]:
            # hit -> continues till user reaches 21
            case 'h':
                cardUser = random.choice(list(components.cards.keys()))
                usersHand.append(cardUser)
                count = countingCards(usersHand)
                usersPrint(usersHand)

                if count >= 21:
                    return usersHand, "finished"
            case 's':
                return usersHand, "finished"
            # double -> if available, user gets one more cards and then quits
            case 'd':
                if len(usersHand) == 2:
                    print(functions.formattingConsole("YELLOW"))
                    print(f"Your new bet: {usersBet}€")
                    print(functions.formattingConsole("END"))

                    cardUser = random.choice(list(components.cards.keys()))
                    usersHand.append(cardUser)

                    return usersHand, "double"
                else:
                    print(functions.formattingConsole("RED, BOLD"))
                    print("This move is unavailable due to rules!")
                    print(functions.formattingConsole("END"))
            case 'f':
                return usersHand, "surrender"
            case 'e':
                if count == 21 and dealersHand[0] == 'A':
                    return usersHand, "even"
                else:
                    print(functions.formattingConsole("RED, BOLD"))
                    print("This move is unavailable due to rules!")
                    print(functions.formattingConsole("END"))
            case _:
                print(functions.formattingConsole("RED, BOLD"))
                print("Invalid move! Please try again.")
                print(functions.formattingConsole("END"))


# deciding who wins, based on scores
def whoWon(usersCount: int, dealersCount: int):
    if usersCount > 21:
        return "dealer"
    elif dealersCount > 21 and usersCount != 21:
        return "user"
    elif usersCount == dealersCount:
        return "tie"
    elif usersCount == 21:
        return "blackjack"
    elif usersCount > dealersCount:
        return "user"
    elif usersCount < dealersCount:
        return "dealer"


# prints out dealers and users cards, message for user who won + his loss/ win bet
def outComeFinished(usersHand:list, dealersHand: list, usersBet:float, usersBalance: float):
    dealersCount = dealersCards(True, dealersHand)
    usersCount = countingCards(usersHand)
    usersPrint(usersHand)

    winner = whoWon(usersCount, dealersCount)
    if winner == "user":
        usersBet = usersBet * 2
        print(functions.formattingConsole("GREEN, BOLD"))
        print(f"YOU WON {usersBet}€!")
        print(functions.formattingConsole("END"))
        usersBalance += usersBet
    elif winner == "tie":
        print(functions.formattingConsole("BLUE, BOLD"))
        print(f"IT'S A TIE, YOU WILL RECEIVE YOUR BET {usersBet}€ BACK.")
        print(functions.formattingConsole("END"))
        usersBalance += usersBet
    elif winner == "blackjack":
        usersBet = usersBet * 2.5
        usersBalance += usersBet
        print(functions.formattingConsole("PURPLE, BOLD"))
        print(f"YOU GOT BLACKJACK! YOU WON {usersBet}€!")
        print(functions.formattingConsole("END"))
    else:
        print(functions.formattingConsole("RED, BOLD"))
        print(f"YOU LOST {usersBet}€.")
        print(functions.formattingConsole("END"))

    return usersBalance
