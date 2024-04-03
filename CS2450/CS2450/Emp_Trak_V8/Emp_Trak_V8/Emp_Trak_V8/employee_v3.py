'''
Feb 23
Ethan Taylor

Changes Made:
    -Changed get/set methods for classification for easier interaction with GUI
    -Changed get/set methods for pay method for easier interaction with GUI
    -Changed get methods for routing and account numbers for easier interaction with GUI
    -Added get method for just the classification object, for internal use within Employee class
    -Added forgotten set methods for salary, commission rate, and hourly rate
Changes Still Needed:
    -Account for odd formatting of employees.csv (The one provided by the
teacher doesn't separate first name and last name)
'''

#import any needed modules 
from abc import ABC, abstractmethod
from database_module import *
import os, os.path, shutil

#initiate constants
employees = []
EMPLOYEE_DATA_FILE = 'csv/employees.csv'
TIMECARD_FILE = 'csv/timecards.csv'
SALES_FILE = 'csv/receipts.csv'
PAY_LOGFILE = 'output/paylog.txt'

"""Employee object class"""
class Employee:

    """Creates employee object"""
    def __init__(self, ID, first_name, last_name, address, city, state, zip,
                 classification, pay_method, salary, commission, hourly,
                 routing_num, account_num, office_phone=None, personal_phone=None,
                 office_email=None, personal_email=None, dob=None, ssn=None,
                 admin=None, title=None, dept=None, start=None, end=None,
                 status=None, password=None):

        self.__emp_id = ID
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__classification = classification #1=salary, 2=commissioned, 3=hourly
        self.__pay_method = pay_method #1=deposit, 2=mail
        self.__salary = float(salary)
        self.__commission = float(commission)
        self.__hourly = float(hourly)
        self.__routing_num = routing_num
        self.__account_num = account_num
        self.__office_phone = office_phone
        self.__personal_phone = personal_phone
        self.__office_email = office_email
        self.__personal_email = personal_email
        self.__dob = dob
        self.__ssn = ssn
        self.__admin = admin #Boolean; True if admin, else False
        self.__title = title
        self.__dept = dept
        self.__start = start #Start date
        self.__end = end #End date if deactivated
        self.__status = status #Boolean; True if active, else False
        self.__password = password #For logging into system

        #Establish classification object
        if self.__classification == '1':
            self.make_salaried(self.__salary)
        elif self.__classification == '2':
            self.make_commissioned(self.__salary, self.__commission)
        elif self.__classification == '3':
            self.make_hourly(self.__hourly)



    #Getters
    """Returns employee's ID number"""
    def get_id(self):
        return self.__emp_id

    """Returns employee's first name"""
    def get_first_name(self):
        return self.__first_name
    
    """Returns employee's last name"""
    def get_last_name(self):
        return self.__last_name
            
    """Returns employee's address"""
    def get_address(self):
        return self.__address

    """Returns employee's city"""
    def get_city(self):
        return self.__city

    """Returns employee's state"""
    def get_state(self):
        return self.__state

    """Returns employee's zip code"""
    def get_zip(self):
        return self.__zip
    
    """Returns numerical representation of employee's classification object"""
    def get_class(self):
        if str(self.__classification) == "Salaried Employee":
            return "1"
        elif str(self.__classification) == "Commissioned Employee":
            return "2"
        else:
            return "3"

    """Returns employee's classification object"""
    def get_classification(self):
        return self.__classification
    
    """Returns the employee's salary"""
    def get_salary(self):
        return self.__salary

    """Return the employee's commission rate"""
    def get_commission_rate(self):
        return self.__commission

    """Returns the employee's hourly payment rate"""
    def get_hourly_rate(self):
        return self.__hourly

    """Returns the employee's office phone#"""
    def get_office_phone(self):
        return self.__office_phone

    """Returns the employee's personal phone#"""
    def get_personal_phone(self):
        return self.__personal_phone

    """Returns the employee's office email"""
    def get_office_email(self):
        return self.__office_email

    """Returns the employee's personal email"""
    def get_personal_email(self):
        return self.__personal_email

    """Returns the employee's date of birth"""
    def get_dob(self):
        return self.__dob

    """Returns the employee's SS#"""
    def get_ssn(self):
        return self.__ssn

    """Returns the employee's payment type"""
    def get_pay_method(self): #1=direct deposit, 2=mail
        return self.__pay_method

    """Returns the employee's routing number"""
    def get_routing(self): 
        return self.__routing_num

    """Returns the employee's account number"""
    def get_account(self): 
        return self.__account_num

    """Returns True if employee has admin level permission, else false"""
    def is_admin(self):
        return self.__admin

    """Returns the employee's title"""
    def get_title(self):
        return self.__title

    """Returns the employee's dept"""
    def get_dept(self):
        return self.__dept

    """Returns the employee's start date"""
    def get_start(self):
        return self.__start

    """Returns the employee's end date"""
    def get_end(self):
        return self.__end

    """Returns True if employee still active, else false"""
    def get_status(self):
        return self.__status

    """Returns the employee's login password"""
    def get_password(self):
        return self.__password



    #Setters
    """Sets employee's ID number"""
    def set_id(self, id_num):
        self.__emp_id = id_num

    """Sets employee's first name"""
    def set_first_name(self, name):
        self.__first_name = name
    
    """Sets employee's last name"""
    def set_last_name(self, name):
        self.__last_name = name
            
    """Sets employee's address"""
    def set_address(self, address):
        self.__address = address

    """Sets employee's city"""
    def set_city(self, city):
        self.__city = city

    """Sets employee's state"""
    def set_state(self, state):
        self.__state = state

    """Sets employee's zip code"""
    def set_zip(self, zipcode):
        self.__zip = zipcode

    """Sets the employee's office phone#"""
    def set_office_phone(self, num):
        self.__office_phone = num

    """Sets the employee's personal phone#"""
    def set_personal_phone(self, num):
        self.__personal_phone = num

    """Sets the employee's office email"""
    def set_office_email(self, email):
        self.__office_email = email

    """Sets the employee's personal email"""
    def set_personal_email(self, email):
        self.__personal_email = email

    """Sets the employee's date of birth"""
    def set_dob(self, date):
        self.__dob = date

    """Sets the employee's SS#"""
    def set_ssn(self, num):
        self.__ssn = num

    """Sets the employee's payment type"""
    def set_pay_method(self, value): #1=direct deposit, 2=mail
        self.__pay_method = value

    """Sets the employee's routing number"""
    def set_routing(self, num):
        self.__routing_num = num

    """Sets the employee's account number"""
    def set_account(self, num):
        self.__account_num = num

    """Sets employee's permission level"""
    def make_admin(self, boolean): #Boolean, True to make admin, else False
        self.__admin = boolean

    """Sets the employee's title"""
    def set_title(self, title):
        self.__title = title

    """Sets the employee's dept"""
    def set_dept(self, dept):
        self.__dept = dept

    """Sets the employee's start date and updates their status"""
    def set_start(self, date):
        self.__start = date
        self.__status = True

    """Sets the employee's end date and updates their status"""
    def set_end(self, date):
        self.__end = date
        self.__status = False

    """Sets the employee's employment status directly"""
    def set_status(self, boolean): #Boolean, True for active, else False
        self.__status = boolean

    """Sets the employee's login password"""
    def set_password(self, password):
        self.__password = password

    """Sets the employee's salary"""
    def set_salary(self, salary):
        self.__salary = salary

    """Sets the employee's commission rate"""
    def set_commission_rate(self, rate):
        self.__commission = rate

    """Sets the employee's hourly rate"""
    def set_hourly_rate(self, rate):
        self.__hourly = rate



    
    """Makes the employee a salaried employee"""
    def make_salaried(self, salary):
        self.__salary = salary
        self.__classification = Salaried(self.__salary)

    """Makes the employee an hourly employee"""
    def make_hourly(self, rate):
        self.__hourly = rate
        self.__classification = Hourly(self.__hourly)

    """Makes the employee a commissioned employee"""
    def make_commissioned(self, salary, rate):
        self.__commission = rate
        self.__salary = salary
        self.__classification = Commissioned(self.__salary, self.__commission)

    """Pays the employee""" #writes output to text file
    def issue_payment(self):
        with open(PAY_LOGFILE, 'a') as fout:
            if self.get_classification().compute_pay() == '0.00':
                fout.write("")
            else:
                name = self.get_first_name() + " " + self.get_last_name()
                fout.write(f"Mailing ${self.get_classification().compute_pay()} to {name} at {self.get_address()} {self.get_city()} {self.get_state()} {self.get_zip()}\n")

    """String representation of employee object"""
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.classification}"
    
    # Create or Update emp in DB
    def create_emp_in_db(self):
        data = create_employee(self)
        if (data["status"] == 0):
            self.set_id(str(data["data"]["id"]))
            return True # Create was successful
        else:
            return False # Error in creating
        
    def update_emp_in_db(self):
        data = update_employee(self)
        if (data["status"] == 0):
            return True # Update was successful
        else:
            return False # Error in updating

    def print_all_members(self):
        for data_member in self.__dict__.items():
            print(data_member)





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

    # Getter for timecards
    def get_timecards(self):
        return self.timecards

    # Clear timecards list
    def clear_timecards(self):
        self.timecards.clear()

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
    def get_rate(self):
        return self.commission_rate

    """Adds receipts to the list of receipts"""
    def add_receipt(self, amount):
        try:
            self.receipts.append(float(amount))
        except:
            print("Invalid amount.")
            return None

        # Getter for receipts
    def get_receipts(self):
        return self.receipts

    # Clear receipts list
    def clear_receipts(self):
        self.receipts.clear()

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
    emps = get_db("database/employees.json")
    employees.clear()

    for emp in emps:
        employees.append(Employee(str(emp["id"]), emp["first_name"], emp["last_name"], emp["address"], emp["city"],
                                       emp["state"] ,emp["zip"], emp["classification"], emp["pay_method"], emp["salary"],
                                       emp["commission"], emp["hourly"], emp["routing_num"], emp["account_num"], 
                                       emp["office_phone"], emp["personal_phone"], emp["office_email"], emp["personal_email"],
                                       emp["dob"], emp["ssn"], emp["admin"], emp["title"], emp["dept"], emp["start"],
                                       emp["end"], emp["status"], emp["password"]))

    return employees

"""Adds receipts to every commissioned employee"""
def process_receipts():
    with open(SALES_FILE) as fin:
        for line in fin:
            l = line.split(',')
            emp_idx = find_employee_by_id(str(l[0]))

            # Make sure the currently loaded receipts are clear
            employees[emp_idx].get_classification().clear_receipts()

            for receipt in l[1:]:
                employees[emp_idx].get_classification().add_receipt(receipt)

"""Adds timecards to every hourly employee"""
def process_timecards():
    with open(TIMECARD_FILE) as fin:
        for line in fin:
            l = line.split(',')
            emp_idx = find_employee_by_id(str(l[0]))

            # Make sure the currently loaded timecards are clear
            employees[emp_idx].get_classification().clear_timecards()

            for timecard in l[1:]:
                employees[emp_idx].get_classification().add_timecard(timecard)


"""Finds an employee by their ID number"""
def find_employee_by_id(ID):#ID parameter represents a string!
    # emps = load_employees()

    for idx, emp in enumerate(employees):
        if str(employees[idx].get_id()) == ID:
            return idx

"""Pays each employee"""
def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()

        # Clear the receipts and timecards so no duplicates occur
        if (emp.get_class() == "2"): # Commission
            emp.get_classification().clear_receipts()
        elif (emp.get_class() == "3"): # Hourly
            emp.get_classification().clear_timecards()



