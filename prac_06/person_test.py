"""
Practice & Extension Work
"""

from prac_06.person import Person


def main():
    persons = []
    count = int(input("How many people do you want to input? \n>>>"))
    while count > 0:
        f_name = input("First name :")
        l_name = input("Last name :")
        age = int(input("Age :"))
        persons.append(Person(f_name, l_name, age))
        # print(Person(f_name, l_name, age))
        count -= 1

    # persons.append((Person("Kyaw", "Phyo", 19)))
    # persons.append((Person("Akari", "Naing", 20)))
    # persons.append((Person("Soe", "Nadi", 18)))
    persons.sort(key=lambda x: x.age)
    print("")
    print("Informations:")
    print("FirstName | LastName | Age")
    print("==========================")
    for i, person in enumerate(persons):
        print("{1.f_name:<9} | {1.l_name:<8} | {1.age:<3}".format(i + 1, person))


main()
