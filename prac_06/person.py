"""
Practice & Extension Work
"""

class Person:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def __str__(self):
        return "{}| {}| {}".format(self.f_name, self.l_name, self.age)
