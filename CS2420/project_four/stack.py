"""
This module creates the 'Stack' data structure

Classes: Stack
"""
class Stack:
    """Stack Class is a restricted list that only allows
    the user to add and remove from the 'top' of the list
    Mathods:
        __init()__
        push()
        pop()
        top()
        size()
        clear()
    """
    def __init__(self):
        """Stack Class Constructor"""
        self.lyst = []

    def push(self, item):
        """Add an item to the top of the stack"""
        self.lyst.append(item)

    def pop(self):
        """Removes the top item of the stack and returns its value"""
        if self.lyst is None:
            raise IndexError
        return self.lyst.pop()

    def top(self):
        """Returns the value of the top item of the stack"""
        if self.lyst is None:
            raise IndexError
        return self.lyst[len(self.lyst) - 1]

    def size(self):
        """Returns the number of items in the stack"""
        return len(self.lyst)

    def clear(self):
        """Clears the stack"""
        self.lyst = []
