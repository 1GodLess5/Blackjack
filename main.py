import os
import functions
import dealingCards
import account

# TODO 1) you are in usersMenu branch
# TODO    menu.py continue with TODOs


# welcoming screen
functions.firstScreen()
# account management
userName, usersBalance = account.account()
usersBalance = float(usersBalance)
# getting user's bet for this round
os.system("clear")
functions.gameLogo()
usersBet = functions.usersBet(usersBalance)
# main function of this game, updates userBalance
usersBalance = dealingCards.dealingCards(usersBet, usersBalance)
print(f"Your new balance: {usersBalance}")
functions.writeBalance(userName, usersBalance, True)


