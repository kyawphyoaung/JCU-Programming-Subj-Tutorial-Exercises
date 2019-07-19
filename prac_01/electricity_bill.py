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
    tariff = int(input("Which tariff? 11 or 31: "))
    dailyuse = float(input("\nEnter daily use in kWh: "))
    days = float(input("\nEnter number of billing days: "))
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928
    if(tariff == 11):
        bill = TARIFF_11 * dailyuse * days
        print("Estimated bill: ", bill)
    elif(tariff == 31):
        bill = TARIFF_31 * dailyuse * days
        print("Estimated bill: ", bill)
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