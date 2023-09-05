"""
    Please implement functions named:  reset, basicOps, and linearSearch, avgBasicOpsMaybeInSet, and
                                       avgBasicOpsInSet; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.

"""
count = 0

""" basicOps returns the number of basic operations """
def basicOps():
    return count
    
""" reset, resets basic op counter to 0 """
def reset():
    global count
    count = 0


""" 
    linearSearch, implement linear search of items for the value x.  
    1.  Return the index of the first occurence of x in the list
    2.  Otherwise, if it's not in the list return -1

"""
def linearSearch(items, x):
    global count
    for item in items:
        count += 1
        if item == x:
            return items.index(x)
    return -1

""" 
    avgBasicOpsInSet, for a set of size n, returns the expected average number of basic operations as a double 

    For calculation of expected average number of basic operations assume:
        1.  the number of items in the set (n) is 0 < n <= 256
        2.  the values in the set of items are unsigned bytes (aka the values are in the range of 0-255)
        3.  items is a set, therefore a value is only allowed once
        4.  sets are unordered
        5.  the item being searched for, x, is (somewhere) in the set
        6.  the distribution of x is uniform on the list (each possible value in the set, 
            the list of items, has the same probablity)
        7.  set size (n) is a positive number (it won't be zero)
"""
def avgBasicOpsInSet(n):
    return (n+1)/2


""" 
    avgBasicOpsMaybeInSet, for a set of size n, returns the expected average number of basic operations as a double 

    For calculation of expected average number of basic operations assume:
        1.  the number of items in the set (n) is 0 <= n <= 256
        2.  the values in the set of items are unsigned bytes (aka the values are in the range of 0-255)
        3.  items is a set, therefore a value is only allowed once
        4.  sets are unordered
        5.  the item being searched for, x, might (or might not) be in the set
        6.  the distribution of x is uniform over the range of an unsigned byte
        7.  set size might be 0
"""
def avgBasicOpsMaybeInSet(n):
    sum_of_x = 0
    for i in range(n):
        sum_of_x += i
    maximum = (256 - n+1) * n
    average_ops = (sum_of_x + maximum)/256
    return average_ops

print(avgBasicOpsMaybeInSet(4))