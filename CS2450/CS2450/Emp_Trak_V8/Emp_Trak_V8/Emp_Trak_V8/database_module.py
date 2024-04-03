'''
Version 2.0

March 15th
Tyler Deschamps
'''

import json

from csv_file_module import *
from datetime import datetime

EMP_DB_PATH = "database/employees.json"
RECEIPTS_DB_PATH = "database/receipts.json"
TIMECARDS_DB_PATH = "database/timecards.json"

# =============================================================================
# Store Data in JSON file
# =============================================================================
def store_db(database_path, data):
    json_obj = json.dumps(data, indent=4)

    file = open(database_path, "w")
    file.write(json_obj)

    file.close()

# =============================================================================
# Get Data stored in JSON file
# =============================================================================
def get_db(database_path):
    table = []
    table_list = []

    file = open(database_path, "r")
    table = file.read()
    table_list = json.loads(table)

    file.close()

    return table_list

# =============================================================================
# Search Database for specific argument
# =============================================================================
def search_employees(search_filter, search_data):
    emps = get_db()
    column = search_filter.get()
    search_data = search_data.get()

    for emp in emps:
        # Integer comparisons
        if (column == "id"):
            if (int(search_data) == emp[column]):
                print()

        # String comparisons
        else:
            if (search_data == emp[column]):
                print()

# =============================================================================
# Creates a new empoloyee object and saves it in database
# =============================================================================
def create_employee(emp_obj):
    emps = get_db(EMP_DB_PATH)

    try:
        new_emps = emps

        # Create new employee dictionary to be converted to JSON
        new_employee = {
            "id": emp_obj.get_id(),
            "first_name": emp_obj.get_first_name(),
            "last_name": emp_obj.get_last_name(),
            "address": emp_obj.get_address(),
            "city": emp_obj.get_city(),
            "state": emp_obj.get_state(),
            "zip": emp_obj.get_zip(),
            "classification": emp_obj.get_class(),
            "pay_method": emp_obj.get_pay_method(),
            "salary": emp_obj.get_salary(),
            "commission": emp_obj.get_commission_rate(),
            "hourly": emp_obj.get_hourly_rate(),
            "routing_num": emp_obj.get_routing(),
            "account_num": emp_obj.get_account(),
            "office_phone": emp_obj.get_office_phone(),
            "personal_phone": emp_obj.get_personal_phone(),
            "office_email": emp_obj.get_office_email(),
            "personal_email": emp_obj.get_personal_email(),
            "dob": emp_obj.get_dob(),
            "ssn": emp_obj.get_ssn(),
            "admin": emp_obj.is_admin(),
            "title": emp_obj.get_title(),
            "dept": emp_obj.get_dept(),
            "start": emp_obj.get_start(),
            "end": emp_obj.get_end(),
            "status": emp_obj.get_status(),
            "password": emp_obj.get_password()
        }

        new_emps.append(new_employee)

        # Prepare jsonObj and write to json file
        json_obj = json.dumps(new_emps, indent=4)

        file = open(EMP_DB_PATH, "w")
        file.write(json_obj)
        file.close()

        return {
            "status": 0,
            "data": new_employee
        }
    except:
        # Roll back the DB
        print("Error in creating employee in database, reverting to last successful save.")

        backup = json.dumps(emps, indent=4)

        file = open(EMP_DB_PATH, "w")
        file.write(backup)
        file.close()

        return {
            "status": 1,
            "data": []
        }


# =============================================================================
# Updates an empoloyee object and saves it in database
# =============================================================================
def update_employee(emp_obj):
    emps = get_db(EMP_DB_PATH)

    try:
        updated_emps = emps

        # Create update employee dictionary to be converted to JSON
        updated_employee = {
            "id": emp_obj.get_id(),
            "first_name": emp_obj.get_first_name(),
            "last_name": emp_obj.get_last_name(),
            "address": emp_obj.get_address(),
            "city": emp_obj.get_city(),
            "state": emp_obj.get_state(),
            "zip": emp_obj.get_zip(),
            "classification": emp_obj.get_class(),
            "pay_method": emp_obj.get_pay_method(),
            "salary": emp_obj.get_salary(),
            "commission": emp_obj.get_commission_rate(),
            "hourly": emp_obj.get_hourly_rate(),
            "routing_num": emp_obj.get_routing(),
            "account_num": emp_obj.get_account(),
            "office_phone": emp_obj.get_office_phone(),
            "personal_phone": emp_obj.get_personal_phone(),
            "office_email": emp_obj.get_office_email(),
            "personal_email": emp_obj.get_personal_email(),
            "dob": emp_obj.get_dob(),
            "ssn": emp_obj.get_ssn(),
            "admin": emp_obj.is_admin(),
            "title": emp_obj.get_title(),
            "dept": emp_obj.get_dept(),
            "start": emp_obj.get_start(),
            "end": emp_obj.get_end(),
            "status": emp_obj.get_status(),
            "password": emp_obj.get_password()
        }

        for idx, emp in enumerate(updated_emps):
            if (str(emp["id"]) == str(updated_employee["id"])):
                updated_emps[idx] = updated_employee

        # Prepare jsonObj and write to json file
        json_obj = json.dumps(updated_emps, indent=4)

        file = open(EMP_DB_PATH, "w")
        file.write(json_obj)
        file.close()

        return {
            "status": 0,
            "data": updated_employee
        }
    except: 
        # Roll back the DB
        print("Error in updating employee in database, reverting to last successful save.")

        backup = json.dumps(emps, indent=4)

        file = open(EMP_DB_PATH, "w")
        file.write(backup)
        file.close()

        return {
            "status": 1,
            "data": []
        }

# =============================================================================
# Creates an empoloyee's timecard entry and saves it in database
# =============================================================================
def create_employee_timecard(emp_obj, time):
    t_cards = get_db(TIMECARDS_DB_PATH)

    try:
        updated_t_cards = t_cards

        new_t_card = {
            "id": t_cards[-1]['id'] + 1,
            "emp_id": emp_obj.get_id(),
            "time": time
        }

        updated_t_cards.append(new_t_card)

        # Prepare jsonObj and write to json file
        json_obj = json.dumps(updated_t_cards, indent=4)

        file = open(TIMECARDS_DB_PATH, "w")
        file.write(json_obj)
        file.close()

        timecards_to_csv("csv/timecards.csv", get_db(TIMECARDS_DB_PATH))

        return {
            "status": 0,
            "data": new_t_card
        }
    except:
         # Roll back the DB
        print("Error in creating employee timecard in database, reverting to last successful save.")

        backup = json.dumps(t_cards, indent=4)

        file = open(TIMECARDS_DB_PATH, "w")
        file.write(backup)
        file.close()

        return {
            "status": 1,
            "data": []
        }

# =============================================================================
# Updates an empoloyee's timecard entry and saves it in database
# =============================================================================
def create_employee_receipt(emp_obj, amount):
    receipts = get_db(RECEIPTS_DB_PATH)

    try:
        updated_receipts = receipts

        new_receipt = {
            "id": receipts[-1]['id'] + 1,
            "emp_id": emp_obj.get_id(),
            "amount": amount
        }

        updated_receipts.append(new_receipt)

        # Prepare jsonObj and write to json file
        json_obj = json.dumps(updated_receipts, indent=4)

        file = open(RECEIPTS_DB_PATH, "w")
        file.write(json_obj)
        file.close()

        receipts_to_csv("csv/receipts.csv", get_db(RECEIPTS_DB_PATH))

        return {
            "status": 0,
            "data": new_receipt
        }
    except:
        # Roll back the DB
        print("Error in adding receipt to database, reverting to last successful save.")

        backup = json.dumps(receipts, indent=4)

        file = open(RECEIPTS_DB_PATH, "w")
        file.write(backup)
        file.close()

        return {
            "status": 1,
            "data": []
        }


