import os
import functions
import dealingCards
import account

# TODO 1) you are in usersMenu branch
# TODO    menu.py continue with TODOs
# FUTURE
# TODO In the account.py create Forgot password -> After creating new account, create random string and pass it to
# TODO the user, tell him to save it if he forgets the password. Hash the string and save it into new file "secrets.txt"
# TODO when user forgets password, ask him for this code instead and make him create new password

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



