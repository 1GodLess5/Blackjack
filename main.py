import functions
import components
import ageChecker
import dealingCards

# welcome message, do you have an account?
# no -> age verification, rules verification, create account
# yes -> login, main menu -> 1) Play Game
#                            2) Balance (> see my balance, top out my balance, withdraw)
#                            3) Exit Game
# TODO 1) you are in accountManagement branch
# TODO    account.py in the bottom continue with TODO

# welcoming screen
functions.firstScreen()
# verifying user's age
ageChecker.main()
# user's agreement to the rules
functions.rulesConfirmation()

# getting user's balance to play with
usersBalance = functions.enterBalance()  # testing variables: usersBalance = 500, usersBet = 25
# getting user's bet for this round
usersBet = functions.usersBet(usersBalance)
# main function of this game, updates userBalance
usersBalance = dealingCards.dealingCards(usersBet, usersBalance)
print(f"Your new balance: {usersBalance}")



