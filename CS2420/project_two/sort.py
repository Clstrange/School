
import random
import time


def selection_sort(lyst_two):
    """testing"""
    lyst_size = len(lyst_two) - 1
    largest_num = lyst_two[0]
    for length in range(len(lyst_two)): 
        largest_num = lyst_two[0]
        for item in range(lyst_size):
            item = lyst_two[item]
            if item > largest_num:
                largest_num = item
        lyst_two[lyst_size], lyst_two[lyst_two.index(largest_num)] = lyst_two[lyst_two.index(largest_num)], lyst_two[lyst_size]
        lyst_size = lyst_size - 1

def insertion_sort(lyst):
    """testing"""
    new_lyst = [lyst.pop(0)]
    for number in lyst: 
        test = False
        for value in new_lyst:
            if number < value:
                test = False
                break
            if number > value:
                test = True
        if test == True:
            new_lyst.append(number)
        else: 
            
            new_lyst.insert(new_lyst.index(value), number)
def mergesort(lyst_three):
    """testing"""

    if len(lyst_three) > 1:
        left = lyst_three[:len(lyst_three)//2]
        right = lyst_three[len(lyst_three)//2:]
        mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lyst_three[k] = left[i]
                i += 1
            else:
               
                lyst_three[k] = right[j]
                j = j + 1
            k += 1
        while i < len(left):
            lyst_three[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lyst_three[k] = right[j]
            j += 1
            k += 1

def quicksort(lyst_four):
    quicksorthelper(lyst_four, 0, len(lyst_four) - 1)

def quicksorthelper(lyst_four, left, right):
    if left < right:
        partition_pos = partition(lyst_four, left,  right)
        quicksorthelper(lyst_four, left, partition_pos - 1)
        quicksorthelper(lyst_four, partition_pos + 1, right)

def partition(lyst_four, left, right):
    i = left
    j = right - 1
    pivot = lyst_four[right]
    while i < j:
        while i < right and lyst_four[i] < pivot:
            i += 1
        while j > left and lyst_four[j] >= pivot:
            j -= 1
        if i < j:
            lyst_four[i], lyst_four[j] = lyst_four[j], lyst_four[i]
    if lyst_four[i] > pivot:
        lyst_four[i], lyst_four[right] = lyst_four[right], lyst_four[i]
    return i

def timsort (lyst_five):
    lyst_five.sort()

def is_sorted(lyst_six):
    if lyst_six == lyst_six:
        return True
    else: return False
