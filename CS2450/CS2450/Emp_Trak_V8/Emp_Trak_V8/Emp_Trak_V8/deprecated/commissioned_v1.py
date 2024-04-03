#Import any needed modules
import salaried_v1
from abc import abstractmethod


"""Commission classification object for an employee"""
class Commissioned(Salaried):

    """Creates Commission classification object"""
    def __init__(self, salary, commission_rate):
        Salaried.__init__(self, salary)
        self.commission_rate = commission_rate
        self.receipts = []

    """Returns commissioned employee's commission rate"""
    def getRate(self):
        return self.commission_rate

    """Adds receipts to the list of receipts"""
    def add_receipt(self, amount):
        try:
            self.receipts.append(float(amount))
        except:
            print("Invalid amount.")
            return None

    """Computes the payment for a commissioned employee"""
    def compute_payment(self):
        result = 0
        for receipt in self.receipts:
            result += (self.commission_rate / 100) * receipt
            print("result", result);
        return f"{result + self.salary / 24:.2f}"

    def __str__(self):
        return "Commissioned Employee"
