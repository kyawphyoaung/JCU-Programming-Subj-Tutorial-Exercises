from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi

MENU = """Let's Drive!
q)uit, c)hoose taxi, d)rive
"""

current_taxi = None
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
bill_to_date = 0


def main():
    global bill_to_date
    print(MENU)
    option = input(">>>")
    while option != "q":
        if option == "c":
            taxi_available()
            current_taxi = int(input("Choose taxi:"))
            print("Bill to Date", bill_to_date)
            print("")
            option = input(MENU)
        elif option == "d":
            bill_to_date = drive(current_taxi, bill_to_date)
            print("")
            option = input(MENU)
    print("Total Trip cost: ${:.2f}".format(bill_to_date))
    print(taxi_now())


def taxi_available():
    taxi_count = 0
    print("Taxis available:")
    for taxi in taxis:
        print("{} - {}".format(taxi_count, taxi))
        taxi_count += 1


def taxi_now():
    taxi_count = 0
    print("Taxis available:")
    for taxi in taxis:
        print("{} - {}".format(taxi_count, taxi))
        taxi_count += 1


def drive(choose_taxi, bill_to_date):
    drive_km = int(input("Drive how far?"))
    for taxi in taxis:
        if taxi == taxis[choose_taxi]:
            taxi.drive(drive_km)
            bill = taxi.get_fare()
            print("Your Prius trip cost you ${}".format(bill))
            bill_to_date += bill
            print("Bill to date: ${}".format(bill_to_date))
    return bill_to_date


main()
