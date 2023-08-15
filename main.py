import functions
import components
import ageChecker


# TODO 1) cardsRender(cardToDraw: str, numberOfcards: int) -> FINISH THIS FUNCTION
# TODO 2) dealingCards()


# welcoming screen
functions.firstScreen()
# verifying user's age
ageChecker.main()
# user's agreement to the rules
functions.rulesConfirmation()

# getting user's balance to play with
usersBalance = functions.enterBalance()

# getting user's bet for this round
usersBet = functions.usersBet(usersBalance)





