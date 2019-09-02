"""
Practice & Extension Work
"""

import sys
from prac_06.car import Car

MENU = """
 Menu:
 d) drive
 r) refuel
 q) quit
 """


def main():
    print("Let's Drive!")
    car_name = input("Enter your car name :")
    car = Car(car_name, 100)
    print(car)

    print(MENU)
    choice = input("Enter your choice :")

    while choice != "q":
        if choice == "d":
            km_drive = int(input("How many km do you wish to drive? \n>>> "))
            while km_drive < 0:
                print("Distance must be >= 0")
                km_drive = int(input("How many km do you wish to drive? \n>>> "))
            distance = car.drive(km_drive)
            if car.fuel == 0:
                print("The car drove {}km and ran out of fuel".format(distance))
            else:
                print("The car drove {}km".format(distance))
        elif choice == "r":
            refuel = int(input("How many units of fuel do you want to add to the car? \n>>> "))
            while refuel < 0:
                print("Fuel amount must be >= 0")
                refuel = int(input("How many units of fuel do you want to add to the car? \n>>> "))
            car.add_fuel(refuel)
            print(" Added {} units of fuel.".format(refuel))
        else:
            print("Invalid choice")
        print("")
        print(car)
        print(MENU)
        choice = input("Enter your choice :")

    print("Good bye The {}'s driver.".format(car.name))
    sys.exit()

main()
