def gcd(a, b):
    if 1 <= a <= 100 and 1 <= b <= 100:
        if a == b:
            return a
        if b < a:
            a, b = b, a
        while (0 < a):
            a, b = b % a, a
        return b
    else:
        break
a = 1
b = 1
while a != 0 and b != 0:
    a = int(input("Adjon meg egy számot az [1,100] intervallumból: "))
    b = int(input("Adjon meg egy számot az [1,100] intervallumból: "))
    print(gcd(a, b))


