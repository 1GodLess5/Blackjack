# password creating
import getpass
from passlib.hash import bcrypt
# functions clear and time.sleep()
import os
import time
# my files
import functions
import ageChecker
# initializing hashing
hasher = bcrypt.using(rounds=13)


def account():
    hasAccount = isAccount()
    if hasAccount == 1:  # user has account
        userName, usersBalance = logIn()
        if userName == None:
            account()
        else:
            # reminding user of the rules
            functions.rulesConfirmation()
            return userName, usersBalance
    else:  # needs to create an account
        # verifying user's age before making an account
        ageChecker.main()
        # creating an account
        userName = createAccount()
        # user's agreement to the rules
        functions.rulesConfirmation()
        # getting user's balance to play with
        usersBalance = functions.enterBalance()  # testing variables: usersBalance = 500, usersBet = 25

        # TODO CHECK OUT FOR BUGS -> YOU WILL FIND ALL PASSWORDS IN users.txt -> I FEEL LIKE THE HASH CONFIRMATION FAILS SOMETIMES
        # TODO FINISH THIS FILE, ADD WRITING USERS BALANCE IN FILE? AFTER CREATING THE ACCOUNT





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
            with open("users.txt", "r") as file:
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
    print("You have successfully created new account, you will be redirected to rules confirmation in 5 seconds!")
    print(functions.formattingConsole("END"))
    time.sleep(5)

    return user


def checkForSpecial(stringToCheck: str):
    for character in stringToCheck:
        if ord(character) < 48 or (57 < ord(character) < 65) or (90 < ord(character) < 97) or ord(character) > 122:
            return True
    return False

def logIn():
    userExists = False

    userName = input("Enter your name: ")
    with open("users.txt", "r") as file:
        for line in file:
            name = line.split(" ")[0]  # THIS LINE [0] is the first out of split, [1] would be for password...
            if name == userName:
                userExists = True

    passwordTries = 3
    if userExists == True:
        while passwordTries > 0:
            passwordCheck = ""
            password = getpass.getpass("Enter your password: ")
            with open("users.txt", "r") as file:
                name = line.split(" ")[0]
                passwordCheck = line.split(" ")[1]
                balance = line.split(" ")[2].strip("\n")

                if name == userName and hasher.verify(password, passwordCheck) == True:
                    print(functions.formattingConsole("GREEN, BOLD"))
                    print("You have successfully logged in your account!")
                    print("Your balance: " + balance)
                    print(functions.formattingConsole("END"))
                    return name, balance
            # if the "with" statement which goes through the file fails, one attempt gets down
            passwordTries -= 1
            print(functions.formattingConsole("RED, BOLD"))
            print(f"Incorrect password, please try again. Remaining tries: {passwordTries}")
            print(functions.formattingConsole("END"))
            if passwordTries == 0:
                print(functions.formattingConsole("RED, BOLD"))
                print(f"You have failed to verify your password. Try again or make new account in 10 seconds.")
                print(functions.formattingConsole("END"))
                time.sleep(10)
                return None, None
    else:
        print(functions.formattingConsole("RED, BOLD"))
        print("This username does not exist.")
        print(functions.formattingConsole("END"))
        time.sleep(10)
        return None, None


account()
