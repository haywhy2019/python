"""lecture 3 python files"""
# python3 -i lecture3.py
def prime_factors(n):
    while n > 1:
        k = smallest_prime_factor(n)
        n = n//k
        print(k)

def smallest_prime_factor(n):
    k = 2
    while n % k != 0:
        k = k + 1
    return k

i, total= 0,0
while i < 3:
    i = i + 1
    total = total + i


from operator import floordiv, mod

def divide_exact(n,d):
    return floordiv(n,d), mod(n, d)

q, r = divide_exact(2013, 10)
print("quotient: ", q, "remainer: ", r)
