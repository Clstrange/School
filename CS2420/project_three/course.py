"""
This module creates nodes for the linked list 'CourseList'

Classes:
        Course

"""

class Course:
    """Course Class holds data about individual classes.

    Methods:
        __init__(course_number = 0, course_name = "",
                course_credit_hr = 0.0, course_grade = 0.0)
        number()
        name()
        credit_hr()
        grade()
        __str__()
    """

    def __init__(self, course_number = 0, course_name = "",
                course_credit_hr = 0.0, course_grade = 0.0):
        """Course Class Constructor to initialize the object.

        Input Arguments: course_number must be int, course_name must be str,
                        course_credit_hr must be float, course_grade must be float.
        """
        if not isinstance(course_number, int) or course_number < 0:
            raise ValueError
        self.course_number = course_number
        self.link = None

        if not isinstance(course_name, str):
            raise ValueError
        self.course_name = course_name

        if not isinstance(course_credit_hr, float) or course_credit_hr < 0:
            raise ValueError
        self.course_credit_hr = course_credit_hr

        if not isinstance(course_grade, float) or course_grade < 0:
            raise ValueError
        self.course_grade = course_grade

    def number(self):
        """returns number pf course"""
        return self.course_number

    def name(self):
        """returns name of course"""
        return self.course_name

    def credit_hr(self):
        """returns number of credit hours the course is"""
        return self.course_credit_hr

    def grade(self):
        """returns grade obatained for course"""
        return self.course_grade

    def __str__(self):
        """returns string of all courses taken"""
        str_number = str(self.course_number)
        str_name = self.course_name
        str_credit_hr = str(self.course_credit_hr)
        str_grade = str(self.course_grade)

        str_course = str_number + "," + str_name + "," + str_credit_hr + "," + str_grade
        return str_course
