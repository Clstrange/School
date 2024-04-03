'''
Version 2.0

March 15th
Tyler Deschamps
'''

import csv

# from database_module import *

baseKeys = [
    'id', 'first_name', 'last_name', 'street_address', 'city',
    'state', 'zip', 'office_phone', 'pay_type', 'date_of_birth',
    'social_security_number', 'start_date', 'bank_routing_num',
    'bank_account_num', 'permission_id', 'title', 'department',
    'office_email', 'personal_email'
]


def read_from_csv(csvPath):
    empsFromCsv = []
    readerList = []

    with open(csvPath, mode="r") as emps:
        reader = csv.reader(emps)

        for row in reader:
            readerList.append(row)

        csvKeys = readerList[0]
        for row in range(1, len(readerList)):
            tempDict = dict(zip(csvKeys, readerList[row]))
            empsFromCsv.append(tempDict)

    return empsFromCsv


def emps_to_csv(csv_file_path, emps):
    label_row = []

    for key in emps[0]:
        label_row.append(key)

    # Open file and write a column labels row, then insert each employee each row after 
    file = open(csv_file_path, "w+", newline='')

    write = csv.writer(file)
    write.writerow(label_row)

    for emp in emps:
        row = []

        for key, value in emp.items():
            row.append(str(value))

        write.writerows([row])

    file.close()


def timecards_to_csv(csv_file_path, timecards):
    timecard_rows = []

    # Format employee times
    for tc in timecards:
        matched_row = False

        if (len(timecard_rows) >= 1):

            for row in timecard_rows:
                if (row['id'] == tc['emp_id']):
                    row['vals'].append(tc['time'])
                    matched_row = True

                    break

        if (not matched_row):
            timecard_rows.append({
                'id': tc['emp_id'],
                'vals': [tc['time']]
            })

    # Open file and for each employees times, write as a row in csv
    file = open(csv_file_path, "w+", newline='')
    write = csv.writer(file)

    for row in timecard_rows:
        new_row = [str(row['id'])]

        for val in row['vals']:
            new_row.append(str(val))

        write.writerows([new_row])

    file.close()


def receipts_to_csv(csv_file_path, receipts):
    receipt_rows = []
    
    # Format employee receipts
    for rc in receipts:
        matched_row = False

        if (len(receipt_rows) >= 1):

            for row in receipt_rows:
                if (row['id'] == rc['emp_id']):
                    row['vals'].append(rc['amount'])
                    matched_row = True

                    break

        if (not matched_row):
            receipt_rows.append({
                'id': rc['emp_id'],
                'vals': [rc['amount']]
            })

    # Open file and for each of the employee's list of receipts, write as a row in csv
    file = open(csv_file_path, "w+", newline='')
    write = csv.writer(file)

    for row in receipt_rows:
        new_row = [str(row['id'])]

        for val in row['vals']:
            new_row.append(str(val))

        write.writerows([new_row])

    file.close()


