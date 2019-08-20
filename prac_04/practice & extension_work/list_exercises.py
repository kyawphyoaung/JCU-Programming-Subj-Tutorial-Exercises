import sys

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
MENU = """ [N]umbers
[U]sernames
"""

def main():
    print(MENU)
    option = input(">>> ")
    if option == "n":
        num()
    elif option == "u":
        user_validate()
    else:
        print("Invalid Input")
        sys.exit()


def num():
    count = 1
    numbers = []
    number = int(input("Number{} :".format(count)))
    while number > 0:
        number = int(input("Number{} :".format(count)))
        numbers.append(number)
        count += 1
    find_nums(numbers)
    avg_num(numbers)

def find_nums(names):
    print("The first number is {}".format(names[0]))
    print("The last number is {}".format(names[4]))
    names.sort()
    print("The smallest number is {}".format(names[0]))
    print("The largest number is {}".format(max(names)))


def avg_num(names):
    total = sum(names)
    quantity = len(names)
    average = total / quantity
    print("The average of the numbers is {}".format(average))

def user_validate():
    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
        main()
    else:
        print("Access denied")
        user_validate()

main()