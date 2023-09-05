import math

def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def exponent(x):
    if math.isnan(x):
        return 1024
    elif x * 1e-1 == 0:
        return -1022
    else:
        x = int(x) # remove the decimal from the number
        x = bin(x).replace("0b", "") # convert the integer to binary
        return int(len(x)) - 1

def fraction(x):
    if x == 0:
        return 0
    dec_x = x - int(x)
    # creates a binary string of the fraction portion
    bin_decimal = ""
    while dec_x != 1:
        dec_x *= 2
        if dec_x > 1:
            bin_decimal += "1"
            dec_x -= int(dec_x)
        elif dec_x < 1:
            bin_decimal += "0"
    bin_decimal += "1"

    # creates a binary string of the integer portion
    int_x = bin(int(x)).replace("0b", "")
    total_x = int_x + bin_decimal
    total_x = total_x[1:] # ignore the first 1

    # combine the integer portion and decimal portion
    while(total_x[0] == '0'):
        total_x = total_x[1:]

    # reverse the order of the string so that it can be turned back to a decimal
    binary_string = total_x[::-1]

    # convert the binary string back to decimal
    decimal = 0
    for bit in binary_string:
        decimal = .5 * (int(bit) + decimal)
    return decimal

def mantissa(x):
    if x == 0:
        return 0
    return 1 + fraction(x)

def is_posinfinity(x):
    if x == math.inf():
        return True
    else:
        return False

def is_neginfinity(x):
    if x == -math.inf():
        return True
    else:
        return False
    
def fractionToBinary(num):
    total = "."
    while num != 1:
        num *= 2
        if num > 1:
            total += "1"
            num -= int(num)
        elif num < 1:
            total += "0"
    total += "1"
    return total

def ulp(x):
    if x * 1e-1 == 0:
        return 5e-234
    return 2**(-52+math.floor(math.log2(x)))

def ulps(x, y):

    e = math.floor(math.log2(x))
    if math.floor(math.log2(x)) == (math.floor(math.log2(y)-1)):
        interval_count = (y - x) / 2**-52+e
    else:
        lower_upper_bound = math.floor(math.log(x)) + 1
        upper_lower_bound = math.floor(math.log(y))
        x_section = (lower_upper_bound -x) / (2**(-52 + e))
        y_section = (y - upper_lower_bound) / (2**(-52+e))
        middle_section = ((math.floor(math.log(y)) - math.floor(math.log(x))) * (2**52)) + 1
        interval_count = x_section + y_section + middle_section
    return interval_count

subMin = 5e-324
y = 6.5