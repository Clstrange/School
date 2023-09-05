def EEA(x,y):
    a, b = max(x, y), min(x, y)
    T1, T2 = 0, 1
    while True:
        if b == 0:
            return T1
        Q,R = divmod(a,b)
        T = T1 - (T2*Q)
        a = b
        b = R
        T1 = T2
        T2 = T

print(EEA(5,21))
