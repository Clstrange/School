def rsa(p, q):
    n = p*q
    o = (p-1) * (q-1)
    e = co_prime(o)
    private_key = find_d(e,o)
    public_key = (e,n)
    return (private_key, public_key)

def find_d(e,o):
    d = 0
    while ((e*d) % o) != 1:
        d += 1
    return d

def co_prime(o):
    for i in range(o-1, 1, -1):
        if gcd(o, i) == 1:
            return i
    print("co_prime ERROR")

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def main():
    p = 13
    q = 3
    print(rsa(p,q))
if __name__ ==  "__main__":
    main()