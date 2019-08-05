"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
import random

MIN_LENGTH = 5 # change from 2 to 5
MAX_LENGTH = 15 # change from 6 to 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")

    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False

    # Checking the length of password
    if(len(password) > MAX_LENGTH or len(password) < MIN_LENGTH):
        checkit = False

    # to count when finding user's password
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # start checking user enterd password
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if(char.isupper()):
            count_upper +=1
        elif(char.islower()):
            count_lower +=1
        elif(char.isdigit()):
            count_digit +=1
        else:
            checkit = False

    # TODO: if any of the 'normal' counts are zero, return False

    # if password contain lower,upper and digit, count will not be zero anymore
    if (count_lower != 0 and count_upper != 0 and count_digit != 0):
        checkit = True
    else:
        checkit = False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # check special chars required or not
    # find special chars in user enterd password
    if(SPECIAL_CHARS_REQUIRED):
        for char in password:
            if(char in SPECIAL_CHARACTERS):
                count_special +=1
            else:
                count_special +=1

    # check count sepcial and return values
    # return false if it's zero
    if(count_special != 0 ):
        checkit = True
    else:
        checkit = False

    # if we get here (without returning False), then the password must be valid
    return checkit


main()
