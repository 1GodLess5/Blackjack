import functions
import account
import menu

# TODO 1) you are in usersMenu branch
# TODO    menu.py continue with TODOs


# welcoming screen
functions.firstScreen()
# account management
userName, usersBalance = account.account()
usersBalance = float(usersBalance)
# main loop of the game
menu.main(userName, usersBalance)
