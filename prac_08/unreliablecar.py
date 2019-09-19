import random
from prac_08.car import Car


class Unreliablecar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel, reliability)

    def drive(self, distance):
        number = random.randint(1, 101)
        if number >= self.reliabilty:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
