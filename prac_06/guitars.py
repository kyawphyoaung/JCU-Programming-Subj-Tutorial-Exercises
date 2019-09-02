from prac_06.guitar import Guitar


def main():
    guitars = []
    # vintage_string = ""
    g_name = input("Name :")
    while g_name:
        g_year = int(input("Year :"))
        g_cost = float(input("Cost :"))
        guitars.append(Guitar(g_name, g_year, g_cost))
        print("{} ({}) : ${:.2f} added".format(g_name, g_year, g_cost))
        g_name = input("Name :")

    print("")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("...snip...")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage(int(guitar.get_age())):
            vintage_string = "(vintage)"
        print("Guitar {0}: {1.name:<20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guitar, vintage_string))


main()