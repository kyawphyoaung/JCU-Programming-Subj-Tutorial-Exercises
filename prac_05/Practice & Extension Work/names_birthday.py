"""
Convert parallel lists into a dictionary...
by Kyaw Phyo Aung (13822414)

"""
informations = {}
names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]


def main():
    auto_output()
    manual_input()

def auto_output():
    i = 0
    while i < len(names):
        name = names[i]
        dob = dates_of_birth[i]
        informations = dict_fun(name, dob)
        i += 1
    print("")
    for people in informations:
        print("{} was born on {}".format(people, informations[people]))


def manual_input():
    count = 1
    while count < 6:
        name = input("Enter names :")
        dob = input("Enter date of births")
        informations[name] = dob
        count += 1
    # print(informations)
    print("")
    for people in informations:
        print("{} was born on {}".format(people, informations[people]))


def dict_fun(name, dob):
    informations[name] = dob
    return informations
main()
