income_list = []
income_total_list = []
profit = 0
income = 0


def main():
    calculate_income()
    print("")
    print("Income Report")
    print("--------------")
    user_output()

def calculate_income():
    try:
        mmcount = 1
        totalincome = 0
        print("How many months?")
        months = int(input(">>>"))
        while mmcount <= months:
            income = float(input("Enter income for month {}: ".format(mmcount)))
            mmcount += 1
            income_list.append(income)
            totalincome += income
            income_total_list.append(totalincome)
    except ValueError:
        print("Invalid Input Try Again!")
        calculate_income()

def user_output():
    for i in range(len(income_total_list)):
        mmcount = i + 1
        print("Month  {0} - Income: $ {1:10.2f}     Total: $ {2:10.2f}".format(mmcount, income_list[i],
                                                                               income_total_list[i]))

main()