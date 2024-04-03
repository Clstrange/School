import EmpDat_v7.5 #code file to test
from employee_v3 import * #code for employee
import pytest    #testing framework
from tkinter import ttk

#PLEASE NOTE THAT IN THIS VERSION, MANUALLY CHANGING THE state variable in EmpDat_v5 to emp_state in the view_page
#is required to make all tests pass, when that variable is changed in the next update to EmpDat, I will update this
#test code to work with that change. There are 7 of these that need to be changed



# emp_dict = {}
# emp1 = Employee("1", "Jaden", "Albrecht", "Street", "City", "State", "Zip", "1", "1",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", False, "Master Manager", "Managing Dept", "1/1/22", None, True,
#             "test")
# emp2 = Employee("2", "Cody", "Strange", "Street", "City", "State", "Zip", "2", "2",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", False, "Super Scribe", "Writing Dept", "1/1/22", None, True,
#             "test")
# emp3 = Employee("3", "Tyler", "Deschamp", "Street", "City", "State", "Zip", "3", "1",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", False, "Chart Champion", "Documenting Dept", "1/1/22", None, True,
#             "test")
# emp4 = Employee("4", "Jordan", "Van Patten", "Street", "City", "State", "Zip", "1", "2",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", False, "Triumphant Tester", "Testing Dept", "1/1/22", None, True,
#             "test")
# emp5 = Employee("5", "Ethan", "Taylor", "Street", "City", "State", "Zip", "2", "1",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", True, "GUI Guy", "GUI Dept", "1/1/22", None, True,
#             "test")
# emp6 = Employee("6", "Etha", "Taylor", "Street", "City", "State", "Zip", "2", "1",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", True, "GUI Guy", "GUI Dept", "1/1/22", None, True,
#             "test")
# emp7 = Employee("7", "Eth", "Taylor", "Street", "City", "State", "Zip", "2", "1",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", True, "GUI Guy", "GUI Dept", "1/1/22", None, True,
#             "test")
# emp8 = Employee("8", "Et", "Taylor", "Street", "City", "State", "Zip", "2", "1",
#             100.00, 10.00, 1.00, "Routing Num", "Account Num", "Office Num",
#             "Personal Phone", "Office Email", "Personal Email", "Birthday",
#             "SSN", True, "GUI Guy", "GUI Dept", "1/1/22", None, True,
#             "test")

# emp_dict[emp1.get_id()] = emp1
# emp_dict[emp2.get_id()] = emp2
# emp_dict[emp3.get_id()] = emp3
# emp_dict[emp4.get_id()] = emp4
# emp_dict[emp5.get_id()] = emp5
# emp_dict[emp6.get_id()] = emp6
# emp_dict[emp7.get_id()] = emp7
# emp_dict[emp8.get_id()] = emp8
# x = EmpDat_v5.EmpApp(emp_dict)

emps = get_db("database/employees.json")
emp_dict = {}

for emp in emps:
    emp_dict[str(emp["id"])] = Employee(str(emp["id"]), emp["first_name"], emp["last_name"], emp["address"], emp["city"],
                                    emp["state"] ,emp["zip"], emp["classification"], emp["pay_method"], emp["salary"],
                                    emp["commission"], emp["hourly"], emp["routing_num"], emp["account_num"], 
                                    emp["office_phone"], emp["personal_phone"], emp["office_email"], emp["personal_email"],
                                    emp["dob"], emp["ssn"], emp["admin"], emp["title"], emp["dept"], emp["start"],
                                    emp["end"], emp["status"], emp["password"])
        
x = EmpDat_v5.EmpApp(emp_dict)
#CODE FOR TESTING LOGIN (Validate user class only)
def test_correct_1():
    #code that should pass username and password
    x.username.set("8")
    x.user_pass.set("test")
    x.validate_user()
    assert x.msg.get() != ("Invalid ID!") and ("Incorrect password or ID!") != x.msg.get()

def test_correct_2():
    x.username.set("2")
    x.user_pass.set("test")
    x.validate_user()
    assert x.msg.get() != ("Invalid ID!") and ("Incorrect password or ID!") != x.msg.get()

def test_correct_3():
    x.username.set("3")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") != x.msg.get() and ("Incorrect password or ID!") != x.msg.get()

def test_correct_4():
    x.username.set("4")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") != x.msg.get() and ("Incorrect password or ID!") != x.msg.get()

def test_correct_5():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") != x.msg.get() and ("Incorrect password or ID!") != x.msg.get()

def test_correct_6():
    x.username.set("6")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") != x.msg.get() and ("Incorrect password or ID!") != x.msg.get()

def test_correct_7():
    x.username.set("7")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") != x.msg.get() and ("Incorrect password or ID!") != x.msg.get()

#code testing for incorrect usernames but correct passwords
def test_incorrect_1():
    x.username.set("jim")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrect_2():
    x.username.set("tony")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrect_3():
    x.username.set("123")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrect_4():
    x.username.set("57")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()
    

def test_incorrect_5():
    x.username.set("gfad")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrect_6():
    x.username.set("wrong")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrect_7():
    x.username.set("almost")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrect_8():
    x.username.set("so close")
    x.user_pass.set("test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

#code that tests for incorrect passwords, but correct username

def test_incorrectP_1():
    x.username.set("1")
    x.user_pass.set("tests")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_2():
    x.username.set("1")
    x.user_pass.set("test!")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_3():
    x.username.set("1")
    x.user_pass.set("tesT")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_4():
    x.username.set("1")
    x.user_pass.set("Test")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_5():
    x.username.set("1")
    x.user_pass.set("nope")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_6():
    x.username.set("1")
    x.user_pass.set("tESt")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_7():
    x.username.set("1")
    x.user_pass.set("password")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_8():
    x.username.set("1")
    x.user_pass.set("letMeIn")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_9():
    x.username.set("1")
    x.user_pass.set("please")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_10():
    x.username.set("1")
    x.user_pass.set("prettyplease")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()

def test_incorrectP_11():
    x.username.set("1")
    x.user_pass.set("123456")
    x.validate_user()
    assert ("Invalid ID!") == x.msg.get() or ("Incorrect password or ID!") == x.msg.get()




#CODE FOR TESTING VIEW PAGE
def test_nonAdminPass_1():
    x.username.set("8")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert v.id.get() == emp_dict[x.username.get()].get_id()
    assert v.f_name.get() == emp_dict[x.username.get()].get_first_name()
    assert v.l_name.get() == emp_dict[x.username.get()].get_last_name()
    assert v.street.get() == emp_dict[x.username.get()].get_address()
    assert v.city.get() == emp_dict[x.username.get()].get_city()
    assert v.emp_state.get() == emp_dict[x.username.get()].get_state()
    assert v.zip.get() == emp_dict[x.username.get()].get_zip()
    assert v.classification.get() == emp_dict[x.username.get()].get_class()
    assert v.hourly.get() == str(emp_dict[x.username.get()].get_hourly_rate())
    assert v.commissioned.get() == str(emp_dict[x.username.get()].get_commission_rate())
    assert v.salary.get() == str(emp_dict[x.username.get()].get_salary())
    assert v.o_phone.get() == emp_dict[x.username.get()].get_office_phone()
    assert v.o_email.get() == emp_dict[x.username.get()].get_office_email()
    assert v.p_phone.get() == emp_dict[x.username.get()].get_personal_phone()
    assert v.p_email.get() == emp_dict[x.username.get()].get_personal_email()
    assert v.dob.get() == emp_dict[x.username.get()].get_dob()
    assert v.ssn.get() == emp_dict[x.username.get()].get_ssn()
    assert v.pay_type.get() == emp_dict[x.username.get()].get_pay_method()
    assert v.routing_num.get() == emp_dict[x.username.get()].get_routing()
    assert v.account_entry.get() == emp_dict[x.username.get()].get_account()
    assert v.emp_title.get() == emp_dict[x.username.get()].get_title()
    assert v.emp_dept.get() == emp_dict[x.username.get()].get_dept()
    assert v.start_date.get() == emp_dict[x.username.get()].get_start()
    assert v.end_date.get() == str(emp_dict[x.username.get()].get_end())
    if (emp_dict[x.username.get()].get_status() == True):
        assert v.emp_status.get() == "Active"
    else:
        assert v.emp_status.get() == "Deactivated"

def test_nonAdminPass_2():
    x.username.set("2")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert v.id.get() == emp_dict[x.username.get()].get_id()
    assert v.f_name.get() == emp_dict[x.username.get()].get_first_name()
    assert v.l_name.get() == emp_dict[x.username.get()].get_last_name()
    assert v.street.get() == emp_dict[x.username.get()].get_address()
    assert v.city.get() == emp_dict[x.username.get()].get_city()
    assert v.emp_state.get() == emp_dict[x.username.get()].get_state()
    assert v.zip.get() == emp_dict[x.username.get()].get_zip()
    assert v.classification.get() == emp_dict[x.username.get()].get_class()
    assert v.hourly.get() == str(emp_dict[x.username.get()].get_hourly_rate())
    assert v.commissioned.get() == str(emp_dict[x.username.get()].get_commission_rate())
    assert v.salary.get() == str(emp_dict[x.username.get()].get_salary())
    assert v.o_phone.get() == emp_dict[x.username.get()].get_office_phone()
    assert v.o_email.get() == emp_dict[x.username.get()].get_office_email()
    assert v.p_phone.get() == emp_dict[x.username.get()].get_personal_phone()
    assert v.p_email.get() == emp_dict[x.username.get()].get_personal_email()
    assert v.dob.get() == emp_dict[x.username.get()].get_dob()
    assert v.ssn.get() == emp_dict[x.username.get()].get_ssn()
    assert v.pay_type.get() == emp_dict[x.username.get()].get_pay_method()
    assert v.routing_num.get() == emp_dict[x.username.get()].get_routing()
    assert v.account_entry.get() == emp_dict[x.username.get()].get_account()
    assert v.emp_title.get() == emp_dict[x.username.get()].get_title()
    assert v.emp_dept.get() == emp_dict[x.username.get()].get_dept()
    assert v.start_date.get() == emp_dict[x.username.get()].get_start()
    assert v.end_date.get() == str(emp_dict[x.username.get()].get_end())
    if (emp_dict[x.username.get()].get_status() == True):
        assert v.emp_status.get() == "Active"
    else:
        assert v.emp_status.get() == "Deactivated"
def test_nonAdminPass_3():
    x.username.set("3")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert v.id.get() == emp_dict[x.username.get()].get_id()
    assert v.f_name.get() == emp_dict[x.username.get()].get_first_name()
    assert v.l_name.get() == emp_dict[x.username.get()].get_last_name()
    assert v.street.get() == emp_dict[x.username.get()].get_address()
    assert v.city.get() == emp_dict[x.username.get()].get_city()
    assert v.emp_state.get() == emp_dict[x.username.get()].get_state()
    assert v.zip.get() == emp_dict[x.username.get()].get_zip()
    assert v.classification.get() == emp_dict[x.username.get()].get_class()
    assert v.hourly.get() == str(emp_dict[x.username.get()].get_hourly_rate())
    assert v.commissioned.get() == str(emp_dict[x.username.get()].get_commission_rate())
    assert v.salary.get() == str(emp_dict[x.username.get()].get_salary())
    assert v.o_phone.get() == emp_dict[x.username.get()].get_office_phone()
    assert v.o_email.get() == emp_dict[x.username.get()].get_office_email()
    assert v.p_phone.get() == emp_dict[x.username.get()].get_personal_phone()
    assert v.p_email.get() == emp_dict[x.username.get()].get_personal_email()
    assert v.dob.get() == emp_dict[x.username.get()].get_dob()
    assert v.ssn.get() == emp_dict[x.username.get()].get_ssn()
    assert v.pay_type.get() == emp_dict[x.username.get()].get_pay_method()
    assert v.routing_num.get() == emp_dict[x.username.get()].get_routing()
    assert v.account_entry.get() == emp_dict[x.username.get()].get_account()
    assert v.emp_title.get() == emp_dict[x.username.get()].get_title()
    assert v.emp_dept.get() == emp_dict[x.username.get()].get_dept()
    assert v.start_date.get() == emp_dict[x.username.get()].get_start()
    assert v.end_date.get() == str(emp_dict[x.username.get()].get_end())
    if (emp_dict[x.username.get()].get_status() == True):
        assert v.emp_status.get() == "Active"
    else:
        assert v.emp_status.get() == "Deactivated"

def test_nonAdminPass_4():
    x.username.set("4")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert v.id.get() == emp_dict[x.username.get()].get_id()
    assert v.f_name.get() == emp_dict[x.username.get()].get_first_name()
    assert v.l_name.get() == emp_dict[x.username.get()].get_last_name()
    assert v.street.get() == emp_dict[x.username.get()].get_address()
    assert v.city.get() == emp_dict[x.username.get()].get_city()
    assert v.emp_state.get() == emp_dict[x.username.get()].get_state()
    assert v.zip.get() == emp_dict[x.username.get()].get_zip()
    assert v.classification.get() == emp_dict[x.username.get()].get_class()
    assert v.hourly.get() == str(emp_dict[x.username.get()].get_hourly_rate())
    assert v.commissioned.get() == str(emp_dict[x.username.get()].get_commission_rate())
    assert v.salary.get() == str(emp_dict[x.username.get()].get_salary())
    assert v.o_phone.get() == emp_dict[x.username.get()].get_office_phone()
    assert v.o_email.get() == emp_dict[x.username.get()].get_office_email()
    assert v.p_phone.get() == emp_dict[x.username.get()].get_personal_phone()
    assert v.p_email.get() == emp_dict[x.username.get()].get_personal_email()
    assert v.dob.get() == emp_dict[x.username.get()].get_dob()
    assert v.ssn.get() == emp_dict[x.username.get()].get_ssn()
    assert v.pay_type.get() == emp_dict[x.username.get()].get_pay_method()
    assert v.routing_num.get() == emp_dict[x.username.get()].get_routing()
    assert v.account_entry.get() == emp_dict[x.username.get()].get_account()
    assert v.emp_title.get() == emp_dict[x.username.get()].get_title()
    assert v.emp_dept.get() == emp_dict[x.username.get()].get_dept()
    assert v.start_date.get() == emp_dict[x.username.get()].get_start()
    assert v.end_date.get() == str(emp_dict[x.username.get()].get_end())
    if (emp_dict[x.username.get()].get_status() == True):
        assert v.emp_status.get() == "Active"
    else:
        assert v.emp_status.get() == "Deactivated"

def test_AdminPass_1():
    x.username.set("8")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert v.id.get() == emp_dict[x.username.get()].get_id()
    assert v.f_name.get() == emp_dict[x.username.get()].get_first_name()
    assert v.l_name.get() == emp_dict[x.username.get()].get_last_name()
    assert v.street.get() == emp_dict[x.username.get()].get_address()
    assert v.city.get() == emp_dict[x.username.get()].get_city()
    assert v.emp_state.get() == emp_dict[x.username.get()].get_state()
    assert v.zip.get() == emp_dict[x.username.get()].get_zip()
    assert v.classification.get() == emp_dict[x.username.get()].get_class()
    assert v.hourly.get() == str(emp_dict[x.username.get()].get_hourly_rate())
    assert v.commissioned.get() == str(emp_dict[x.username.get()].get_commission_rate())
    assert v.salary.get() == str(emp_dict[x.username.get()].get_salary())
    assert v.o_phone.get() == emp_dict[x.username.get()].get_office_phone()
    assert v.o_email.get() == emp_dict[x.username.get()].get_office_email()
    assert v.p_phone.get() == emp_dict[x.username.get()].get_personal_phone()
    assert v.p_email.get() == emp_dict[x.username.get()].get_personal_email()
    assert v.dob.get() == emp_dict[x.username.get()].get_dob()
    assert v.ssn.get() == emp_dict[x.username.get()].get_ssn()
    assert v.pay_type.get() == emp_dict[x.username.get()].get_pay_method()
    assert v.routing_num.get() == emp_dict[x.username.get()].get_routing()
    assert v.account_entry.get() == emp_dict[x.username.get()].get_account()
    assert v.emp_title.get() == emp_dict[x.username.get()].get_title()
    assert v.emp_dept.get() == emp_dict[x.username.get()].get_dept()
    assert v.start_date.get() == emp_dict[x.username.get()].get_start()
    assert v.end_date.get() == str(emp_dict[x.username.get()].get_end())
    if (emp_dict[x.username.get()].get_status() == True):
        assert v.emp_status.get() == "Active"
    else:
        assert v.emp_status.get() == "Deactivated"

def test_AdminPass_2():
    x.username.set("6")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert v.id.get() == emp_dict[x.username.get()].get_id()
    assert v.f_name.get() == emp_dict[x.username.get()].get_first_name()
    assert v.l_name.get() == emp_dict[x.username.get()].get_last_name()
    assert v.street.get() == emp_dict[x.username.get()].get_address()
    assert v.city.get() == emp_dict[x.username.get()].get_city()
    assert v.emp_state.get() == emp_dict[x.username.get()].get_state()
    assert v.zip.get() == emp_dict[x.username.get()].get_zip()
    assert v.classification.get() == emp_dict[x.username.get()].get_class()
    assert v.hourly.get() == str(emp_dict[x.username.get()].get_hourly_rate())
    assert v.commissioned.get() == str(emp_dict[x.username.get()].get_commission_rate())
    assert v.salary.get() == str(emp_dict[x.username.get()].get_salary())
    assert v.o_phone.get() == emp_dict[x.username.get()].get_office_phone()
    assert v.o_email.get() == emp_dict[x.username.get()].get_office_email()
    assert v.p_phone.get() == emp_dict[x.username.get()].get_personal_phone()
    assert v.p_email.get() == emp_dict[x.username.get()].get_personal_email()
    assert v.dob.get() == emp_dict[x.username.get()].get_dob()
    assert v.ssn.get() == emp_dict[x.username.get()].get_ssn()
    assert v.pay_type.get() == emp_dict[x.username.get()].get_pay_method()
    assert v.routing_num.get() == emp_dict[x.username.get()].get_routing()
    assert v.account_entry.get() == emp_dict[x.username.get()].get_account()
    assert v.emp_title.get() == emp_dict[x.username.get()].get_title()
    assert v.emp_dept.get() == emp_dict[x.username.get()].get_dept()
    assert v.start_date.get() == emp_dict[x.username.get()].get_start()
    assert v.end_date.get() == str(emp_dict[x.username.get()].get_end())
    if (emp_dict[x.username.get()].get_status() == True):
        assert v.emp_status.get() == "Active"
    else:
        assert v.emp_status.get() == "Deactivated"

#CODE FOR TESTING EDIT PAGE
def test_edit_1():
    x.username.set("8")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    e = EmpDat_v5.Edit_Page(v, controller=x)
    e.f_name.set("FirstNameChanged")
    e.l_name.set("LastNameChanged")
    e.street.set("StreetChanged")
    e.city.set("CityChanged")
    e.zip.set("ZIPChanged")
    e.classification.set("2")
    e.pay_type.set("1")
    e.salary.set("100.00")
    e.commissioned.set("10.00")
    e.hourly.set("1.00")
    e.routing_num.set("RoutingChanged")
    e.account_num.set("AccountChanged")
    e.o_phone.set("OfficePChanged")
    e.p_phone.set("PersonalPChanged")
    e.o_email.set("OfficeEChanged")
    e.p_email.set("PersonalEChanged")
    e.dob.set("BirthdayChanged")
    e.ssn.set("SSNChanged")
    e.emp_title.set("MasterChanged")
    e.emp_dept.set("DeptChanged")
    e.start_date.set("1/2/2022")
    e.update_emp()
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[x.username.get()].get_first_name() == "FirstNameChanged"
    assert emp_dict[x.username.get()].get_last_name() == "LastNameChanged"
    assert emp_dict[x.username.get()].get_address() == "StreetChanged"
    assert emp_dict[x.username.get()].get_city() == "CityChanged"
    assert emp_dict[x.username.get()].get_zip() == "ZIPChanged"
    assert emp_dict[x.username.get()].get_class() == "2"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) == "1.00"
    assert str(emp_dict[x.username.get()].get_commission_rate()) == "10.00"
    assert str(emp_dict[x.username.get()].get_salary()) == "100.00"
    assert emp_dict[x.username.get()].get_office_phone() == "OfficePChanged"
    assert emp_dict[x.username.get()].get_office_email() == "OfficeEChanged"
    assert emp_dict[x.username.get()].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[x.username.get()].get_personal_email() == "PersonalEChanged"
    assert emp_dict[x.username.get()].get_dob() == "BirthdayChanged"
    assert emp_dict[x.username.get()].get_ssn() == "SSNChanged"
    assert emp_dict[x.username.get()].get_pay_method() == "1"
    assert emp_dict[x.username.get()].get_routing() == "RoutingChanged"
    assert emp_dict[x.username.get()].get_account() == "AccountChanged"
    assert emp_dict[x.username.get()].get_title() == "MasterChanged"
    assert emp_dict[x.username.get()].get_dept() == "DeptChanged"
    assert emp_dict[x.username.get()].get_start() == "1/2/2022"
    if (emp_dict[x.username.get()].get_status() == True):
        assert e.emp_status.get() == "Active"
    else:
        assert e.emp_status.get() == "Deactivated"

def test_edit_2():
    x.username.set("8")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    e = EmpDat_v5.Edit_Page(v, controller=x)
    e.f_name.set("FirstNameChanged")
    e.l_name.set("LastNameChanged")
    e.street.set("StreetChanged")
    e.city.set("CityChanged")
    e.zip.set("ZIPChanged")
    e.classification.set("2")
    e.pay_type.set("1")
    e.salary.set("100.00")
    e.commissioned.set("10.00")
    e.hourly.set("1.00")
    e.routing_num.set("RoutingChanged")
    e.account_num.set("AccountChanged")
    e.o_phone.set("OfficePChanged")
    e.p_phone.set("PersonalPChanged")
    e.o_email.set("OfficeEChanged")
    e.p_email.set("PersonalEChanged")
    e.dob.set("BirthdayChanged")
    e.ssn.set("SSNChanged")
    e.emp_title.set("MasterChanged")
    e.emp_dept.set("DeptChanged")
    e.start_date.set("1/2/2022")
    e.update_emp()
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[x.username.get()].get_first_name() == "FirstNameChanged"
    assert emp_dict[x.username.get()].get_last_name() == "LastNameChanged"
    assert emp_dict[x.username.get()].get_address() == "StreetChanged"
    assert emp_dict[x.username.get()].get_city() == "CityChanged"
    assert emp_dict[x.username.get()].get_zip() == "ZIPChanged"
    assert emp_dict[x.username.get()].get_class() == "2"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) == "1.00"
    assert str(emp_dict[x.username.get()].get_commission_rate()) == "10.00"
    assert str(emp_dict[x.username.get()].get_salary()) == "100.00"
    assert emp_dict[x.username.get()].get_office_phone() == "OfficePChanged"
    assert emp_dict[x.username.get()].get_office_email() == "OfficeEChanged"
    assert emp_dict[x.username.get()].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[x.username.get()].get_personal_email() == "PersonalEChanged"
    assert emp_dict[x.username.get()].get_dob() == "BirthdayChanged"
    assert emp_dict[x.username.get()].get_ssn() == "SSNChanged"
    assert emp_dict[x.username.get()].get_pay_method() == "1"
    assert emp_dict[x.username.get()].get_routing() == "RoutingChanged"
    assert emp_dict[x.username.get()].get_account() == "AccountChanged"
    assert emp_dict[x.username.get()].get_title() == "MasterChanged"
    assert emp_dict[x.username.get()].get_dept() == "DeptChanged"
    assert emp_dict[x.username.get()].get_start() == "1/2/2022"
    if (emp_dict[x.username.get()].get_status() == True):
        assert e.emp_status.get() == "Active"
    else:
        assert e.emp_status.get() == "Deactivated"

def test_edit_3():
    x.username.set("2")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    e = EmpDat_v5.Edit_Page(v, controller=x)
    e.f_name.set("FirstNameChanged")
    e.l_name.set("LastNameChanged")
    e.street.set("StreetChanged")
    e.city.set("CityChanged")
    e.zip.set("ZIPChanged")
    e.classification.set("1")
    e.pay_type.set("1")
    e.salary.set("100.00")
    e.commissioned.set("10.00")
    e.hourly.set("1.00")
    e.routing_num.set("RoutingChanged")
    e.account_num.set("AccountChanged")
    e.o_phone.set("OfficePChanged")
    e.p_phone.set("PersonalPChanged")
    e.o_email.set("OfficeEChanged")
    e.p_email.set("PersonalEChanged")
    e.dob.set("BirthdayChanged")
    e.ssn.set("SSNChanged")
    e.emp_title.set("MasterChanged")
    e.emp_dept.set("DeptChanged")
    e.start_date.set("1/2/2022")
    e.update_emp()
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[x.username.get()].get_first_name() == "FirstNameChanged"
    assert emp_dict[x.username.get()].get_last_name() == "LastNameChanged"
    assert emp_dict[x.username.get()].get_address() == "StreetChanged"
    assert emp_dict[x.username.get()].get_city() == "CityChanged"
    assert emp_dict[x.username.get()].get_zip() == "ZIPChanged"
    assert emp_dict[x.username.get()].get_class() == "1"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) == "1.00"
    assert str(emp_dict[x.username.get()].get_commission_rate()) == "10.00"
    assert str(emp_dict[x.username.get()].get_salary()) == "100.00"
    assert emp_dict[x.username.get()].get_office_phone() == "OfficePChanged"
    assert emp_dict[x.username.get()].get_office_email() == "OfficeEChanged"
    assert emp_dict[x.username.get()].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[x.username.get()].get_personal_email() == "PersonalEChanged"
    assert emp_dict[x.username.get()].get_dob() == "BirthdayChanged"
    assert emp_dict[x.username.get()].get_ssn() == "SSNChanged"
    assert emp_dict[x.username.get()].get_pay_method() == "1"
    assert emp_dict[x.username.get()].get_routing() == "RoutingChanged"
    assert emp_dict[x.username.get()].get_account() == "AccountChanged"
    assert emp_dict[x.username.get()].get_title() == "MasterChanged"
    assert emp_dict[x.username.get()].get_dept() == "DeptChanged"
    assert emp_dict[x.username.get()].get_start() == "1/2/2022"
    if (emp_dict[x.username.get()].get_status() == True):
        assert e.emp_status.get() == "Active"
    else:
        assert e.emp_status.get() == "Deactivated"

def test_edit_4():
    x.username.set("3")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    e = EmpDat_v5.Edit_Page(v, controller=x)
    e.f_name.set("FirstNameChanged")
    e.l_name.set("LastNameChanged")
    e.street.set("StreetChanged")
    e.city.set("CityChanged")
    e.zip.set("ZIPChanged")
    e.classification.set("2")
    e.pay_type.set("1")
    e.salary.set("100.00")
    e.commissioned.set("10.00")
    e.hourly.set("1.00")
    e.routing_num.set("RoutingChanged")
    e.account_num.set("AccountChanged")
    e.o_phone.set("OfficePChanged")
    e.p_phone.set("PersonalPChanged")
    e.o_email.set("OfficeEChanged")
    e.p_email.set("PersonalEChanged")
    e.dob.set("BirthdayChanged")
    e.ssn.set("SSNChanged")
    e.emp_title.set("MasterChanged")
    e.emp_dept.set("DeptChanged")
    e.start_date.set("1/2/2022")
    e.update_emp()
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[x.username.get()].get_first_name() == "FirstNameChanged"
    assert emp_dict[x.username.get()].get_last_name() == "LastNameChanged"
    assert emp_dict[x.username.get()].get_address() == "StreetChanged"
    assert emp_dict[x.username.get()].get_city() == "CityChanged"
    assert emp_dict[x.username.get()].get_zip() == "ZIPChanged"
    assert emp_dict[x.username.get()].get_class() == "2"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) == "1.00"
    assert str(emp_dict[x.username.get()].get_commission_rate()) == "10.00"
    assert str(emp_dict[x.username.get()].get_salary()) == "100.00"
    assert emp_dict[x.username.get()].get_office_phone() == "OfficePChanged"
    assert emp_dict[x.username.get()].get_office_email() == "OfficeEChanged"
    assert emp_dict[x.username.get()].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[x.username.get()].get_personal_email() == "PersonalEChanged"
    assert emp_dict[x.username.get()].get_dob() == "BirthdayChanged"
    assert emp_dict[x.username.get()].get_ssn() == "SSNChanged"
    assert emp_dict[x.username.get()].get_pay_method() == "1"
    assert emp_dict[x.username.get()].get_routing() == "RoutingChanged"
    assert emp_dict[x.username.get()].get_account() == "AccountChanged"
    assert emp_dict[x.username.get()].get_title() == "MasterChanged"
    assert emp_dict[x.username.get()].get_dept() == "DeptChanged"
    assert emp_dict[x.username.get()].get_start() == "1/2/2022"
    if (emp_dict[x.username.get()].get_status() == True):
        assert e.emp_status.get() == "Active"
    else:
        assert e.emp_status.get() == "Deactivated"

def test_edit_5():
    x.username.set("4")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    e = EmpDat_v5.Edit_Page(v, controller=x)
    e.f_name.set("FirstNameChanged")
    e.l_name.set("LastNameChanged")
    e.street.set("StreetChanged")
    e.city.set("CityChanged")
    e.zip.set("ZIPChanged")
    e.classification.set("2")
    e.pay_type.set("1")
    e.salary.set("100.00")
    e.commissioned.set("10.00")
    e.hourly.set("1.00")
    e.routing_num.set("RoutingChanged")
    e.account_num.set("AccountChanged")
    e.o_phone.set("OfficePChanged")
    e.p_phone.set("PersonalPChanged")
    e.o_email.set("OfficeEChanged")
    e.p_email.set("PersonalEChanged")
    e.dob.set("BirthdayChanged")
    e.ssn.set("SSNChanged")
    e.emp_title.set("MasterChanged")
    e.emp_dept.set("DeptChanged")
    e.start_date.set("1/2/2022")
    e.update_emp()
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[x.username.get()].get_first_name() == "FirstNameChanged"
    assert emp_dict[x.username.get()].get_last_name() == "LastNameChanged"
    assert emp_dict[x.username.get()].get_address() == "StreetChanged"
    assert emp_dict[x.username.get()].get_city() == "CityChanged"
    assert emp_dict[x.username.get()].get_zip() == "ZIPChanged"
    assert emp_dict[x.username.get()].get_class() == "2"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) == "1.00"
    assert str(emp_dict[x.username.get()].get_commission_rate()) == "10.00"
    assert str(emp_dict[x.username.get()].get_salary()) == "100.00"
    assert emp_dict[x.username.get()].get_office_phone() == "OfficePChanged"
    assert emp_dict[x.username.get()].get_office_email() == "OfficeEChanged"
    assert emp_dict[x.username.get()].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[x.username.get()].get_personal_email() == "PersonalEChanged"
    assert emp_dict[x.username.get()].get_dob() == "BirthdayChanged"
    assert emp_dict[x.username.get()].get_ssn() == "SSNChanged"
    assert emp_dict[x.username.get()].get_pay_method() == "1"
    assert emp_dict[x.username.get()].get_routing() == "RoutingChanged"
    assert emp_dict[x.username.get()].get_account() == "AccountChanged"
    assert emp_dict[x.username.get()].get_title() == "MasterChanged"
    assert emp_dict[x.username.get()].get_dept() == "DeptChanged"
    assert emp_dict[x.username.get()].get_start() == "1/2/2022"
    if (emp_dict[x.username.get()].get_status() == True):
        assert e.emp_status.get() == "Active"
    else:
        assert e.emp_status.get() == "Deactivated"

def test_edit_6():
    x.username.set("6")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    e = EmpDat_v5.Edit_Page(v, controller=x)
    e.f_name.set("FirstNameChanged")
    e.l_name.set("LastNameChanged")
    e.street.set("StreetChanged")
    e.city.set("CityChanged")
    e.zip.set("ZIPChanged")
    e.classification.set("1")
    e.pay_type.set("1")
    e.salary.set("100.00")
    e.commissioned.set("10.00")
    e.hourly.set("1.00")
    e.routing_num.set("RoutingChanged")
    e.account_num.set("AccountChanged")
    e.o_phone.set("OfficePChanged")
    e.p_phone.set("PersonalPChanged")
    e.o_email.set("OfficeEChanged")
    e.p_email.set("PersonalEChanged")
    e.dob.set("BirthdayChanged")
    e.ssn.set("SSNChanged")
    e.emp_title.set("MasterChanged")
    e.emp_dept.set("DeptChanged")
    e.start_date.set("1/2/2022")
    e.update_emp()
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[x.username.get()].get_first_name() == "FirstNameChanged"
    assert emp_dict[x.username.get()].get_last_name() == "LastNameChanged"
    assert emp_dict[x.username.get()].get_address() == "StreetChanged"
    assert emp_dict[x.username.get()].get_city() == "CityChanged"
    assert emp_dict[x.username.get()].get_zip() == "ZIPChanged"
    assert emp_dict[x.username.get()].get_class() == "1"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) == "1.00"
    assert str(emp_dict[x.username.get()].get_commission_rate()) == "10.00"
    assert str(emp_dict[x.username.get()].get_salary()) == "100.00"
    assert emp_dict[x.username.get()].get_office_phone() == "OfficePChanged"
    assert emp_dict[x.username.get()].get_office_email() == "OfficeEChanged"
    assert emp_dict[x.username.get()].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[x.username.get()].get_personal_email() == "PersonalEChanged"
    assert emp_dict[x.username.get()].get_dob() == "BirthdayChanged"
    assert emp_dict[x.username.get()].get_ssn() == "SSNChanged"
    assert emp_dict[x.username.get()].get_pay_method() == "1"
    assert emp_dict[x.username.get()].get_routing() == "RoutingChanged"
    assert emp_dict[x.username.get()].get_account() == "AccountChanged"
    assert emp_dict[x.username.get()].get_title() == "MasterChanged"
    assert emp_dict[x.username.get()].get_dept() == "DeptChanged"
    assert emp_dict[x.username.get()].get_start() == "1/2/2022"
    if (emp_dict[x.username.get()].get_status() == True):
        assert e.emp_status.get() == "Active"
    else:
        assert e.emp_status.get() == "Deactivated"

#This tests that if all fields are invalid, that the error will pop up and variables will not have changed
#it then tries to change to all valid variables
def test_edit_invalid_variable_1():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    e = EmpDat_v5.Edit_Page(v, controller=x)
    e.f_name.set("123")
    e.l_name.set("123")
    e.street.set("123")
    e.city.set("123")
    e.zip.set("123")
    e.classification.set("asd")
    e.pay_type.set("asd")
    e.salary.set("asd")
    e.commissioned.set("asd")
    e.hourly.set("asd")
    e.routing_num.set("123")
    e.account_num.set("123")
    e.o_phone.set("123")
    e.p_phone.set("123")
    e.o_email.set("123")
    e.p_email.set("123")
    e.dob.set("123")
    e.ssn.set("123")
    e.emp_title.set("123")
    e.emp_dept.set("123")
    e.start_date.set("asd")
    e.update_emp()
    assert e.page_error.get() == "One or more entries invalid!"

    assert emp_dict[x.username.get()].get_first_name() != "123"
    assert emp_dict[x.username.get()].get_last_name() != "123"
    assert emp_dict[x.username.get()].get_address() != "123"
    assert emp_dict[x.username.get()].get_city() != "123"
    assert emp_dict[x.username.get()].get_zip() != "123"
    assert emp_dict[x.username.get()].get_class() != "asd"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) != "asd"
    assert str(emp_dict[x.username.get()].get_commission_rate()) != "asd"
    assert str(emp_dict[x.username.get()].get_salary()) != "asd"
    assert emp_dict[x.username.get()].get_office_phone() != "123"
    assert emp_dict[x.username.get()].get_office_email() != "123"
    assert emp_dict[x.username.get()].get_personal_phone() != "123"
    assert emp_dict[x.username.get()].get_personal_email() != "123"
    assert emp_dict[x.username.get()].get_dob() != "123"
    assert emp_dict[x.username.get()].get_ssn() != "123"
    assert emp_dict[x.username.get()].get_pay_method() != "abc"
    assert emp_dict[x.username.get()].get_routing() != "123"
    assert emp_dict[x.username.get()].get_account() != "123"
    assert emp_dict[x.username.get()].get_title() != "123"
    assert emp_dict[x.username.get()].get_dept() != "123"
    assert emp_dict[x.username.get()].get_start() != "asd"

    e.f_name.set("FirstNameChanged")
    e.l_name.set("LastNameChanged")
    e.street.set("StreetChanged")
    e.city.set("CityChanged")
    e.zip.set("ZIPChanged")
    e.classification.set("2")
    e.pay_type.set("1")
    e.salary.set("100.00")
    e.commissioned.set("10.00")
    e.hourly.set("1.00")
    e.routing_num.set("RoutingChanged")
    e.account_num.set("AccountChanged")
    e.o_phone.set("OfficePChanged")
    e.p_phone.set("PersonalPChanged")
    e.o_email.set("OfficeEChanged")
    e.p_email.set("PersonalEChanged")
    e.dob.set("BirthdayChanged")
    e.ssn.set("SSNChanged")
    e.emp_title.set("MasterChanged")
    e.emp_dept.set("DeptChanged")
    e.start_date.set("1/2/2022")
    e.update_emp()
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[x.username.get()].get_first_name() == "FirstNameChanged"
    assert emp_dict[x.username.get()].get_last_name() == "LastNameChanged"
    assert emp_dict[x.username.get()].get_address() == "StreetChanged"
    assert emp_dict[x.username.get()].get_city() == "CityChanged"
    assert emp_dict[x.username.get()].get_zip() == "ZIPChanged"
    assert emp_dict[x.username.get()].get_class() == "2"
    assert str(emp_dict[x.username.get()].get_hourly_rate()) == "1.00"
    assert str(emp_dict[x.username.get()].get_commission_rate()) == "10.00"
    assert str(emp_dict[x.username.get()].get_salary()) == "100.00"
    assert emp_dict[x.username.get()].get_office_phone() == "OfficePChanged"
    assert emp_dict[x.username.get()].get_office_email() == "OfficeEChanged"
    assert emp_dict[x.username.get()].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[x.username.get()].get_personal_email() == "PersonalEChanged"
    assert emp_dict[x.username.get()].get_dob() == "BirthdayChanged"
    assert emp_dict[x.username.get()].get_ssn() == "SSNChanged"
    assert emp_dict[x.username.get()].get_pay_method() == "1"
    assert emp_dict[x.username.get()].get_routing() == "RoutingChanged"
    assert emp_dict[x.username.get()].get_account() == "AccountChanged"
    assert emp_dict[x.username.get()].get_title() == "MasterChanged"
    assert emp_dict[x.username.get()].get_dept() == "DeptChanged"
    assert emp_dict[x.username.get()].get_start() == "1/2/2022"
    if (emp_dict[x.username.get()].get_status() == True):
        assert e.emp_status.get() == "Active"
    else:
        assert e.emp_status.get() == "Deactivated"


#CODE TO TEST ADD PAGE
def test_add_1():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    a = EmpDat_v5.Add_Page(v, controller=x)
    a.f_name.set("FirstNameChanged")
    a.l_name.set("LastNameChanged")
    a.street.set("StreetChanged")
    a.city.set("CityChanged")
    a.emp_state.set("StateChanged")
    a.zip.set("ZIPChanged")
    a.classification.set("2")
    a.pay_type.set("1")
    a.salary.set("100.00")
    a.commissioned.set("10.00")
    a.hourly.set("1.00")
    a.routing_num.set("RoutingChanged")
    a.account_num.set("AccountChanged")
    a.o_phone.set("OfficePChanged")
    a.p_phone.set("PersonalPChanged")
    a.o_email.set("OfficeEChanged")
    a.p_email.set("PersonalEChanged")
    a.dob.set("BirthdayChanged")
    a.ssn.set("SSNChanged")
    a.emp_title.set("MasterChanged")
    a.emp_dept.set("DeptChanged")
    a.emp_password.set("test")
    a.permission.set("1")
    a.add_emp()
    assert a.page_error.get() != "Missing required fields!"
    assert a.page_error.get() != "One or more entries invalid!"
    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[str(len(emp_dict.keys()))].get_first_name() == "FirstNameChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_last_name() == "LastNameChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_address() == "StreetChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_city() == "CityChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_zip() == "ZIPChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_class() == "2"
    assert str(emp_dict[str(len(emp_dict.keys()))].get_hourly_rate()) == "1.0"
    assert str(emp_dict[str(len(emp_dict.keys()))].get_commission_rate()) == "10.0"
    assert str(emp_dict[str(len(emp_dict.keys()))].get_salary()) == "100.0"
    assert emp_dict[str(len(emp_dict.keys()))].get_office_phone() == "OfficePChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_office_email() == "OfficeEChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_personal_email() == "PersonalEChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_dob() == "BirthdayChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_ssn() == "SSNChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_pay_method() == "1"
    assert emp_dict[str(len(emp_dict.keys()))].get_routing() == "RoutingChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_account() == "AccountChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_title() == "MasterChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_dept() == "DeptChanged"
    if (emp_dict[str(len(emp_dict.keys()))].get_status() == True):
        assert a.emp_status.get() == "Active"
    else:
        assert a.emp_status.get() == "Deactivated"

#Test for all correct fields except one, then correct field
def test_add_incorrect_1():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    v = EmpDat_v5.View_Page(parent=x.container, controller=x)
    a = EmpDat_v5.Add_Page(v, controller=x)
    a.f_name.set("FirstNameChanged")
    a.l_name.set("LastNameChanged")
    a.street.set("StreetChanged")
    a.city.set("CityChanged")
    a.emp_state.set("StateChanged")
    a.zip.set("ZIPChanged")
    a.classification.set("2")
    a.pay_type.set("1")
    a.salary.set("100.00")
    a.commissioned.set("10.00")
    a.hourly.set("asd")
    a.routing_num.set("RoutingChanged")
    a.account_num.set("AccountChanged")
    a.o_phone.set("OfficePChanged")
    a.p_phone.set("PersonalPChanged")
    a.o_email.set("OfficeEChanged")
    a.p_email.set("PersonalEChanged")
    a.dob.set("BirthdayChanged")
    a.ssn.set("SSNChanged")
    a.emp_title.set("MasterChanged")
    a.emp_dept.set("DeptChanged")
    a.emp_password.set("test")
    a.permission.set("1")
    a.add_emp()
    assert a.page_error.get() != "Missing required fields!"
    assert a.page_error.get() == "One or more entries invalid!"

    a.hourly.set("1.00")
    a.add_emp()

    if (emp_dict[x.username.get()].is_admin() == True):
        assert v.permission.get() == '1'
    else:
        assert v.permission.get() == '2'
    assert emp_dict[str(len(emp_dict.keys()))].get_first_name() == "FirstNameChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_last_name() == "LastNameChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_address() == "StreetChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_city() == "CityChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_zip() == "ZIPChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_class() == "2"
    assert str(emp_dict[str(len(emp_dict.keys()))].get_hourly_rate()) == "1.0"
    assert str(emp_dict[str(len(emp_dict.keys()))].get_commission_rate()) == "10.0"
    assert str(emp_dict[str(len(emp_dict.keys()))].get_salary()) == "100.0"
    assert emp_dict[str(len(emp_dict.keys()))].get_office_phone() == "OfficePChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_office_email() == "OfficeEChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_personal_phone() == "PersonalPChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_personal_email() == "PersonalEChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_dob() == "BirthdayChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_ssn() == "SSNChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_pay_method() == "1"
    assert emp_dict[str(len(emp_dict.keys()))].get_routing() == "RoutingChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_account() == "AccountChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_title() == "MasterChanged"
    assert emp_dict[str(len(emp_dict.keys()))].get_dept() == "DeptChanged"
    if (emp_dict[str(len(emp_dict.keys()))].get_status() == True):
        assert a.emp_status.get() == "Active"
    else:
        assert a.emp_status.get() == "Deactivated"


#CODE FOR TESTING SEARCH PAGE
#Test_1 searches for a user that should be in the database
def test_search_1():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Search_Page(parent=x.container, controller=x)
    s.search_parameter.set("id")
    s.search.set("5")
    s.search_employees()
    assert s.search.get() == ""
    assert s.msg.get() != "Must choose a search parameter"
    assert s.msg.get() != "ID not found!"
    assert s.msg.get() != "Last Name not found!"

def test_search_2():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Search_Page(parent=x.container, controller=x)
    s.search.set("1")
    s.search_employees()
    assert s.msg.get() == "Must choose a search parameter"

def test_search_3():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Search_Page(parent=x.container, controller=x)
    s.search_parameter.set("id")
    s.search.set("100")
    s.search_employees()
    assert s.msg.get() == "ID not found!"
    assert s.search.get() != ""

def test_search_4():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Search_Page(parent=x.container, controller=x)
    s.search_parameter.set("last")
    s.search.set("johnasdk")
    s.search_employees()
    assert s.msg.get() == "Last Name not found!"

def test_search_4():
    x.username.set("5")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Search_Page(parent=x.container, controller=x)
    s.search_parameter.set("last")
    s.search.set("LastNameChanged")
    s.search_employees()
    assert s.search.get() == ""
    assert s.msg.get() != "Must choose a search parameter"
    assert s.msg.get() != "ID not found!"
    assert s.msg.get() != "Last Name not found!"


#CODE FOR TESTING PAY PAGE
def test_pay_1():
    x.username.set("2")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Pay_Page(parent=x.container, controller=x)
    if (str(emp_dict["2"].get_classification()) == "Salaried Employee"):
        s.create_add_frame(2)
        s.emp_to_add.set("2")
        s.amount.set("100")
        s.add_item(2)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() == "Specified Employee has incorrect classification!"
    elif (str(emp_dict["2"].get_classification()) == "Hourly Employee"):
        s.create_add_frame(2)
        s.emp_to_add.set("2")
        s.amount.set("100")
        s.add_item(2)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() != "Specified Employee has incorrect classification!"
        assert s.add_error_msg.get() != "Amount must enter either a number or a decimal!"
    else:
        s.create_add_frame(1)
        s.emp_to_add.set("2")
        s.amount.set("100")
        s.add_item(1)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() != "Specified Employee has incorrect classification!"
        assert s.add_error_msg.get() != "Amount must enter either a number or a decimal!"

def test_pay_2():
    x.username.set("2")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Pay_Page(parent=x.container, controller=x)
    if (str(emp_dict["3"].get_classification()) == "Salaried Employee"):
        s.create_add_frame(2)
        s.emp_to_add.set("3")
        s.amount.set("100")
        s.add_item(2)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() == "Specified Employee has incorrect classification!"
    elif (str(emp_dict["3"].get_classification()) == "Hourly Employee"):
        s.create_add_frame(2)
        s.emp_to_add.set("3")
        s.amount.set("100")
        s.add_item(2)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() != "Specified Employee has incorrect classification!"
        assert s.add_error_msg.get() != "Amount must enter either a number or a decimal!"
    else:
        s.create_add_frame(1)
        s.emp_to_add.set("3")
        s.amount.set("100")
        s.add_item(1)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() != "Specified Employee has incorrect classification!"
        assert s.add_error_msg.get() != "Amount must enter either a number or a decimal!"

def test_pay_3():
    x.username.set("2")
    x.user_pass.set("test")
    x.validate_user()
    s = EmpDat_v5.Pay_Page(parent=x.container, controller=x)
    if (str(emp_dict["7"].get_classification()) == "Salaried Employee"):
        s.create_add_frame(2)
        s.emp_to_add.set("7")
        s.amount.set("100")
        s.add_item(2)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() == "Specified Employee has incorrect classification!"
    elif (str(emp_dict["7"].get_classification()) == "Hourly Employee"):
        s.create_add_frame(2)
        s.emp_to_add.set("7")
        s.amount.set("100")
        s.add_item(2)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() != "Specified Employee has incorrect classification!"
        assert s.add_error_msg.get() != "Amount must enter either a number or a decimal!"
    else:
        s.create_add_frame(1)
        s.emp_to_add.set("7")
        s.amount.set("100")
        s.add_item(1)
        assert s.add_error_msg.get() != "Invalid Employee ID!"
        assert s.add_error_msg.get() != "Specified Employee has incorrect classification!"
        assert s.add_error_msg.get() != "Amount must enter either a number or a decimal!"