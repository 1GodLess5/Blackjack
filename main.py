import functions
import components
import dealingCards
import account
# welcome message, do you have an account?
# no -> age verification, rules verification, create account
# yes -> login, main menu -> 1) Play Game
#                            2) Balance (> see my balance, top out my balance, withdraw)
#                            3) Exit Game
# TODO 1) you are in accountManagement branch
# TODO    account.py in the account() continue with TODOs

# welcoming screen
functions.firstScreen()
# account management
userName, usersBalance = account.account()

# getting user's bet for this round
usersBet = functions.usersBet(usersBalance)
# main function of this game, updates userBalance
usersBalance = dealingCards.dealingCards(usersBet, usersBalance)
print(f"Your new balance: {usersBalance}")



