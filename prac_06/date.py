"""
Practice & Extension Work
"""

class Date:
    def __init__(self,day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}:{}:{}".format(self.day, self.month, self.year)

    def add_days(self, n):
        self.day += n
        while self.day > 30:
            if self.day > 30:
                self.day -= 30
                self.month +=1
            if self.month > 12:
                self.month -= 12
                self.year +=1
        return self.day, self.month, self.year