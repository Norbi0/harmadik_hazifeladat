a = int(input("Adja meg a sorozat első értékét (egész érték az [1,100] intervallumból): "))
n = int(input("Adja meg a sorozat n-edik értékét (egész érték az [1,50] intervallumból): "))
q = int(input("Adja meg a sorozat kvóciensét (egész érték az [1,10] intervallumból): "))
def geometric_sequence_element(a, n, q):
    if 1 <= a <= 100 and 1 <= n <= 50 and 1 <= q <= 10:
        nedik = a * (q ** (n - 1))
        return nedik
    else:
        return "Hiba."
print(geometric_sequence_element(a, n, q))
