import sys
from time import perf_counter

def weight_on(column, row):
    """returns the weight on the back of the person in 
    row rand and column c, top pos = (0,0)"""
    if row == 0:
        return 0

    elif column == 0:
        return (weight_on(column, row - 1) + 200) / 2

    elif row == column:
        return (weight_on(column - 1, row - 1) + 200) / 2

    else:
        return (200 + weight_on(column - 1, row - 1)) / 2 + (200 + weight_on(column, row - 1)) / 2


def main():
    t1_start = perf_counter()
    for row in range(int(sys.argv[1]) - 1):
        column = 0
        row += 1

        while column <= row:
            print("{:.2f}".format(weight_on(column, row)), end = ' ')
            column += 1
        print('')
    t1_stop = perf_counter()

    print("Elapsed time:", t1_stop-t1_start)
        

if __name__ == "__main__":
    main()

