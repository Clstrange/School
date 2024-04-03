#EmpDat_v7
'''
NOTES:
    -This should work fine as long as it's in the Emp_Trak directory

Changes Made: (Ethan Taylor Mar 23)
    -Added dropdown search filter to search page
    -Implemented style for error message
    -Implemented a check for empty fields on the View Page
    
Changes Still Needed:
    -Implement user manual into help button
    -More themes and styles?
'''

from re import I
import tkinter.messagebox

from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont
from turtle import width, xcor
from typing import List
from employee_v3 import *
from datetime import datetime
from database_module import *
   
class EmpApp(Tk):

    def __init__(self, database=None, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.emp_dat = database
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.title("EmpDat")
        self.user = None
        self.target = None
        #Set themes/styles
        s = ttk.Style()
        s.configure('Error.TLabel', font='helvetica 14', foreground='red') #Error style
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = ttk.Frame(self)
        self.container.grid(column=0, row=0, sticky=(N,W,E,S))
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        
        self.login(self.container)

    def login(self, container):
        '''Builds the login screen of the app'''

        #Set up frame
        self.login_page = ttk.Frame(container)
        self.login_page.grid(row=0, column=0, sticky="nsew")
        ttk.Label(self.login_page, text="Login", font=self.title_font).grid(column=0, row=0, sticky=(N,S), columnspan=3)
         
        #Set up username labels/entry
        self.username = StringVar()
        self.name_entry = ttk.Entry(self.login_page, width=20, textvariable=self.username)
        self.name_entry.grid(column=2, row=2, sticky=(W,E))
        ttk.Label(self.login_page, text="Employee ID").grid(column=1, row=2, sticky=E)
        self.name_entry.bind('<Return>', lambda e: self.validate_user())
        
        #Set up user password labels/entry
        self.user_pass = StringVar()
        pass_entry = ttk.Entry(self.login_page, width=20, textvariable=self.user_pass, show="*")
        pass_entry.grid(column=2, row=3, sticky=(W,E))
        ttk.Label(self.login_page, text="Password").grid(column=1, row=3, sticky=E)
        pass_entry.bind('<Return>', lambda e: self.validate_user())
        
        #Set up submit button
        ttk.Button(self.login_page, text="Enter", command=self.validate_user).grid(column=2, row=4, sticky=E)

        #Set up message label
        self.msg = StringVar()
        ttk.Label(self.login_page, textvariable=self.msg,
                  style='Error.TLabel').grid(column=0, row=4, sticky=W, columnspan=2)
        self.msg.set("")

        #Extra Formatting
        for child in self.login_page.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        self.name_entry.focus()

        #Intercept close button
        self.protocol("WM_DELETE_WINDOW", lambda: self.close_confirm(self))

    def validate_user(self):
        '''Validates user input'''
        name = self.username.get()
        password = self.user_pass.get()
        
        if (name not in self.emp_dat.keys()
            or self.emp_dat[name].get_status() == False): #Employee ID not in database or deactivated
            self.msg.set("Invalid ID!")
            self.username.set("")
            self.user_pass.set("")
            self.name_entry.focus()
        elif password != self.emp_dat[name].get_password(): #Employee ID does not match password
            self.msg.set("Incorrect password or ID!")
            self.username.set("")
            self.user_pass.set("")
            self.name_entry.focus()
        else:
            self.user = self.emp_dat[name]
            self.target = self.emp_dat[name]
            for F in (View_Page, Search_Page, Edit_Page, Add_Page, Pay_Page):
                page_name = F.__name__
                frame = F(parent=self.container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame("View_Page")

    def show_manual(self, *args):
        '''Function that will show the user manual whenever the Help button is pressed'''
        tkinter.messagebox.showinfo(message='WIP -- Will eventually show the User Manual',
                            parent=self)
        self.focus()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.reset_frames()
        frame = self.frames[page_name]
        frame.tkraise()

    def reset_frames(self):
        '''Resets all frames'''
        for frame in self.frames.values():
            frame.destroy()
        for F in (View_Page, Search_Page, Edit_Page, Add_Page, Pay_Page):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def close_confirm(self, window):
        '''Asks for confirmation when the close button is clicked'''
        confirmation = tkinter.messagebox.askokcancel(message="Do you wish to close the program?",
                                              parent=self)
        if confirmation == True:
            window.destroy()
        else:
            window.focus()




class View_Page(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        #Set up frame name
        self.create_frame_name()

        #Set up page error message
        self.create_error_label()
        
        #Set up sidebar buttons
        self.create_sidebar(self.controller.user, self.controller.target)

        #Set up labels/entries based on target
        self.create_profile(self.controller.user, self.controller.target)

    def create_frame_name(self):
        '''Creates a frame for the name of the viewed employee'''
        self.frame_name = StringVar()
        emp_name = self.controller.target.get_first_name() + " " + self.controller.target.get_last_name()
        self.frame_name.set("Viewing " + emp_name)
        title = ttk.Label(self,
                          textvariable=self.frame_name,
                          font=self.controller.title_font)
        title.grid(column=1, row=0, sticky=(N,S))

    def create_sidebar(self, user, target):
        '''Creates the buttons in the sidemenu based on user permission'''
        self.sidebar = ttk.Frame(self)
        self.sidebar.grid(column=0, row=0, sticky=(N,W,E,S), rowspan=6)
        if user.is_admin() == True: #admin view
            edit = ttk.Button(self.sidebar, text="Edit Employee",
                              command=lambda: self.controller.show_frame("Edit_Page"))
            edit.grid(column=0, row=0, sticky=(N,W,E,S))
            add = ttk.Button(self.sidebar, text="Add Employee",
                             command=lambda: self.controller.show_frame("Add_Page"))
            add.grid(column=0, row=1, sticky=(N,W,E,S))
            fire = ttk.Button(self.sidebar, text="Deactivate Employee",
                              command=lambda: self.deactivate_emp(target))
            fire.grid(column=0, row=2, sticky=(N,W,E,S))
            if target.get_status() == False:
                fire.configure(state=DISABLED)
            search = ttk.Button(self.sidebar, text="Search Employee",
                                command=lambda: self.controller.show_frame("Search_Page"))
            search.grid(column=0, row=3, sticky=(N,W,E,S))
            pay = ttk.Button(self.sidebar, text="Run Payroll",
                             command=lambda: self.controller.show_frame("Pay_Page"))
            pay.grid(column=0, row=4, sticky=(N,W,E,S))
            user_manual = ttk.Button(self.sidebar, text="Help",
                                     command=lambda: self.controller.show_manual())
            user_manual.grid(column=0, row=5, sticky=(N,W,E,S))
        elif user == target: #general viewing themselves
            edit = ttk.Button(self.sidebar, text="Edit Employee",
                              command=lambda: self.controller.show_frame("Edit_Page"))
            edit.grid(column=0, row=0, sticky=(N,W,E,S))
            search = ttk.Button(self.sidebar, text="Search Employee",
                                command=lambda: self.controller.show_frame("Search_Page"))
            search.grid(column=0, row=1, sticky=(N,W,E,S))
            user_manual = ttk.Button(self.sidebar, text="Help",
                                     command=lambda: self.controller.show_manual())
            user_manual.grid(column=0, row=2, sticky=(N,W,E,S))
        else: #general view
            search = ttk.Button(self.sidebar, text="Search Employee",
                                command=lambda: self.controller.show_frame("Search_Page"))
            search.grid(column=0, row=1, sticky=(N,W,E,S))
            user_manual = ttk.Button(self.sidebar, text="Help",
                                     command=lambda: self.controller.show_manual())
            user_manual.grid(column=0, row=2, sticky=(N,W,E,S))
        for child in self.sidebar.winfo_children():
            child.grid_configure(padx=5, pady=20)

    def create_profile(self, user, target):
        '''Creates all the labels/entries to show the target employee's profile,
        based on user's permission'''
        self.profile = ttk.Frame(self)
        self.profile.grid(column=1, row=1, sticky=(N,W,E,S))
        #Create lists for easier manipulation of select widgets
        self.entry_list = []
        self.entry_data_list = []
        self.general_entry_list = []
        if user.is_admin() == True or user == target: #admin view or general viewing self
            #Set up Employee ID labels/entry/error
            id_label = ttk.Label(self.profile, text="Employee ID:")
            id_label.grid(column=0, row=1, sticky=E)
            self.id = StringVar()
            self.id.set(target.get_id())
            self.entry_data_list.append(self.id)
            self.id_entry = ttk.Entry(self.profile, textvariable=self.id)
            self.id_entry.grid(column=1, row=1, sticky=W)
            self.entry_list.append(self.id_entry)
#             self.id_error = StringVar()
#             self.id_error_label = ttk.Label(profile, textvariable=self.id_error)
#             self.id_error_label.grid(column=0, row=2, columnspan=2)
            #Set up first name labels/entry/error
            f_name_label = ttk.Label(self.profile, text="First Name:")
            f_name_label.grid(column=0, row=3, sticky=E)
            self.f_name = StringVar()
            self.f_name.set(target.get_first_name())
            self.entry_data_list.append(self.f_name)
            self.f_name_entry = ttk.Entry(self.profile, textvariable=self.f_name)
            self.f_name_entry.grid(column=1, row=3, sticky=W)
            self.entry_list.append(self.f_name_entry)
#             self.f_name_error = StringVar()
#             self.f_name_error_label = ttk.Label(profile, textvariable=self.f_name_error)
#             self.f_name_error_label.grid(column=0, row=4, columnspan=2)
            #Set up last name labels/entry/error
            l_name_label = ttk.Label(self.profile, text="Last Name:")
            l_name_label.grid(column=0, row=5, sticky=E)
            self.l_name = StringVar()
            self.l_name.set(target.get_last_name())
            self.entry_data_list.append(self.l_name)
            self.l_name_entry = ttk.Entry(self.profile, textvariable=self.l_name)
            self.l_name_entry.grid(column=1, row=5, sticky=W)
            self.entry_list.append(self.l_name_entry)
#             self.l_name_error = StringVar()
#             self.l_name_error_label = ttk.Label(profile, textvariable=self.l_name_error)
#             self.l_name_error_label.grid(column=0, row=6, columnspan=2)
            #Set up street labels/entry/error
            street_label = ttk.Label(self.profile, text="Address:")
            street_label.grid(column=0, row=7, sticky=E)
            self.street = StringVar()
            self.street.set(target.get_address())
            self.entry_data_list.append(self.street)
            self.street_entry = ttk.Entry(self.profile, textvariable=self.street)
            self.street_entry.grid(column=1, row=7, sticky=W)
            self.entry_list.append(self.street_entry)
#             self.street_error = StringVar()
#             self.street_error_label = ttk.Label(profile, textvariable=self.street_error)
#             self.street_error_label.grid(column=0, row=8, columnspan=2)
            #Set up city labels/entry/error
            city_label = ttk.Label(self.profile, text="City:")
            city_label.grid(column=0, row=9, sticky=E)
            self.city = StringVar()
            self.city.set(target.get_city())
            self.entry_data_list.append(self.city)
            self.city_entry = ttk.Entry(self.profile, textvariable=self.city)
            self.city_entry.grid(column=1, row=9, sticky=W)
            self.entry_list.append(self.city_entry)
#             self.city_error = StringVar()
#             self.city_error_label = ttk.Label(profile, textvariable=self.city_error)
#             self.city_error_label.grid(column=0, row=10, columnspan=2)
            #Set up state labels/entry/error
            state_label = ttk.Label(self.profile, text="State:")
            state_label.grid(column=0, row=11, sticky=E)
            self.state = StringVar()
            self.state.set(target.get_state())
            self.entry_data_list.append(self.state)
            self.state_entry = ttk.Entry(self.profile, textvariable=self.state)
            self.state_entry.grid(column=1, row=11, sticky=W)
            self.entry_list.append(self.state_entry)
#             self.state_error = StringVar()
#             self.state_error_label = ttk.Label(profile, textvariable=self.state_error)
#             self.state_error_label.grid(column=0, row=12, columnspan=2)
            #Set up zip labels/entry/error
            zip_label = ttk.Label(self.profile, text="Zip:")
            zip_label.grid(column=0, row=13, sticky=E)
            self.zip = StringVar()
            self.zip.set(target.get_zip())
            self.entry_data_list.append(self.zip)
            self.zip_entry = ttk.Entry(self.profile, textvariable=self.zip)
            self.zip_entry.grid(column=1, row=13, sticky=W)
            self.entry_list.append(self.zip_entry)
#             self.zip_error = StringVar()
#             self.zip_error_label = ttk.Label(profile, textvariable=self.zip_error)
#             self.zip_error_label.grid(column=0, row=14, columnspan=2)
            #Set up classification labels/entry/error
            class_label = ttk.Label(self.profile, text="Classification:\n(1=Salaried, 2=Commissioned, 3=Hourly)")
            class_label.grid(column=0, row=15, sticky=E)
            self.classification = StringVar()
            self.classification.set(target.get_class())
            self.entry_data_list.append(self.classification)
            self.class_entry = ttk.Entry(self.profile, textvariable=self.classification)
            self.class_entry.grid(column=1, row=15, sticky=W)
            self.entry_list.append(self.class_entry)
#             self.class_error = StringVar()
#             self.class_error_label = ttk.Label(profile, textvariable=self.class_error)
#             self.class_error_label.grid(column=0, row=16, columnspan=2)
            #Set up hourly labels/entry/error
            hourly_label = ttk.Label(self.profile, text="Hourly Rate:")
            hourly_label.grid(column=0, row=17, sticky=E)
            self.hourly = StringVar()
            self.hourly.set(target.get_hourly_rate())
            self.entry_data_list.append(self.hourly)
            self.hourly_entry = ttk.Entry(self.profile, textvariable=self.hourly)
            self.hourly_entry.grid(column=1, row=17, sticky=W)
            self.entry_list.append(self.hourly_entry)
#             self.hourly_error = StringVar()
#             self.hourly_error_label = ttk.Label(profile, textvariable=self.hourly_error)
#             self.hourly_error_label.grid(column=0, row=18, columnspan=2)
            #Set up commissioned labels/entry/error
            commission_label = ttk.Label(self.profile, text="Commission Rate:")
            commission_label.grid(column=0, row=19, sticky=E)
            self.commissioned = StringVar()
            self.commissioned.set(target.get_commission_rate())
            self.entry_data_list.append(self.commissioned)
            self.commission_entry = ttk.Entry(self.profile, textvariable=self.commissioned)
            self.commission_entry.grid(column=1, row=19, sticky=W)
            self.entry_list.append(self.commission_entry)
#             self.commission_error = StringVar()
#             self.commission_error_label = ttk.Label(profile, textvariable=self.commission_error)
#             self.commission_error_label.grid(column=0, row=20, columnspan=2)
            #Set up salary labels/entry/error
            salary_label = ttk.Label(self.profile, text="Salary:")
            salary_label.grid(column=0, row=21, sticky=E)
            self.salary = StringVar()
            self.salary.set(target.get_salary())
            self.entry_data_list.append(self.salary)
            self.salary_entry = ttk.Entry(self.profile, textvariable=self.salary)
            self.salary_entry.grid(column=1, row=21, sticky=W)
            self.entry_list.append(self.salary_entry)
#             self.salary_error = StringVar()
#             self.salary_error_label = ttk.Label(profile, textvariable=self.salary_error)
#             self.salary_error_label.grid(column=0, row=22, columnspan=2)
            #Set up office phone labels/entry/error
            o_phone_label = ttk.Label(self.profile, text="Office Phone:")
            o_phone_label.grid(column=0, row=23, sticky=E)
            self.o_phone = StringVar()
            self.o_phone.set(target.get_office_phone())
            self.entry_data_list.append(self.o_phone)
            self.o_phone_entry = ttk.Entry(self.profile, textvariable=self.o_phone)
            self.o_phone_entry.grid(column=1, row=23, sticky=W)
            self.entry_list.append(self.o_phone_entry)
#             self.o_phone_error = StringVar()
#             self.o_phone_error_label = ttk.Label(profile, textvariable=self.o_phone_error)
#             self.o_phone_error_label.grid(column=0, row=24, columnspan=2)
            #Set up office email labels/entry/error
            o_email_label = ttk.Label(self.profile, text="Office Email:")
            o_email_label.grid(column=0, row=25, sticky=E)
            self.o_email = StringVar()
            self.o_email.set(target.get_office_email())
            self.entry_data_list.append(self.o_email)
            self.o_email_entry = ttk.Entry(self.profile, textvariable=self.o_email)
            self.o_email_entry.grid(column=1, row=25, sticky=W)
            self.entry_list.append(self.o_email_entry)
#             self.o_email_error = StringVar()
#             self.o_email_error_label = ttk.Label(profile, textvariable=self.o_email_error)
#             self.o_email_error_label.grid(column=0, row=26, columnspan=2)
            #Set up personal phone labels/entry/paste
            p_phone_label = ttk.Label(self.profile, text="Personal Phone:")
            p_phone_label.grid(column=0, row=27, sticky=E)
            self.p_phone = StringVar()
            self.p_phone.set(target.get_personal_phone())
            self.entry_data_list.append(self.p_phone)
            self.p_phone_entry = ttk.Entry(self.profile, textvariable=self.p_phone)
            self.p_phone_entry.grid(column=1, row=27, sticky=W)
            self.entry_list.append(self.p_phone_entry)
#             self.p_phone_error = StringVar()
#             self.p_phone_error_label = ttk.Label(profile, textvariable=self.p_phone_error)
#             self.p_phone_error_label.grid(column=0, row=28, columnspan=2)
            #Set up personal email labels/entry/error
            p_email_label = ttk.Label(self.profile, text="Personal Email:")
            p_email_label.grid(column=0, row=29, sticky=E)
            self.p_email = StringVar()
            self.p_email.set(target.get_personal_email())
            self.entry_data_list.append(self.p_email)
            self.p_email_entry = ttk.Entry(self.profile, textvariable=self.p_email)
            self.p_email_entry.grid(column=1, row=29, sticky=W)
            self.entry_list.append(self.p_email_entry)
#             self.p_email_error = StringVar()
#             self.p_email_error_label = ttk.Label(profile, textvariable=self.p_email_error)
#             self.p_email_error_label.grid(column=0, row=30, columnspan=2)
            #Set up DOB labels/entry/error
            dob_label = ttk.Label(self.profile, text="Date of Birth:")
            dob_label.grid(column=2, row=1, sticky=E)
            self.dob = StringVar()
            self.dob.set(target.get_dob())
            self.entry_data_list.append(self.dob)
            self.dob_entry = ttk.Entry(self.profile, textvariable=self.dob)
            self.dob_entry.grid(column=3, row=1, sticky=W)
            self.entry_list.append(self.dob_entry)
#             self.dob_error = StringVar()
#             self.dob_error_label = ttk.Label(profile, textvariable=self.dob_error)
#             self.dob_error_label.grid(column=2, row=2, columnspan=2)
            #Set up SSN labels/entry/error
            ssn_label = ttk.Label(self.profile, text="SSN:")
            ssn_label.grid(column=2, row=3, sticky=E)
            self.ssn = StringVar()
            self.ssn.set(target.get_ssn())
            self.entry_data_list.append(self.ssn)
            self.ssn_entry = ttk.Entry(self.profile, textvariable=self.ssn)
            self.ssn_entry.grid(column=3, row=3, sticky=W)
            self.entry_list.append(self.ssn_entry)
#             self.ssn_error = StringVar()
#             self.ssn_error_label = ttk.Label(profile, textvariable=self.ssn_error)
#             self.ssn_error_label.grid(column=2, row=4, columnspan=2)
            #Set up pay type labels/entry/error
            pay_type_label = ttk.Label(self.profile, text="Pay Method:\n(1=Direct Deposit, 2=Mail)")
            pay_type_label.grid(column=2, row=5, sticky=E)
            self.pay_type = StringVar()
            self.pay_type.set(target.get_pay_method())
            self.entry_data_list.append(self.pay_type)
            self.pay_type_entry = ttk.Entry(self.profile, textvariable=self.pay_type)
            self.pay_type_entry.grid(column=3, row=5, sticky=W)
            self.entry_list.append(self.pay_type_entry)
#             self.pay_type_error = StringVar()
#             self.pay_type_error_label = ttk.Label(profile, textvariable=self.pay_type_error)
#             self.pay_type_error_label.grid(column=2, row=6, columnspan=2)
            #Set up routing num labels/entry/error
            routing_label = ttk.Label(self.profile, text="Routing Num:")
            routing_label.grid(column=2, row=7, sticky=E)
            self.routing_num = StringVar()
            self.routing_num.set(target.get_routing())
            self.entry_data_list.append(self.routing_num)
            self.routing_entry = ttk.Entry(self.profile, textvariable=self.routing_num)
            self.routing_entry.grid(column=3, row=7, sticky=W)
            self.entry_list.append(self.routing_entry)
#             self.routing_error = StringVar()
#             self.routing_error_label = ttk.Label(profile, textvariable=self.routing_error)
#             self.routing_error_label.grid(column=2, row=8, columnspan=2)
            #Set up account num labels/entry/error
            account_label = ttk.Label(self.profile, text="Account Num:")
            account_label.grid(column=2, row=9, sticky=E)
            self.account_num = StringVar()
            self.account_num.set(target.get_account())
            self.entry_data_list.append(self.account_num)
            self.account_entry = ttk.Entry(self.profile, textvariable=self.account_num)
            self.account_entry.grid(column=3, row=9, sticky=W)
            self.entry_list.append(self.account_entry)
#             self.account_error = StringVar()
#             self.account_error_label = ttk.Label(profile, textvariable=self.account_error)
#             self.account_error_label.grid(column=2, row=10, columnspan=2)
            #Set up permission labels/entry/error
            permission_label = ttk.Label(self.profile, text="Permission Level:\n(1=Admin, 2=General)")
            permission_label.grid(column=2, row=11, sticky=E)
            self.permission = StringVar()
            if target.is_admin() == True:
                self.permission.set("1")
            else:
                self.permission.set("2")
            self.entry_data_list.append(self.permission)
            self.permission_entry = ttk.Entry(self.profile, textvariable=self.permission)
            self.permission_entry.grid(column=3, row=11, sticky=W)
            self.entry_list.append(self.permission_entry)
#             self.permission_error = StringVar()
#             self.permission_error_label = ttk.Label(profile, textvariable=self.permission_error)
#             self.permission_error_label.grid(column=2, row=12, columnspan=2)
            #Set up title labels/entry/error
            title_label = ttk.Label(self.profile, text="Title:")
            title_label.grid(column=2, row=13, sticky=E)
            self.emp_title = StringVar()
            self.emp_title.set(target.get_title())
            self.entry_data_list.append(self.emp_title)
            self.title_entry = ttk.Entry(self.profile, textvariable=self.emp_title)
            self.title_entry.grid(column=3, row=13, sticky=W)
            self.entry_list.append(self.title_entry)
#             self.title_error = StringVar()
#             self.title_error_label = ttk.Label(profile, textvariable=self.title_error)
#             self.title_error_label.grid(column=2, row=14, columnspan=2)
            #Set up dept labels/entry/error
            dept_label = ttk.Label(self.profile, text="Dept:")
            dept_label.grid(column=2, row=15, sticky=E)
            self.emp_dept = StringVar()
            self.emp_dept.set(target.get_dept())
            self.entry_data_list.append(self.emp_dept)
            self.dept_entry = ttk.Entry(self.profile, textvariable=self.emp_dept)
            self.dept_entry.grid(column=3, row=15, sticky=W)
            self.entry_list.append(self.dept_entry)
#             self.dept_error = StringVar()
#             self.dept_error_label = ttk.Label(profile, textvariable=self.dept_error)
#             self.dept_error_label.grid(column=2, row=16, columnspan=2)
            #Set up start labels/entry/error
            start_label = ttk.Label(self.profile, text="Start Date:")
            start_label.grid(column=2, row=17, sticky=E)
            self.start_date = StringVar()
            self.start_date.set(target.get_start())
            self.entry_data_list.append(self.start_date)
            self.start_entry = ttk.Entry(self.profile, textvariable=self.start_date)
            self.start_entry.grid(column=3, row=17, sticky=W)
            self.entry_list.append(self.start_entry)
#             self.start_error = StringVar()
#             self.start_error_label = ttk.Label(profile, textvariable=self.start_error)
#             self.start_error_label.grid(column=2, row=18, columnspan=2)
            #Set up end labels/entry/error
            end_label = ttk.Label(self.profile, text="End Date:")
            end_label.grid(column=2, row=19, sticky=E)
            self.end_date = StringVar()
            self.end_date.set(target.get_end())
            self.entry_data_list.append(self.end_date)
            self.end_entry = ttk.Entry(self.profile, textvariable=self.end_date)
            self.end_entry.grid(column=3, row=19, sticky=W)
            self.entry_list.append(self.end_entry)
#             self.end_error = StringVar()
#             self.end_error_label = ttk.Label(profile, textvariable=self.end_error)
#             self.end_error_label.grid(column=2, row=20, columnspan=2)
            #Set up status labels/entry/error
            status_label = ttk.Label(self.profile, text="Status:")
            status_label.grid(column=2, row=21, sticky=E)
            self.emp_status = StringVar()
            if target.get_status() == True:
                self.emp_status.set("Active")
            else:
                self.emp_status.set("Deactivated")
            self.entry_data_list.append(self.emp_status)
            self.status_entry = ttk.Entry(self.profile, textvariable=self.emp_status)
            self.status_entry.grid(column=3, row=21, sticky=W)
            self.entry_list.append(self.status_entry)
#             self.status_error = StringVar()
#             self.status_error_label = ttk.Label(profile, textvariable=self.status_error)
#             self.status_error_label.grid(column=2, row=22, columnspan=2)
            #Set up password labels/entry/error
            pass_label = ttk.Label(self.profile, text="Password:")
            pass_label.grid(column=2, row=23, sticky=E)
            self.emp_password = StringVar()
            self.emp_password.set(target.get_password())
            self.entry_data_list.append(self.emp_password)
            self.pass_entry = ttk.Entry(self.profile, textvariable=self.emp_password)
            self.pass_entry.grid(column=3, row=23, sticky=W)
            self.entry_list.append(self.pass_entry)
#             self.pass_error = StringVar()
#             self.pass_error_label = ttk.Label(profile, textvariable=self.pass_error)
#             self.pass_error_label.grid(column=2, row=24, columnspan=2)
            #Check for empty fields
            for data in self.entry_data_list:
                if data.get() == "":
                    self.page_error.set("This employee is missing information!")
        else: #general viewing other
            #Set up Employee ID labels/entry
            id_label = ttk.Label(self.profile, text="Employee ID:")
            id_label.grid(column=0, row=1, sticky=E)
            self.id = StringVar()
            self.id.set(target.get_id())
            self.id_entry = ttk.Entry(self.profile, textvariable=self.id)
            self.id_entry.grid(column=1, row=1, sticky=W)
            self.general_entry_list.append(self.id_entry)
            #Set up first name labels/entry
            f_name_label = ttk.Label(self.profile, text="First Name:")
            f_name_label.grid(column=0, row=2, sticky=E)
            self.f_name = StringVar()
            self.f_name.set(target.get_first_name())
            self.f_name_entry = ttk.Entry(self.profile, textvariable=self.f_name)
            self.f_name_entry.grid(column=1, row=2, sticky=W)
            self.general_entry_list.append(self.f_name_entry)
            #Set up last name labels/entry
            l_name_label = ttk.Label(self.profile, text="Last Name:")
            l_name_label.grid(column=0, row=3, sticky=E)
            self.l_name = StringVar()
            self.l_name.set(target.get_last_name())
            self.l_name_entry = ttk.Entry(self.profile, textvariable=self.l_name)
            self.l_name_entry.grid(column=1, row=3, sticky=W)
            self.general_entry_list.append(self.l_name_entry)
            #Set up street labels/entry
            street_label = ttk.Label(self.profile, text="Address:")
            street_label.grid(column=0, row=4, sticky=E)
            self.street = StringVar()
            self.street.set(target.get_address())
            self.street_entry = ttk.Entry(self.profile, textvariable=self.street)
            self.street_entry.grid(column=1, row=4, sticky=W)
            self.general_entry_list.append(self.street_entry)
            #Set up city labels/entry
            city_label = ttk.Label(self.profile, text="City:")
            city_label.grid(column=0, row=5, sticky=E)
            self.city = StringVar()
            self.city.set(target.get_city())
            self.city_entry = ttk.Entry(self.profile, textvariable=self.city)
            self.city_entry.grid(column=1, row=5, sticky=W)
            self.general_entry_list.append(self.city_entry)
            #Set up state labels/entry
            state_label = ttk.Label(self.profile, text="State:")
            state_label.grid(column=0, row=6, sticky=E)
            self.state = StringVar()
            self.state.set(target.get_state())
            self.state_entry = ttk.Entry(self.profile, textvariable=self.state)
            self.state_entry.grid(column=1, row=6, sticky=W)
            self.general_entry_list.append(self.state_entry)
            #Set up zip labels/entry
            zip_label = ttk.Label(self.profile, text="Zip:")
            zip_label.grid(column=0, row=7, sticky=E)
            self.zip = StringVar()
            self.zip.set(target.get_zip())
            self.zip_entry = ttk.Entry(self.profile, textvariable=self.zip)
            self.zip_entry.grid(column=1, row=7, sticky=W)
            self.general_entry_list.append(self.zip_entry)
            #Set up office phone labels/entry
            o_phone_label = ttk.Label(self.profile, text="Office Phone:")
            o_phone_label.grid(column=2, row=1, sticky=E)
            self.o_phone = StringVar()
            self.o_phone.set(target.get_office_phone())
            self.o_phone_entry = ttk.Entry(self.profile, textvariable=self.o_phone)
            self.o_phone_entry.grid(column=3, row=1, sticky=W)
            self.general_entry_list.append(self.o_phone_entry)
            #Set up office email labels/entry
            o_email_label = ttk.Label(self.profile, text="Office Email:")
            o_email_label.grid(column=2, row=2, sticky=E)
            self.o_email = StringVar()
            self.o_email.set(target.get_office_email())
            self.o_email_entry = ttk.Entry(self.profile, textvariable=self.o_email)
            self.o_email_entry.grid(column=3, row=2, sticky=W)
            self.general_entry_list.append(self.o_email_entry)
            #Set up title labels/entry
            title_label = ttk.Label(self.profile, text="Title:")
            title_label.grid(column=2, row=3, sticky=E)
            self.emp_title = StringVar()
            self.emp_title.set(target.get_title())
            self.title_entry = ttk.Entry(self.profile, textvariable=self.emp_title)
            self.title_entry.grid(column=3, row=3, sticky=W)
            self.general_entry_list.append(self.title_entry)
            #Set up dept labels/entry
            dept_label = ttk.Label(self.profile, text="Dept:")
            dept_label.grid(column=2, row=4, sticky=E)
            self.emp_dept = StringVar()
            self.emp_dept.set(target.get_dept())
            self.dept_entry = ttk.Entry(self.profile, textvariable=self.emp_dept)
            self.dept_entry.grid(column=3, row=4, sticky=W)
            self.general_entry_list.append(self.dept_entry)
        #Profile Screen Formatting
        for child in self.profile.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.readonly(self.controller.user, True)

    def create_error_label(self):
        '''Creates a label for error messages on the page'''
        self.page_error = StringVar()
        page_error_label = ttk.Label(self, textvariable=self.page_error,
                                     style='Error.TLabel')
        page_error_label.grid(column=1, row=2, pady=10)

    def readonly(self, user, boolean):
        '''Toggles readonly mode for entry fields'''
        if boolean == True:
            for entry in self.entry_list:
                entry.configure(state="readonly")
            for entry in self.general_entry_list:
                entry.configure(state="readonly")
        elif boolean == False:
            if user.is_admin() != True:
                for entry in self.entry_list:
                    if (entry == self.f_name_entry or
                        entry == self.l_name_entry or
                        entry == self.street_entry or
                        entry == self.city_entry or
                        entry == self.state_entry or
                        entry == self.zip_entry or
                        entry == self.p_phone_entry or
                        entry == self.p_email_entry or
                        entry == self.dob_entry or
                        entry == self.ssn_entry or
                        entry == self.pay_type_entry or
                        entry == self.routing_entry or
                        entry == self.account_entry or
                        entry == self.pass_entry
                        ):
                        entry.configure(state="normal")

            else:
                for entry in self.entry_list:
                    entry.configure(state="normal")

    def empty_entries(self):
        '''Empties all of the entry fields'''
        for entry in self.entry_list:
            entry.configure(state="normal")
        for data in self.entry_data_list:
            data.set("")

    def deactivate_emp(self, target):
        '''Creates a confirmation dialog box that if confirmed, deactivates target employee'''
        confirmation = tkinter.messagebox.askokcancel(message="Do you wish to deactivate this employee?",
                                              parent=self.controller)
        if confirmation == True:
            now = datetime.now()
            current_date = now.strftime("%m/%d/%Y")
            target.set_end(current_date)

            # Update employee in DB
            self.controller.target.update_emp_in_db()

            self.controller.show_frame("View_Page")

        self.controller.focus()

    def validate_entry(self, info, grid_num):
        '''Validates the specified employee information'''
        #Classification
        if grid_num == 8:
            if info not in ['1', '2', '3']:
                self.class_error = StringVar()
                self.class_error.set("Must enter either 1, 2, or 3!")
                self.class_error_label = ttk.Label(self.profile, textvariable=self.class_error,
                                                   style='Error.TLabel')
                self.class_error_label.grid(column=0, row=16, columnspan=2, sticky=E)
                return False
            else:
                try:
                    self.class_error_label.grid_remove()
                except AttributeError: #class_error_label not yet grid
                    pass
                return True
        #Salary, Hourly, Commission
        elif grid_num == 9 or grid_num == 10 or grid_num == 11:
            try:
                float(info)
                if grid_num == 9:
                    try:
                        self.hourly_error_label.grid_remove()
                    except AttributeError: #hourly_error_label has not yet been grid
                        pass
                elif grid_num == 10:
                    try:
                        self.commission_error_label.grid_remove()
                    except AttributeError: #commission_error_label has not yet been grid
                        pass
                else:
                    try:
                        self.salary_error_label.grid_remove()
                    except AttributeError: #salary_error_label has not yet been grid
                        pass
                return True
            except ValueError:
                if grid_num == 9:
                    self.hourly_error = StringVar()
                    self.hourly_error.set("Must enter either a number or a decimal!")
                    self.hourly_error_label = ttk.Label(self.profile, textvariable=self.hourly_error,
                                                        style='Error.TLabel')
                    self.hourly_error_label.grid(column=0, row=18, columnspan=2, sticky=E)
                elif grid_num == 10:
                    self.commission_error = StringVar()
                    self.commission_error.set("Must enter either a number or a decimal!")
                    self.commission_error_label = ttk.Label(self.profile, textvariable=self.commission_error,
                                                            style='Error.TLabel')
                    self.commission_error_label.grid(column=0, row=20, columnspan=2, sticky=E)
                else:
                    self.salary_error = StringVar()
                    self.salary_error.set("Must enter either a number or a decimal!")
                    self.salary_error_label = ttk.Label(self.profile, textvariable=self.salary_error,
                                                        style='Error.TLabel')
                    self.salary_error_label.grid(column=0, row=22, columnspan=2, sticky=E)
                return False
        #Pay Method
        elif grid_num == 18:
            if info not in ['1', '2']:
                self.pay_type_error = StringVar()
                self.pay_type_error.set("Must enter either 1 or 2!")
                self.pay_type_error_label = ttk.Label(self.profile, textvariable=self.pay_type_error,
                                                      style='Error.TLabel')
                self.pay_type_error_label.grid(column=2, row=6, columnspan=2, sticky=E)
                return False
            else:
                try:
                    self.pay_type_error_label.grid_remove()
                except AttributeError: #pay_type_error_label has not yet been grid
                    pass
                return True
        #Admin
        elif grid_num == 21:
            if info not in ['1', '2']:
                self.permission_error = StringVar()
                self.permission_error.set("Must enter either 1 or 2!")
                self.permission_error_label = ttk.Label(self.profile, textvariable=self.permission_error,
                                                        style='Error.TLabel')
                self.permission_error_label.grid(column=2, row=12, columnspan=2, sticky=E)
                return False
            else:
                try:
                    self.permission_error_label.grid_remove()
                except AttributeError: #permission_error_label has not yet been grid
                    pass
                return True
        #Other
        else:
            return True




class Edit_Page(View_Page):
    '''Class controlling the edit and add employee pages'''
    def __init__(self, parent, controller):
        View_Page.__init__(self, parent, controller)
        self.controller = controller #root
        self.controller.grid_rowconfigure(0, weight=1)
        self.controller.grid_columnconfigure(0, weight=1)
        user = self.controller.user
        target = self.controller.target
        
        #Set up frame name
        self.frame_name = StringVar()
        emp_name = target.get_first_name() + " " + target.get_last_name()
        self.frame_name.set("Editing " + emp_name)
        title = ttk.Label(self,
                          textvariable=self.frame_name,
                          font=self.controller.title_font)
        title.grid(column=1, row=0, sticky=(N,S))
        
        #Set up labels/entries for all fields based on permission level
        View_Page.create_profile(self, user, target)
        View_Page.readonly(self, user, False)
        if user.is_admin() == True:
            self.id_entry.configure(state="readonly")
            self.status_entry.configure(state="readonly")
            self.start_entry.configure(state="readonly")
            self.end_entry.configure(state="readonly")
        
        #Set up Update and Cancel buttons
        self.sidebar.destroy()
        self.sidebar = ttk.Frame(self)
        self.sidebar.grid(column=0, row=0, sticky=(N,W,E,S), rowspan=6)
        update = ttk.Button(self.sidebar, text="Update Employee",
                              command=self.update_emp)
        update.grid(column=0, row=0, sticky=(N,W,E,S))
        cancel = ttk.Button(self.sidebar, text="Cancel",
                             command=lambda: self.controller.show_frame("View_Page"))
        cancel.grid(column=0, row=1, sticky=(N,W,E,S))
        user_manual = ttk.Button(self.sidebar, text="Help",
                                 command=lambda: self.controller.show_manual())
        user_manual.grid(column=0, row=2, sticky=(N,W,E,S))

        #Event bindings for each entry
        for entry in self.entry_list:
            entry.bind('<Return>', lambda e: self.update_emp())

        #Extra Formatting
        for child in self.sidebar.winfo_children():
            child.grid_configure(padx=5, pady=20)

    def update_emp(self):
        '''Updates the data of the specified employee'''
        #Validate info
        grid_num = 1
        valid = True
        updated_info = []
        for data in self.entry_data_list:
            if View_Page.validate_entry(self, data.get(), grid_num) == False:
                valid = False
            else:
                if data.get() == "Active":
                    updated_info.append(True)
                elif data.get() == "Deactivated":
                    updated_info.append(False)
                elif data == self.permission:
                    if data.get() == '1':
                        updated_info.append(True)
                    if data.get() == '2':
                        updated_info.append(False)
                else:
                    updated_info.append(data.get())
            grid_num += 1
        target = self.controller.target
        
        #Compare new vs old data fields and set every changed field if valid
        if valid == True:
            if target.get_id() != updated_info[0]:
                target.set_id(updated_info[0])
            if target.get_first_name() != updated_info[1]:
                target.set_first_name(updated_info[1])
            if target.get_last_name() != updated_info[2]:
                target.set_last_name(updated_info[2])
            if target.get_address() != updated_info[3]:
                target.set_address(updated_info[3])
            if target.get_city() != updated_info[4]:
                target.set_city(updated_info[4])
            if target.get_state() != updated_info[5]:
                target.set_state(updated_info[5])
            if target.get_zip() != updated_info[6]:
                target.set_zip(updated_info[6])
            if target.get_class() != updated_info[7]:
                if updated_info[7] == "1":
                    target.make_salaried(target.get_salary())
                elif updated_info[7] == "2":
                    target.make_commissioned(target.get_salary(), target.get_commission_rate())
                else:
                    target.make_hourly(target.get_hourly_rate())
            if target.get_hourly_rate() != updated_info[8]:
                target.set_hourly_rate(updated_info[8])
            if target.get_commission_rate() != updated_info[9]:
                target.set_commission_rate(updated_info[9])
            if target.get_salary() != updated_info[10]:
                target.set_salary(updated_info[10])
            if target.get_office_phone() != updated_info[11]:
                target.set_office_phone(updated_info[11])
            if target.get_office_email() != updated_info[12]:
                target.set_office_email(updated_info[12])
            if target.get_personal_phone() != updated_info[13]:
                target.set_personal_phone(updated_info[13])
            if target.get_personal_email() != updated_info[14]:
                target.set_personal_email(updated_info[14])
            if target.get_dob() != updated_info[15]:
                target.set_dob(updated_info[15])
            if target.get_ssn() != updated_info[16]:
                target.set_ssn(updated_info[16])
            if target.get_pay_method() != updated_info[17]:
                target.set_pay_method(updated_info[17])
            if target.get_routing() != updated_info[18]:
                target.set_routing(updated_info[18])
            if target.get_account() != updated_info[19]:
                target.set_account(updated_info[19])
            if target.is_admin() != updated_info[20]:
                target.make_admin(updated_info[20])
            if target.get_title() != updated_info[21]:
                target.set_title(updated_info[21])
            if target.get_dept() != updated_info[22]:
                target.set_dept(updated_info[22])
            if target.get_start() != updated_info[23]:
                target.set_start(updated_info[23])
            if target.get_end() != updated_info[24]:
                target.set_end(updated_info[24])
            if target.get_status() != updated_info[25]:
                target.set_status(updated_info[25])
            if target.get_password() != updated_info[26]:
                target.set_password(updated_info[26])
        
            # Update employee in DB
            self.controller.target.update_emp_in_db()

            #Return to view screen with updated employee
            self.controller.show_frame("View_Page")
        else:
            self.page_error.set("One or more entries invalid!")  




class Add_Page(View_Page):
    '''Class controlling the add employee page of the application'''
    def __init__(self, parent, controller):
        View_Page.__init__(self, parent, controller)
        self.controller = controller #root
        self.controller.grid_rowconfigure(0, weight=1)
        self.controller.grid_columnconfigure(0, weight=1)
        user = self.controller.user
        target = self.controller.target
        
        #Set up frame name
        self.frame_name = StringVar()
        self.frame_name.set("Add New Employee")
        title = ttk.Label(self,
                          textvariable=self.frame_name,
                          font=self.controller.title_font)
        title.grid(column=1, row=0, sticky=(N,S))

        #Set up labels/entries for all fields
        View_Page.create_profile(self, user, target)
        View_Page.empty_entries(self)

        #Create and automatically fill id, start, end, and status fields for ease of use
        if user.is_admin() == True:
            now = datetime.now()
            current_date = now.strftime("%m/%d/%Y")
            self.id.set(int(load_employees()[-1].get_id()) + 1) # Key off of last created id in DB
            self.emp_status.set("Active")
            self.start_date.set(current_date)
            self.end_date.set(None)
            self.id_entry.configure(state="readonly")
            self.status_entry.configure(state="readonly")
            self.start_entry.configure(state="readonly")
            self.end_entry.configure(state="readonly")

        #Set up Add and Cancel buttons
        self.sidebar.destroy()
        self.sidebar = ttk.Frame(self)
        self.sidebar.grid(column=0, row=0, sticky=(N,W,E,S), rowspan=6)
        add = ttk.Button(self.sidebar, text="Add Employee",
                              command=self.add_emp)
        add.grid(column=0, row=0, sticky=(N,W,E,S))
        cancel = ttk.Button(self.sidebar, text="Cancel",
                             command=lambda: self.controller.show_frame("View_Page"))
        cancel.grid(column=0, row=1, sticky=(N,W,E,S))
        user_manual = ttk.Button(self.sidebar, text="Help",
                                 command=lambda: self.controller.show_manual())
        user_manual.grid(column=0, row=2, sticky=(N,W,E,S))

        #Event bindings for each entry
        for entry in self.entry_list:
            entry.bind('<Return>', lambda e: self.add_emp())

        #Extra Formatting
        for child in self.sidebar.winfo_children():
            child.grid_configure(padx=5, pady=20)

    def add_emp(self):
        '''Creates new employee and adds them to database'''
        #Get and validate data from fields
        emp_info = []
        grid_num = 1
        valid = True
        for data in self.entry_data_list:
            if View_Page.validate_entry(self, data.get(), grid_num) == False:
                valid = False
            else:
                if data.get() == "Active":
                    emp_info.append(True)
                elif data.get() == "Deactivated":
                    emp_info.append(False)
                elif data == self.permission:
                    if data.get() == '1':
                       emp_info.append(True)
                    if data.get() == '2':
                        emp_info.append(False)
                else:
                    emp_info.append(data.get())
            grid_num +=1
                
        #If no empty/invalid fields, create new employee and add them to the database
        if "" in emp_info: #Empty field
            self.page_error.set("Missing required fields!")
        elif valid == False: #Invalid fields
            self.page_error.set("One or more entries invalid!")
        else:
            new_emp = Employee(emp_info[0], emp_info[1], emp_info[2], emp_info[3], emp_info[4],
                           emp_info[5], emp_info[6], emp_info[7], emp_info[17], emp_info[10],
                           emp_info[9], emp_info[8], emp_info[18], emp_info[19], emp_info[11],
                           emp_info[13], emp_info[12], emp_info[14], emp_info[15], emp_info[16],
                           emp_info[20], emp_info[21], emp_info[22], emp_info[23], emp_info[24],
                           emp_info[25], emp_info[26])
            self.controller.emp_dat[new_emp.get_id()] = new_emp
            self.controller.target = new_emp
            # Save Employee in the database
            new_emp.create_emp_in_db()
        
            #Return to view screen with new employee
            self.controller.show_frame("View_Page")




class Search_Page(ttk.Frame):
    '''Class controlling the search page of the application'''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller #root
        self.controller.grid_rowconfigure(0, weight=1)
        self.controller.grid_columnconfigure(0, weight=1)

        #Set up search dictionaries
        self.name_dict = {}
        self.classification_dict = {}
        self.title_dict = {}
        for emp in self.controller.emp_dat.values():
            name = emp.get_last_name()
            classification = emp.get_class()
            title = emp.get_title()

            #Adds employee data to search dictionaries
            if name not in self.name_dict.keys():
                self.name_dict[name] = []
            self.name_dict[name].append(emp)
            if classification not in self.classification_dict.keys():
                self.classification_dict[classification] = []
            self.classification_dict[classification].append(emp)
            if title not in self.title_dict.keys():
                self.title_dict[title] = []
            self.title_dict[title].append(emp)

        #Set up page name
        ttk.Label(self, text="Search Employee",
                  font=controller.title_font).grid(column=1, row=0,
                                                   sticky=(N,S), columnspan=3,
                                                   padx=5, pady=10)

        #Set up search parameter combobox/label
        ttk.Label(self, text="Search Parameters:").grid(column=1, row=1,
                                                        sticky=E, padx=5, pady=10)
        self.search_parameter = StringVar()
        parameters = ttk.Combobox(self, textvariable=self.search_parameter)
        parameters.grid(column=2, row=1,
                                                        sticky=(W, E))
        parameters['values'] = ('Last Name', 'ID', 'Classification', 'Title')
        
        #Set up search bar and button
        ttk.Label(self, text="Search").grid(column=1, row=2,
                                            sticky=E, padx=5, pady=10)
        self.search = StringVar()
        self.search_box = ttk.Entry(self, textvariable=self.search)
        self.search_box.grid(column=2, row=2, sticky=(W,E))
        self.search_box.bind('<KeyRelease>', self.check_key)
        self.search_box.bind('<FocusOut>', lambda e: self.hide_lb) #For some reason, this isn't working
        self.search_button = ttk.Button(self, text="Search", command=self.search_employees)
        self.search_button.grid(column=4, row=2, sticky=E, padx=5, pady=10)
        self.search_button.grid_remove()

        #Set up listbox and search list
        self.search_list = []
        self.lb = Listbox(self, height=5)
        self.lb.grid(column=2, row=3, sticky=(W, E))
        self.hide_lb()
        self.lb.bind('<<ListboxSelect>>', self.choose_from_lb)
        
        #Set up return and help buttons
        return_button = ttk.Button(self, text="Return",
                                   command=lambda: self.controller.show_frame("View_Page"))
        return_button.grid(column=0, row=0, sticky=E, padx=5, pady=10)
        help_button = ttk.Button(self, text="Help",
                                 command=lambda: self.controller.show_manual())
        help_button.grid(column=0, row=1, sticky=E, padx=5, pady=10)
        
        #Set up error message
        self.msg = StringVar()
        error_label = ttk.Label(self, textvariable = self.msg, style='Error.TLabel')
        self.msg.set('Please select an employee and then click "Search".')
        error_label.grid(column=2, row=4, sticky=(W,E), columnspan=2,
                         padx=5, pady=10)
        
#         #Extra Formatting
#         for child in self.winfo_children():
#             child.grid_configure(padx=5, pady=10)


    def search_employees(self, *args):
        '''Searches the database using the input value from the search box'''
        self.msg.set("")
        self.search.set("")
        self.controller.show_frame("View_Page")


    def change_search_list(self, data, search_value):
        '''Changes the search list'''
        #Clears search list
        self.search_list.clear()

        #Adds/removes employee entreies based on search parameter and value
        for entry in data:
            if (entry not in search_value) and (search_value not in entry):
                continue
            if isinstance(data[entry], List):
                for emp in data[entry]:
                    self.create_new_entry(emp)
            else:
                self.create_new_entry(data[entry])

        #clear error message, if any
        if self.msg != "":
            self.msg.set("")

        #Checks if search list is empty and displays message if true
        if not self.search_list:
            self.hide_lb()
            self.msg.set('Please select an employee and then click "Search".')

        #Return the new search list
        self.lb['height'] = len(self.search_list)
        return self.search_list


    def create_new_entry(self, emp):
        """Helper function for change_search_list which creates a new listbox entry"""
        #Initialize new entry
        emp_entry = ""

        #Obtain required employee information
        id = emp.get_id()
        lastname = emp.get_last_name()
        firstname = emp.get_first_name()
        title = emp.get_title()
        classification = emp.get_class()

        if not id or not firstname or not lastname or not title or not classification:
            return
            
        emp_entry += id + ", "
        emp_entry += lastname + ", "
        emp_entry += firstname + ", "
        emp_entry += title + ", "
        emp_entry += classification

        #Adds new employee entry to search list
        self.search_list.append(emp_entry)


    def update_lb(self, data):
        '''Updates the listbox with the new data'''
        if not data:
            return
        self.lb.delete(0, END)
        for item in data:
            self.lb.insert(END, item)


    def check_key(self, e):
        '''Checks search box as the user types and updates listbox accordingly'''
        value = e.widget.get()
        if value == "":
            self.msg.set('Please select an employee and then click "Search".')
            self.search_button.grid_remove()
            self.hide_lb()
            return

        #Determine current search dictionary
        if self.search_parameter.get() == "Last Name":
            current_search_dict = self.name_dict
        elif self.search_parameter.get() == "ID":
            current_search_dict = self.controller.emp_dat
        elif self.search_parameter.get() == "Title":
            current_search_dict = self.title_dict
        elif self.search_parameter.get() == "Classification":
            current_search_dict = self.classification_dict
        else:
            return #Returns from function if no search parameter is specified by user
        
        #Create new search list and update the listbox
        new_search_list = self.change_search_list(current_search_dict, value)
        self.update_lb(new_search_list)
        self.show_lb()

        #Hide listbox if empty
        if not self.search_list:
            self.lb.grid_remove()


    def choose_from_lb(self, e):
        '''Updates the search box with the choice from the listbox'''
        index = e.widget.curselection()
        choice = self.lb.get(index)            

        #Sets the search box value and the controller target to the selected employee
        self.search.set(choice)
        self.hide_lb()
        self.controller.target = self.controller.emp_dat[choice[0]]
        
        #Allows user to search for selected employee's information
        self.search_button.grid()


    def show_lb(self):
        '''Shows the listbox upon entry focus'''
        self.lb.grid()


    def hide_lb(self):
        '''Hides listbox once out of focus'''
        self.lb.grid_remove()


class Pay_Page(ttk.Frame):
    '''Class controlling the payroll page of the application'''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.grid_rowconfigure(0, weight=1)
        self.controller.grid_columnconfigure(0, weight=1)

        # Get the current employees loaded for payroll
        load_employees()

        
        #Set up frame title
        ttk.Label(self, text="Payroll", font=controller.title_font).grid(column=1, row=0, sticky=(N,S), columnspan=4)

        #Set up receipt, timecard, and payroll buttons
        receipt_button = ttk.Button(self, text="Process Receipts",
                                 command= self.receipts)
        receipt_button.grid(column=2, row=1, sticky=(N,W,E,S))
        timecard_button = ttk.Button(self, text="Process Timecards",
                                 command= self.timecards)
        timecard_button.grid(column=3, row=1, sticky=(N,W,E,S))
        payroll_button = ttk.Button(self, text="Run Payroll",
                                    command=lambda: run_payroll())
        payroll_button.grid(column=4, row=1, sticky=(N,W,E,S))

        #Set up add receipt and add timecard buttons
        self.add_r_button = ttk.Button(self, text="Add Individual Receipts",
                                  command=lambda: self.create_add_frame(1))
        self.add_r_button.grid(column=2, row=2, sticky=(N,W,E,S))
        self.add_t_button = ttk.Button(self, text="Add Individual Timecards",
                                  command=lambda: self.create_add_frame(2))
        self.add_t_button.grid(column=3, row=2, sticky=(N,W,E,S))

        #Set up error label
        self.file_error = StringVar()
        ttk.Label(self, textvariable=self.file_error,
                  style='Error.TLabel').grid(column=1, row=4, sticky=(N,S), columnspan=4)
        
        #Set up menu buttons
        back_button = ttk.Button(self, text="Return",
                                 command=lambda:self.controller.show_frame("View_Page"))
        back_button.grid(column=0, row=0, sticky=(N,W,E,S))
        help_button = ttk.Button(self, text="Help",
                                 command=lambda: self.controller.show_manual())
        help_button.grid(column=0, row=1, sticky=(N,W,E,S))

        #Extra Formatting
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=10)

    def receipts(self):
        '''Processes the reciepts.csv file'''
        try:
            process_receipts()
        except FileNotFoundError:
            self.file_error.set("'receipts.csv' file not found")

    def timecards(self):
        '''Processes the timecards.csv file'''
        try:
            process_timecards()
        except FileNotFoundError:
            self.file_error.set("'timecards.csv' file not found")

    def create_add_frame(self, mode):
        '''Creates a specific frame with widgets for adding either receipts or timecards'''
        #Disable add buttons to prevent stacking frames
        self.add_r_button.grid_remove()
        self.add_t_button.grid_remove()
        #Create frame for adding
        self.add_frame = ttk.Frame(self)
        self.add_frame.grid(column=1, row=3, columnspan=3)

        #Create labels/entries
        if mode == 1: #Receipt mode
            ttk.Label(self.add_frame, text="Adding Receipts").grid(column=0, row=0, columnspan=4)
        else: #Timecard mode
            ttk.Label(self.add_frame, text="Adding Timecards").grid(column=0, row=0, columnspan=4)
        ttk.Label(self.add_frame, text="Employee ID:").grid(column=0, row=1)
        ttk.Label(self.add_frame, text="Amount:").grid(column=2, row=1)
        self.emp_to_add = StringVar()
        id_to_add = ttk.Entry(self.add_frame, textvariable=self.emp_to_add)
        id_to_add.grid(column=1, row=1)
        self.amount = StringVar()
        amt_to_add = ttk.Entry(self.add_frame, textvariable=self.amount)
        amt_to_add.grid(column=3, row=1)

        #Create add and finish buttons
        add_btn = ttk.Button(self.add_frame, text="Add",
                             command=lambda: self.add_item(mode))
        add_btn.grid(column=3, row=2, sticky=E)
        done_btn = ttk.Button(self.add_frame, text="Done",
                              command=lambda: self.finish_adding())
        done_btn.grid(column=3, row=3, sticky=E)

        #Create key binding for add button
        id_to_add.bind('<Return>', lambda e: self.add_item(mode))
        amt_to_add.bind('<Return>', lambda e: self.add_item(mode))

        #Create error label
        self.add_error_msg = StringVar()
        add_error = ttk.Label(self.add_frame, textvariable=self.add_error_msg,
                              style='Error.TLabel')
        add_error.grid(column=0, row=4, columnspan=4)

        #Extra Formatting
        for child in self.add_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def add_item(self, mode):
        '''Adds the receipt or timecard amount to the specified employee'''
        if self.emp_to_add.get() not in self.controller.emp_dat.keys(): #Invalid ID
            self.add_error_msg.set("Invalid Employee ID!")
        else:
            emp = self.controller.emp_dat[self.emp_to_add.get()]
            clas = emp.get_classification()
            try: #Ensure correct value
                float(self.amount.get())
                if mode == 1: #receipt mode
                    if str(clas) == "Commissioned Employee": #has correct classification
                        clas.add_receipt(self.amount.get())

                        # Save amount of receipt to emp in timecard DB
                        create_employee_receipt(emp, int(self.amount.get()))

                        self.amount.set("")
                        self.add_error_msg.set("")
                        # print("Added receipt")
                    else:
                        self.add_error_msg.set("Specified Employee has incorrect classification!")
                elif mode == 2: #timecard mode
                    if str(clas) == "Hourly Employee": #has correct classification
                        clas.add_timecard(self.amount.get())

                        # Save time to emp in timecard DB
                        create_employee_timecard(emp, int(self.amount.get()))

                        self.amount.set("")
                        self.add_error_msg.set("")
                        # print("Added timecard")
                    else:
                        self.add_error_msg.set("Specified Employee has incorrect classification!")
                    
            except ValueError: 
                self.add_error_msg.set("Amount must enter either a number or a decimal!")

    def finish_adding(self):
        '''Destroys the add_frame widget and returns the pay page back to normal'''
        #Destroy add frame
        self.add_frame.destroy()
        
        #Reenable buttons
        self.add_r_button.grid()
        self.add_t_button.grid()

if __name__ == "__main__":
    emps = get_db("database/employees.json")
    emp_dict = {}

    for emp in emps:
        emp_dict[str(emp["id"])] = Employee(str(emp["id"]), emp["first_name"], emp["last_name"], emp["address"], emp["city"],
                                       emp["state"] ,emp["zip"], emp["classification"], emp["pay_method"], emp["salary"],
                                       emp["commission"], emp["hourly"], emp["routing_num"], emp["account_num"], 
                                       emp["office_phone"], emp["personal_phone"], emp["office_email"], emp["personal_email"],
                                       emp["dob"], emp["ssn"], emp["admin"], emp["title"], emp["dept"], emp["start"],
                                       emp["end"], emp["status"], emp["password"])

    app = EmpApp(emp_dict)
    app.mainloop()