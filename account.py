# password and secret creating
import getpass
from passlib.hash import bcrypt
import uuid
# functions clear and time.sleep()
import os
import time
# my files
import functions
import ageChecker
# initializing hashing
hasher = bcrypt.using(rounds=13)


def account():
    """
    Main function.
    :return: Username and user's balance
    """
    hasAccount = isAccount()
    if hasAccount == 1:  # user has account
        userName, usersBalance = logIn()
        if userName == None:
            account()
        else:
            # reminding user of the rules
            functions.rulesConfirmation()
            return userName, usersBalance
    elif hasAccount == 2:  # needs to create an account
        # verifying user's age before making an account
        ageChecker.main()
        # creating an account
        userName = createAccount()
        # user's agreement to the rules
        functions.rulesConfirmation()
        # getting user's balance to play with
        usersBalance = functions.enterBalance()  # testing variables: usersBalance = 500, usersBet = 25
        functions.writeBalance(userName, usersBalance, False)
        return userName, usersBalance
    else:
        forgotPassword()
        account()



def isAccount():
    """
    Function to ask user if he wants to log in or register.
    :return: Bool
    """

    os.system("clear")
    functions.gameLogo()
    print(functions.formattingConsole("BLUE, BOLD"))
    print("LOG-IN/REGISTER")
    print(functions.formattingConsole("END"))
    print(functions.formattingConsole("YELLOW"))
    print("Do you have an account?")
    print(functions.formattingConsole("END"))

    while True:
        try:
            hasAccount = int(input("1) I have an account.\n2) I want to create an account.\n3) I forgot my password.\n"))
            if hasAccount < 1 or hasAccount > 3:
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
    """
    Creates account for user.

    Prompts user to enter username and password. Password gets hashed and stored in "users.txt".
    :return: Username for the further game.
    """
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

    os.system("clear")
    createSecret(user)

    print(functions.formattingConsole("GREEN, BOLD"))
    print("You have successfully created new account, you will be redirected to rules confirmation in 5 seconds!")
    print(functions.formattingConsole("END"))
    time.sleep(5)

    return user


def checkForSpecial(stringToCheck: str):
    """
    Function to check if user doesn't enter invalid characters into his username.
    :param stringToCheck: New username to be checked.
    :return: Bool: True - Contains invalid characters
    """
    for character in stringToCheck:
        if ord(character) < 48 or (57 < ord(character) < 65) or (90 < ord(character) < 97) or ord(character) > 122:
            return True
    return False


def logIn():
    """
    Log-in to the game.
    :return: Username and User's Balance for further game.
    """
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
                for line in file:
                    splittedLine = line.split(" ")
                    name = splittedLine[0]
                    passwordCheck = splittedLine[1]
                    balance = splittedLine[2]

                    if name == userName and hasher.verify(password, passwordCheck) == True:
                        print(functions.formattingConsole("GREEN, BOLD"))
                        print("You have successfully logged in your account!")
                        print("In 5 seconds you will be redirected to rules section.")
                        print(functions.formattingConsole("END"))
                        time.sleep(7)
                        return name, balance
            # if the "with" statement which goes through the file fails, one attempt gets down
            passwordTries -= 1
            print(functions.formattingConsole("RED, BOLD"))
            print(f"Incorrect password, please try again. Remaining tries: {passwordTries}")
            print(functions.formattingConsole("END"))
            if passwordTries == 0:
                print(functions.formattingConsole("RED, BOLD"))
                print(f"You have failed to verify your password. Try again or make new account in 5 seconds.")
                print(functions.formattingConsole("END"))
                time.sleep(7)
                return None, None
    else:
        print(functions.formattingConsole("RED, BOLD"))
        print("This username does not exist.")
        print(functions.formattingConsole("END"))
        time.sleep(5)
        return None, None

def forgotPassword():
    """
    If user forgots his password.
    :return: Bool -> True: Successfully restored
    """
    userExists = False

    userName = input("Enter your name: ")
    with open("users.txt", "r") as file:
        for line in file:
            name = line.split(" ")[0]
            if name == userName:
                userExists = True

    secretTries = 3
    if userExists == True:
        while secretTries > 0:
            secret = getpass.getpass("Enter your secret code: ")

            with open("secrets.txt", "r") as file:
                for line in file:
                    splittedLine = line.split(" ")
                    name = splittedLine[0]
                    secretCheck = splittedLine[1].strip("\n")

                    if name == userName and hasher.verify(secret, secretCheck) == True:
                        print(functions.formattingConsole("GREEN, BOLD"))
                        print("You have successfully entered the secret code!")
                        print(functions.formattingConsole("END"))
                        restoringPassword(userName)
                        print(functions.formattingConsole("GREEN, BOLD"))
                        print("You have successfully restored your account!")
                        print("In 5 seconds you will be redirected to log in window.")
                        print(functions.formattingConsole("END"))
                        time.sleep(7)
                        return True
            # if the "with" statement which goes through the file fails, one attempt gets down
            secretTries -= 1
            print(functions.formattingConsole("RED, BOLD"))
            print(f"Incorrect secret code, please try again. Remaining tries: {secretTries}")
            print(functions.formattingConsole("END"))
            if secretTries == 0:
                print(functions.formattingConsole("RED, BOLD"))
                print(f"You have failed to verify your secret code. Try again or make new account in 5 seconds.")
                print(functions.formattingConsole("END"))
                time.sleep(7)
                return False
    else:
        print(functions.formattingConsole("RED, BOLD"))
        print("This username does not exist.")
        print(functions.formattingConsole("END"))
        time.sleep(5)
        return False


def restoringPassword(userName: str):
    """
    Creates new password and updates "users.txt"
    :param userName: User's name
    :return: None
    """
    while True:
        containsNumber = False
        password = getpass.getpass("Enter new password - at least 8 characters, 1 special character and 1 number: ")

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

    with open("users.txt", "r") as file:
        allLines = file.readlines()

        counter = 0
        for line in allLines:
            name = line.split(" ")[0]
            if name == userName:
                newLine = allLines[counter]
                break
            else:
                counter += 1

    newLine = newLine.split(" ")
    newLine[1] = hashedPassword
    allLines[counter] = newLine[0] + " " + newLine[1].strip("\n") + " " + newLine[2]

    with open("users.txt", "w") as file:
        file.writelines(allLines)

def createSecret(userName: str):
    """
    Creates secret code to restore password.
    :param userName: Users's name
    :return: None
    """
    secretCode = uuid.uuid4()
    secretCode = str(secretCode)

    print(functions.formattingConsole("BOLD, YELLOW"))
    print(f"Dear {userName} it's important to emphasize that the secret code you're about to receive")
    print("is crucial for restoring your password if needed,")
    print("so please make sure to save it in a secure place and avoid sharing it with anyone.")
    print("This code ensures you have uninterrupted access to your game.")
    print(functions.formattingConsole("END"))
    time.sleep(5)
    print(functions.formattingConsole("GREEN, BOLD"))
    print(f"Your secret code:\n{secretCode}")
    print(functions.formattingConsole("END"))
    input("Press enter when you have saved your code.\n")

    hashedSecretCode = hasher.hash(secretCode)
    with open("secrets.txt", "a") as file:
        file.write(userName + " " + hashedSecretCode + "\n")

    os.system("clear")
