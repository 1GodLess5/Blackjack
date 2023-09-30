import os
import time
from datetime import date
import functions


def underAge(isUnderage: bool):
    """
    Prints out message.

    If user is underage, the game shuts down.
    :param isUnderage: Bool: True -> User is underage, False -> User is adult
    :return: None
    """
    if isUnderage:
        print(functions.formattingConsole("BOLD, RED"))
        exit("I'm sorry, but individuals under the age of 18 are not permitted to participate in hazardous games due to safety and legal reasons.")
    else:
        print(functions.formattingConsole("BOLD, GREEN"))
        print("You have successfully verified your age, feel free to enjoy a game of Blackjack with my Python program!")
        print("You will be redirected to account creating in 5 seconds.")
        print("Waiting...")
        print(functions.formattingConsole("END"))
        time.sleep(7)


def main():
    """
    Based on input checks for users age.
    :return: None
    """
    os.system("clear")
    functions.gameLogo()

    print(functions.formattingConsole("BOLD, YELLOW"))
    print("Welcome to the game! To ensure responsible gaming, please enter your birthday to verify that you're 18 years or older,\n"
          "as the game could potentially be addictive. Your well-being is important to us.")
    print(functions.formattingConsole("END"))

    dateToday = str(date.today())

    listOfDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while True:
        leap = False

        try:
            yearOfBirth = int(input("Enter year of birth:\t"))
            monthOfBirth = int(input("Enter month of birth:\t"))

            if monthOfBirth < 1 or monthOfBirth > 13:
                print(functions.formattingConsole("BOLD, RED"))
                print("There are only 12 months, please try your input again.")
                print(functions.formattingConsole("END"))
                continue

            dayOfBirth = int(input("Enter day of birth:\t"))

            if monthOfBirth == 2:
                if yearOfBirth % 4 == 0:
                    if yearOfBirth % 100 == 0:
                        if yearOfBirth % 400 == 0:
                            leap = True
                        else:
                            if dayOfBirth > 28 or dayOfBirth < 1:
                                print(functions.formattingConsole("BOLD, RED"))
                                print(f"Year {yearOfBirth} is not a leap year, so it can't have more than 28 day.")
                                print("Please try your input again.")
                                print(functions.formattingConsole("END"))

                                continue
                    else:
                        leap = True
                else:
                    if dayOfBirth > 28 or dayOfBirth < 1:
                        print(functions.formattingConsole("BOLD, RED"))
                        print(f"Year {yearOfBirth} is not a leap year, so it can't have more than 28 days.")
                        print("Please try your input again.")
                        print(functions.formattingConsole("END"))

                        continue

            if leap == True and monthOfBirth == 2 and dayOfBirth <= 29:
                pass

            elif dayOfBirth > listOfDays[monthOfBirth - 1] or dayOfBirth < 1:
                print(functions.formattingConsole("BOLD, RED"))
                print(f"{monthOfBirth}. month has only {listOfDays[monthOfBirth - 1]} days.")
                print("Please try your input again.")
                print(functions.formattingConsole("END"))

                continue

            break
        except ValueError:
            print(functions.formattingConsole("BOLD, RED"))
            print("You have entered invalid input, try it again.")
            print(functions.formattingConsole("END"))

    checkingDate = dateToday.split("-")

    for i in range(len(checkingDate)):
        checkingDate[i] = int(checkingDate[i])
    if checkingDate[0] - yearOfBirth < 18:
        underAge(True)
    elif checkingDate[0] - yearOfBirth == 18:
        if checkingDate[1] < monthOfBirth:
            underAge(True)
        elif checkingDate[1] == monthOfBirth:
            if checkingDate[2] < dayOfBirth:
                underAge(True)
            else:
                underAge(False)
        else:
            underAge(False)
    else:
        underAge(False)
