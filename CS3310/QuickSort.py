# I declare that the following source code was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
# I declare that the following source code was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

"""
    Please implement functions named:  reset, basicOps, quickSort, partition, bestBasicOps, and worstBasicOps; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.

"""


from math import log2


count = 0

""" basicOps returns the number of basic operations """
def basicOps():
    return count
    
""" reset, resets basic op counter to 0 """
def reset():
    global count
    count = 0


""" 
    quickSort, implement quickSort
"""
def quickSort(arr):
    global count
    if len(arr) <= 1:
        return arr

    # Use a stack to keep track of sublists to sort
    stack = [(0, len(arr) - 1)]
    while stack:
        # Pop the next sublist to sort from the stack
        start, end = stack.pop()

        if end - start < 1:
            # Base case: sublist has 0 or 1 elements
            continue

        # Choose the pivot and partition the sublist
        pivot = arr[start]
        left = start + 1
        right = end
        while left <= right:
            while left <= right and arr[left] <= pivot:
                count += 1
                left += 1
            while left <= right and arr[right] > pivot:
                count += 1
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[start], arr[right] = arr[right], arr[start]

        # Push the two new sublists onto the stack
        if right - 1 - start >= end - right - 1:
            stack.append((start, right - 1))
            stack.append((right + 1, end))
        else:
            stack.append((right + 1, end))
            stack.append((start, right - 1))

    return arr



""" 
    bestBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function 
    returns b(n), aka the best case or minimal number of key comparisons, as a double

    best case of quick sort only does n - 1 key comparisons but splits the items equally around pivot

    therefore, for bestBasicOps, assume that the recurrence relation is:
        b(1) = 0
        b(n) = 2*b(n/2) + n - 1 
    Hint: starting with given b(1), calculate b(2), b(4), etc. until you find a pattern.
    Using the pattern, find a closed form solution.  Then use induction to prove it's true.
    Finally implement here the correct, proven, best-case candidate (closed form) solution.
"""
def bestBasicOps(n):
    # best quickSort == worst mergeSort
    return (2**log2(n))*(log2(n)-1)+1


""" 
    worstBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function 
    returns w(n), aka the worst case or maximum number of key comparisons, as a double

    worst case of quick sort does n-1 key comparisons because there's no need to compare the last element to itself

    therefore, for worstBasicOps, assume that the recurrence relation is:
        w(1) = 0
        w(n) = w(n-1) + n - 1 

    Hint: starting with given w(1), calculate w(2), w(4), etc. until you find a pattern.
    from this pattern, find a closed form solution.  Then use induction to prove it's true.
    Finally, implement here the correct, proven, worst-case candidate (closed form) solution.

"""
def worstBasicOps(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum
