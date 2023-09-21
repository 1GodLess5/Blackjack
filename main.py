import functions
import components
import ageChecker
import dealingCards

# TODO 1) CHECK FOR BUGS IN dealingCards.py, DIDN'T TEST IT THROUGH PROCCESS, BECAUSE IT WASN'T POSSIBLE
# TODO 2) dont forget to merge after finishing, because you are working in dealingCardsRework
# TODO 3) make nice users decision map (play again, exit, ? maybe login ?)
# welcoming screen
# functions.firstScreen()
# verifying user's age
# ageChecker.main()
# user's agreement to the rules
# functions.rulesConfirmation()

# getting user's balance to play with
# usersBalance = functions.enterBalance()
usersBalance = 500
usersBet = 25
# getting user's bet for this round
# usersBet = functions.usersBet(usersBalance)
usersBalance = dealingCards.dealingCards(usersBet, usersBalance)
print(f"Your new balance: {usersBalance}")



