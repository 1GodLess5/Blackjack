import functions
import components
import ageChecker
import dealingCards


# TODO 1) make nice users decision map (play again, exit, ? maybe login ?)

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



