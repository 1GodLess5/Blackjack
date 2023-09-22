import getpass
import os
from passlib.hash import bcrypt
import functions
import string
hasher = bcrypt.using(rounds=13)


def account():
    hasAccount = isAccount()
    if hasAccount == 1:  # user has account
        pass
    else:  # needs to create an account
        createAccount()


def isAccount():
    os.system("CLEAR")
    print(functions.formattingConsole("YELLOW"))
    print("Do you have an account?")
    print(functions.formattingConsole("END"))

    while True:
        try:
            hasAccount = int(input("1) I have an account.\n2) I want to create an account.\n"))

            if hasAccount < 1 or hasAccount > 2:
                print(functions.formattingConsole("RED, BOLD"))
                print("Invalid input!")
                print(functions.formattingConsole("END"))
                continue
        except ValueError:
            print(functions.formattingConsole("RED, BOLD"))
            print("Invalid input!")
            print(functions.formattingConsole("END"))
            continue
        break

    return hasAccount


def createAccount():
    # file = open("users.txt", "r")
    #
    # for line in file:
    #     print(line.rstrip())
    #
    # file.close()

    while True:
        user = input("Enter your name: ")

    # password = getpass.getpass("Enter password: ")
    # hashedPassword = hasher.hash(password)
    #
    # print(user)
    # print(password)
    # print(hashedPassword)

def checkForSpecial(stringToCheck: str):
    for character in stringToCheck:
        if ord(character) < 48 or (57 < ord(character) < 65) or (90 < ord(character) < 97) or ord(character) > 122:
            return True
    return False


account()
