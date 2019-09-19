from prac_08.silverservicetaxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.calu_fare())


main()