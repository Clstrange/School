
import sys
from time import perf_counter

#Command line arguments
arg = sys.argv
function_calls = []
cache = {}
cache_hits = []

def weight(r, c):
    function_calls.append(1)
    #Base cases
    if (r, c) in cache:
        cache_hits.append(1)
        return cache.get(r, c)
    else:
        if r < 0:            
            return 0
        if c < 0 or c > r:   
            return 0
        else:
            
            total = 200 + weight(r - 1, c)/2 + weight(r - 1, c - 1) / 2
            cache[r, c] = total
            return total
            
        
        
def recursion(pyramid_size):
    column = pyramid_size
    pyramid_weights = []
    if pyramid_size < 0:
        print("Elapsed time:", perf_counter(), "seconds")
        print("Number of functions calls: ",sum(function_calls))
        print("Number of cache hits: ", sum(cache_hits))
    else:
        while column >= 0:
            pyramid_weights.append(format(weight(pyramid_size, column) - 200,'.2f'))
            column -= 1
        print(pyramid_weights)
        recursion(pyramid_size-1)

recursion(float(sys.argv[1]))



