
result = 1
base = 7
exponent = 40
mod = 2399

while(exponent > 0):
    if(exponent % 2 == 1):
        result = result * base % mod
    base = base * base % mod
    exponent = exponent // 2
print(result)