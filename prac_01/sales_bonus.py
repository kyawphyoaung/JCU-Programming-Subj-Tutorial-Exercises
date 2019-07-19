"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: S$ \n"))
tenbounus = sales*0.1
fifteen = sales*0.15
while sales > 0 :
    if sales < 1000 :
        sales += tenbounus
        salary = sales
        print("Your salary is : S$", salary)
        sales = float(input("Enter Sales: S$ \n"))
    else :
        sales += fifteen
        salary = sales
        print("Your salary is : S$", salary)
        sales = float(input("Enter Sales: S$ \n"))
