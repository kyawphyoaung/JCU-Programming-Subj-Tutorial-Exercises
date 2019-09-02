from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    print("My guitar: {0}, first made in {1}".format(name, year))
    print("")
    guitar = Guitar(name, year, cost)
    another = Guitar("Another Giutar", 2012)

    print("{} {} - Expected {}. Got {}".format(guitar.name, "get_age()", "97", guitar.get_age()))
    print("{} {} - Expected {}. Got {}".format(another.name, "get_age()", "7", another.get_age()))

    print("{} {} - Expected {}. Got {}".format(guitar.name, "is_vintage()", "True", guitar.is_vintage(guitar.get_age())))
    print("{} {} - Expected {}. Got {}".format(another.name, "is_vintage()", "False", another.is_vintage(another.get_age())))

main()