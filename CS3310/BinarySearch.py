import math

""" 
    Please implement functions named:  reset, basicOps, binarySearch, and avgBasicOpsFullTree; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your 
    favorite Python IDE.

"""


count = 0

""" reset, resets basic op counter to 0 """
def reset():
    global count
    count = 0

""" basicOps returns the number of basic operations """
def basicOps():
    return count

""" 
    binarySearch, implement a recursive binary search of a list of items for the value x.  
    The list of items is sorted in non-decreasing order.  For this function only, 
    x may or may not be in the binary tree.
"""
def binarySearch(items, left, right, x):
    # If x is in items, return the 0-based index occurance of x; otherwise return -1
    # for basic operations, put a counter and increment it every time the basic operation occurs
    # n is the number of items
    #
    # 
    # Note: the unit tests will set the initial search parameters to:  left = 0 and right = n - 1 (n is the # of items being searched)
    # and then invoke binarySearch with the following parameters:
    #     items, the sorted list of items to use for the binary search
    #     left, left index
    #     right, right index
    #     x, item being searched for
    #     
    # binary search algorithm:
    #     terminal condition is when left > right (when implemented properly, if left > right implies x is not in items)
    #
    #     m (middle elemen)  equals the floor of (left + right)/2, hint the integer division operator in Python is // 
    #
    #     if items[m] equals x, then return m
    #     otherwise, if items[m] < x then return binarySearch(items, m + 1, right, x)
    #     /* the only remaining option is items[m] > x */
    #     otherwise, return binarySearch(items, left, m - 1, x)
    global count

    mid = (left + right) // 2
    if left > right:
        return -1
    else:
        count += 1


    if items[mid] == x:
        return mid
    elif items[mid] < x:
        return binarySearch(items, mid + 1, right, x)
    else:
        return binarySearch(items, left, mid -1, x)

""" 
    avgBasicOpsFullTree, for a binary tree of size n, this function 
    returns the average number of basic operations as a double

    For calculation of expected average number of basic operations, assume:
        1.  each integer value contained in the binary tree is only allowed once
        2.  for this function only, assume that the valued being searched (x) for is in the binary tree
        3.  n = 2^k - 1, because it is a full binary tree (of k levels)
"""
def avgBasicOpsFullTree(n):
    if n == 0:
        return 0
    rows = int(math.log2(n+1))
    sum = 0
    for i in range(1, rows+1):
        sum += (2**(i-1))*i
    average = sum / n
    return average



