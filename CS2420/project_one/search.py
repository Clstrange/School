""" this is a summmary of my project """

import random
import time
from math import sqrt

def linear_search(lyst, target):
    """ description of function """
    for i in lyst:
        if i == target:
            return
    return

def binary_search(lyst, target):
    """ description of function """
    
    search_lyst = round(len(lyst) / 2)
    binary_test = lyst[search_lyst - 1]
    hate = round(search_lyst * 1.5)

    for i in lyst:
        if target == binary_test:
            break
        else:
            if target > binary_test:
                search_lyst = hate
            else:
                search_lyst = round((search_lyst / 2) - 0.1)
    return

def jump_search(lyst, target):
    """ description of function """
    search_lyst = 0
    jump_by = round(search_lyst - sqrt(len(lyst)) - 0.1)
    for i in lyst:
        if target == search_lyst:
            return
        elif search_lyst > target:
            search_lyst = jump_by
            for i in range(jump_by):
                if lyst[i] == target:
                    return
        else:
            search_lyst = jump_by
            
    return


def main():
    """ description of function """
    lyst = []

    for list_size in range(100000000):
        lyst.append(random.randrange(1,100))

    lyst = sorted(lyst)
    start_0 = time.perf_counter()

    linear_search(lyst, 1)
    start_1 = time.perf_counter()
    print(start_1 - start_0)

    linear_search(lyst, 50)
    start_2 = time.perf_counter()
    print(start_2 - start_1)

    linear_search(lyst, 100)
    start_3 = time.perf_counter()
    print(start_3 - start_2)

    linear_search(lyst, 0)
    start_4 = time.perf_counter()
    print(start_4 - start_3)

    binary_search(lyst, 1)
    start_5 = time.perf_counter()
    print(start_5 - start_4)

    binary_search(lyst, 50)
    start_6 = time.perf_counter()
    print(start_6 - start_5)

    binary_search(lyst, 100)
    start_7 = time.perf_counter()
    print(start_7 - start_6)

    binary_search(lyst, 0)
    start_8 = time.perf_counter()
    print(start_8 - start_7)
    
    jump_search(lyst, 1)
    start_9 = time.perf_counter()
    print(start_9 - start_8)

    jump_search(lyst, 50)
    start_10 = time.perf_counter()
    print(start_10 - start_9)

    jump_search(lyst, 100)
    start_11 = time.perf_counter()
    print(start_11 - start_10)

    jump_search(lyst, 0)
    start_12 = time.perf_counter()
    print(start_12 - start_11)

    if __name__ == "name":
        main()

main()
