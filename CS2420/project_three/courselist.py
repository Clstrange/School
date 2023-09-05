"""
This module takes nodes from 'Course' and create a linkedlst 'Courselist'

Classes: CourseList
"""

from course import Course

class CourseList:
    """CourseList Class holds nodes taken in from the Course Class.
    Methods:
        __init()__
        insert()
        remove()
        remove_all()
        find()
        size()
        calculate_gpa()
        is_sorted()
        __str__()
        __iter__
        __next__
     """

    def __init__(self):
        """CourseList Class Constructor"""
        self.head = None

    def insert(self, course_test):
        """Insert a new Course node in asecending order"""
        if self.head is None:
            self.head = course_test
        elif(course_test.number() <= self.head.number()):
            course_test.link = self.head
            self.head = course_test

        else:
            p_pointer = self.head
            c_pointer = p_pointer.link
            t_pointer = course_test
            while c_pointer is not None and t_pointer.link is None:
                if (t_pointer.number() >= p_pointer.number()
                    and t_pointer.number() <= c_pointer.number()):

                    p_pointer.link = t_pointer
                    t_pointer.link = c_pointer
                else:
                    p_pointer = c_pointer
                    c_pointer = c_pointer.link
            if c_pointer is None:
                p_pointer.link = t_pointer

    def remove(self, number):
        """Remove the first instance of a Course node based on its number"""
        if self.head.number() == number:
            c_pointer = self.head
            self.head = c_pointer.link
            c_pointer.link = None
        else:
            c_pointer = self.head
            p_pointer = None
            while c_pointer.link is not None and c_pointer.number() is not number:
                p_pointer = c_pointer
                c_pointer = p_pointer.link
            p_pointer.link = c_pointer.link
            c_pointer.link = None

    def remove_all(self, number):
        """Recursivly remove all instances of a Course node based on its number"""
        c_pointer = self.head
        p_pointer = None
        contingency = self.head
        if c_pointer is None:
            return
        if self.head.number() == number:
            self.head = c_pointer.link
            c_pointer.link = None
        else:
            p_pointer = c_pointer
            c_pointer = p_pointer.link
            if c_pointer is None:
                return
            if c_pointer.number() == number:
                p_pointer.link = c_pointer.link
                c_pointer.link = None
            else:
                self.head = c_pointer
        self.remove_all(number)
        self.head = contingency
        return

    def find(self, number):
        """find a Course node based on its number"""
        if self.head is None:
            return -1
        c_pointer = self.head
        p_pointer = None
        while c_pointer is not None and c_pointer.number() is not number:
            p_pointer = c_pointer
            c_pointer = p_pointer.link
        if c_pointer is None:
            return -1
        return c_pointer

    def size(self):
        """Return size of linkedlist"""
        c_pointer = self.head
        p_pointer = None
        list_size = 0
        while c_pointer is not None:
            p_pointer = c_pointer
            c_pointer = p_pointer.link
            list_size += 1
        return list_size

    def calculate_gpa(self):
        """Return average GPA of all courses"""
        c_pointer = self.head
        p_pointer = None
        total_credits = 0
        total_grade_points = 0
        while c_pointer is not None:
            credit = c_pointer.credit_hr()
            total_credits += credit
            gpa = c_pointer.grade()
            total_grade_points += gpa * credit
            p_pointer = c_pointer
            c_pointer = p_pointer.link
        if total_grade_points == 0:
            return 0
        cumulative_gpa = total_grade_points / total_credits
        return cumulative_gpa

    def is_sorted(self):
        """Tests to see if linked list is sorted"""
        c_pointer = self.head
        p_pointer = c_pointer
        while c_pointer is not None:
            if p_pointer.number() > c_pointer.number():
                return False
            p_pointer = c_pointer
            c_pointer = p_pointer.link
        return True

    def __str__(self):
        """Returns string of all courses and their information"""
        if self.head is None:
            return
        c_pointer = self.head
        p_pointer = None
        course_data = ("cs" + str(c_pointer.number()) + " " +  str(c_pointer.name()) + " Grade:"
        + str(c_pointer.grade()) + " Credit Hours: " + str(c_pointer.credit_hr()) + "\n")
        while c_pointer.link is not None:
            p_pointer = c_pointer
            c_pointer = p_pointer.link
            course_data += ("cs" + str(c_pointer.number())
            + " " +  str(c_pointer.name()) + " Grade:"
            + str(c_pointer.grade()) + " Credit Hours: " + str(c_pointer.credit_hr()) + "\n")
        return course_data

    def __iter__(self):
        """Makes the linkedlist iterable"""
        self.c_pointer = self.head
        self.p_pointer = None
        return self

    def __next__(self):
        """Makes the linkedlist iterable"""
        self.p_pointer = self.c_pointer
        if self.p_pointer is None:
            raise StopIteration
        self.c_pointer = self.c_pointer.link
        return self.p_pointer
