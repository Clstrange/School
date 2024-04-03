
#Import any needed modules
from abc import abstractmethod


"""Class that creates an hourly classification"""
class Hourly(Classification):

    """Constructs Hourly classification object"""
    def __init__(self, rate):
        self.rate = rate
        self.timecards = []

    """Adds timecards to the list of timecards"""
    def add_timecard(self, record):
        try:
            self.timecards.append(float(record))
        except:
            print("Invalid record.")

    """Computes the payment of an hourly employee"""
    def compute_payment(self):
        print("--------" + self.rate + "--------" + len(self.timecards) )
        result = 0
        for time in self.timecards:
            result += self.rate * time
        # return f"{result:.2f}"
        return result

    """String representation of hourly employee classification"""
    def __str__(self):
        return "Hourly Employee"
