"""
Electricity bill estimator v2.0 by Kyaw Phyo Aung (13822414)
"""
tariff_costs = {"11": "0.244618", "31": "0.136928"}
tariffs = []
def fun_one():
    print("Electricity bill Estimator")
    cents = float(input("Enter cents per kWh: "))
    dailyuse = float(input("\nEnter daily use in kWh: "))
    days = float(input("\nEnter number of billing days: "))
    cost = cents*0.01
    bill = cost*dailyuse*days
    print("Estimated bill: ",bill)

def fun_two():
    print("Electricity bill Estimator 2.0")

    # Reterieve key from tariff dictionary
    for tariff in tariff_costs:
        tariffs.append(tariff)

    # show only from dictionary
    tariff = int(input("Which tariff? {} or {} :".format(tariffs[0],tariffs[1])))
    dailyuse = float(input("\nEnter daily use in kWh: "))
    days = float(input("\nEnter number of billing days: "))

    if(tariff == 11):
        bill = int(tariffs[0]) * dailyuse * days
        print("Estimated bill: ", bill)
    elif(tariff == 31):
        bill = int(tariffs[1]) * dailyuse * days
        print("Estimated bill: ", bill)
        print("")
    else:
        print("Tariff Wrong!!")

MENU = """C - Cents per kWh
T - Tariff
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        fun_one()
    elif choice == "T":
        fun_two()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")