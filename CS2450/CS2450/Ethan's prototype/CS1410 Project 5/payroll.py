"""
Author: Jaden Albrecht
Project: Payroll
Date: 07/21/2020
Description: This program simulates a simple payroll system.

I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitutes cheating,
and that I will receive a zero on this project if I am found in violation of this policy.
"""

'''
Include doc strings for the module and for each method in the module
'''

#import any needed modules 
from abc import ABC, abstractmethod
import os, os.path, shutil

#initiate constants
employees = []
EMPLOYEE_DATA_FILE = "d:\School\CS2450\Ethan's prototype\CS1410 Project 5\employees.csv"
TIMECARD_FILE = "d:\School\CS2450\Ethan's prototype\CS1410 Project 5\\timecards.csv"
SALES_FILE = "d:\School\CS2450\Ethan's prototype\CS1410 Project 5\\receipts.csv"
PAY_LOGFILE = "d:\School\CS2450\Ethan's prototype\CS1410 Project 5\paylog.txt"

"""Employee object class"""
class Employee:

    """Creates employee object"""
    def __init__(self, ID, first_name, last_name, address, city, state, zip, classification, salary, commission, hourly):
        self.emp_id = ID
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.classification = classification
        self.salary = float(salary)
        self.commission = float(commission)
        self.hourly = float(hourly)

        #Establish classification object
        if self.classification == '1':
            self.make_salaried(self.salary)
        elif self.classification == '2':
            self.make_commissioned(self.salary, self.commission)
        elif self.classification == '3':
            self.make_hourly(self.hourly)

    """Returns employee's ID number"""
    def getID(self):
        return self.emp_id

    """Returns employee's name"""
    def getName(self):
        return f"{self.first_name} {self.last_name}"
            
    """Returns employee's address"""
    def getAddress(self):
        return self.address

    """Returns employee's city"""
    def getCity(self):
        return self.city

    """Returns employee's state"""
    def getState(self):
        return self.state

    """Returns employee's zip code"""
    def getZip(self):
        return self.zip
    
    """Returns employee's classification object"""
    def getClass(self):
        return self.classification
    
    """Returns the employee's salary"""
    def getSalary(self):
        return self.salary

    """Return the employee's commission rate"""
    def getCommissionRate(self):
        return self.commission

    """Returns the employee's hourly payment rate"""
    def getHourlyRate(self):
        return self.hourly
    
    """Makes the employee a salaried employee"""
    def make_salaried(self, salary):
        self.salary = salary
        self.classification = Salaried(self.salary)

    """Makes the employee an hourly employee"""
    def make_hourly(self, rate):
        self.hourly = rate
        self.classification = Hourly(self.hourly)

    """Makes the employee a commissioned employee"""
    def make_commissioned(self, salary, rate):
        self.commission = rate
        self.salary = salary
        self.classification = Commissioned(self.salary, self.commission)

    """Pays the employee""" #writes output to text file
    def issue_payment(self):
        with open(PAY_LOGFILE, 'a') as fout:
            if self.getClass().compute_pay() == '0.00':
                fout.write("")
            else:
                fout.write(f"Mailing ${self.getClass().compute_pay()} to {self.getName()} at {self.getAddress()} {self.getCity()} {self.getState()} {self.getZip()}\n")

    """String representation of employee object"""
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.classification}"

"""An abstract class of a classification object for an employee"""
class Classification(ABC):

    """Constructs abstract classification object"""
    def __init__():
        pass

    """Abstract decorator method of computing an employee's payment"""
    @abstractmethod
    def compute_pay():
        pass

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
    def compute_pay(self):
        result = 0
        for time in self.timecards:
            result += self.rate * time
        return f"{result:.2f}"

    """String representation of hourly employee classification"""
    def __str__(self):
        return "Hourly Employee"

"""Class that creates a salaried classification for an employee"""
class Salaried(Classification):

    """Constructs Salaried classification object"""
    def __init__(self, salary):
        self.salary = salary

    """Computes the payment of a salaried employee"""
    def compute_pay(self):
        return f"{self.salary / 24:.2f}"

    """String representation of salaried employee classification"""
    def __str__(self):
        return "Salaried Employee"

"""Constructs a commission classification for an employee"""
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
    def compute_pay(self):
        result = 0
        for receipt in self.receipts:
            result += (self.commission_rate / 100) * receipt
        return f"{result + self.salary / 24:.2f}"

    def __str__(self):
        return "Commissioned Employee"

"""A function that adds employees to the list"""
def load_employees():
    with open(EMPLOYEE_DATA_FILE) as fin:
        for line in fin.readlines()[1:]:
            l = line.split(',')
            employees.append(Employee(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10]))

"""Adds receipts to every commissioned employee"""
def process_receipts():
    with open(SALES_FILE) as fin:
        for line in fin:
            l = line.split(',')
            emp = find_employee_by_id(l[0])
            for receipt in l[1:]:
                emp.getClass().add_receipt(receipt)

"""Adds timecards to every hourly employee"""
def process_timecards():
    with open(TIMECARD_FILE) as fin:
        for line in fin:
            l = line.split(',')
            emp = find_employee_by_id(l[0])
            for timecard in l[1:]:
                emp.getClass().add_timecard(timecard)

"""Finds an employee by their ID number"""
def find_employee_by_id(ID):#ID parameter represents a string!!!
    for employee in employees:
        if employee.getID() == ID:
            return employee

"""Pays each employee"""
def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()

run_payroll()