from math import log10,ceil
import time

def karatsuba_algoritm(x,y):
    if x < 10 or y < 10:
        return x*y

    n = max(int(log10(x)+1) , int(log10(y)+1))
    n_2 = int(ceil(n/2.0))

    if n % 2 == 1:
        n +=1

    a,b = divmod(x, 10**n_2)
    c,d = divmod(y, 10**n_2)

    ac = karatsuba_algoritm(a,c)
    bd = karatsuba_algoritm(b,d)

    ad_bc = karatsuba_algoritm((a+b) , (c+d)) - ac - bd
    return (((10**n)*ac) + bd + ((10**n_2) * (ad_bc)))

def standard_algorithm(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    str_num1 = str_num1[::-1]
    str_num2 = str_num2[::-1]
    
    result = 0
    
    for i in range(len(str_num1)):
        carry = 0
        
        for j in range(len(str_num2)):

            prod = int(str_num1[i]) * int(str_num2[j]) + carry
            

            if i+j == 0:
                result = prod

            else:
                prev_result = (result // 10**(i+j)) % 10
                result -= prev_result * 10**(i+j)
                result += (prev_result + prod % 10) * 10**(i+j)
                carry = prod // 10
        
        if carry > 0:
            result += carry * 10**(i+len(str_num2))
    
    return result



x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

start = time.perf_counter()
result = standard_algorithm(x,y)
end = time.perf_counter()
standard_time = end - start
print(f"Standard: {standard_time} seconds")

start = time.perf_counter()
result = karatsuba_algoritm(x,y)
end = time.perf_counter()
karatsuba_time = end - start
print(f"Karatsuba: {karatsuba_time} seconds")

difference = standard_time-karatsuba_time
print(f"Karatsuba algorithm is faster by: {difference} seconds")

print(x*y)