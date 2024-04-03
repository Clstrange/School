"""
Last updated:
    Cody Strange
    3/3/2022
    
Various pieces of field validation code that needs
to be implemented at specific parts of emp_dat_v3
"""

def field_validation(value, data_type):
    '''checks that the value passed into the function matches
    the data type that the user specifies'''
    if data_type == "int":
        assert(int(value))
    elif data_type == "str":
        assert(str(value))



