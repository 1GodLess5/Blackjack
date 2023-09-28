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
    os.system("clear")
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
    while True:
        usedName = False
        user = input("Enter your name: ")

        if len(user) < 5:
            print(functions.formattingConsole("RED, BOLD"))
            print("Username must contain at least 5 letters.")
            print(functions.formattingConsole("END"))
        elif checkForSpecial(user) == True:
            print(functions.formattingConsole("RED, BOLD"))
            print("Username must not contain any special characters!")
            print(functions.formattingConsole("END"))
        else:
            with open("users.txt") as file:
                for line in file:
                    name = line.split(" ")[0]
                    if name == user:
                        print(functions.formattingConsole("YELLOW"))
                        print("This username is already taken, please try again.")
                        print(functions.formattingConsole("END"))
                        usedName = True
            if usedName != True:
                break

    while True:
        containsNumber = False
        password = getpass.getpass("Enter password - at least 8 characters, 1 special character and 1 number: ")

        for i in password:
            if ord(i) >= 48 and ord(i) <= 57:
                containsNumber = True

        if checkForSpecial(password) == False:
            print(functions.formattingConsole("RED, BOLD"))
            print("Password must contain at least one special character!")
            print(functions.formattingConsole("END"))
        elif len(password) < 8:
            print(functions.formattingConsole("RED, BOLD"))
            print("Password must be at least 8 characters long!")
            print(functions.formattingConsole("END"))
        elif containsNumber == False:
            print(functions.formattingConsole("RED, BOLD"))
            print("Password must contain at least one number!")
            print(functions.formattingConsole("END"))
        else:
            break

    hashedPassword = hasher.hash(password)
    with open("users.txt", "a") as file:
        file.write(user + " " + str(hashedPassword) + "\n")

    print(functions.formattingConsole("GREEN, BOLD"))
    print("You have successfully created new account!")
    print(functions.formattingConsole("END"))


def checkForSpecial(stringToCheck: str):
    for character in stringToCheck:
        if ord(character) < 48 or (57 < ord(character) < 65) or (90 < ord(character) < 97) or ord(character) > 122:
            return True
    return False


account()
