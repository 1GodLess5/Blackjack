import functions
import components
import ageChecker
import dealingCards

# TODO 1) dealingCards.py()


# welcoming screen
# functions.firstScreen()
# verifying user's age
# ageChecker.main()
# user's agreement to the rules
# functions.rulesConfirmation()

# getting user's balance to play with
# usersBalance = functions.enterBalance()
usersBalance = 500
# getting user's bet for this round
usersBet = functions.usersBet(usersBalance)
dealingCards.dealingCards(usersBet)




