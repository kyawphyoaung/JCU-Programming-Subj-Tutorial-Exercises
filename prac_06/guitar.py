"""
Do-from-scratch Exercises
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        self.age = 2019-self.year
        return self.age

    def is_vintage(self, age):
        if age > 50:
            return True
        else:
            return False

