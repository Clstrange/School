
#Import any needed modules
from abc import abstractmethod


"""Class that creates a salaried classification for an employee"""
class Salaried(Classification):

    """Constructs Salaried classification object"""
    def __init__(self, salary):
        self.salary = salary

    """Computes the payment of a salaried employee"""
    def compute_payment(self):
        return f"{self.salary / 24:.2f}"

    """String representation of salaried employee classification"""
    def __str__(self):
        return "Salaried Employee"
