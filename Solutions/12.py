DIVISORS_MINIMUM = 501

import math

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def GetNumberPrimeFactors(n):
    prime_factors = {}
    d = n
    for q in xrange(2, n, 1):
        if d == 1:
            break
        else:
            c = 0
            while d % q == 0:
                d = d / q
                c += 1
            if c > 0 and IsPrime(q):
                prime_factors[q] = c
    if len(prime_factors) == 0:
        prime_factors[n] = 1
    return prime_factors

def GetNumberOfOptionsToMultiply(items_occurences):
    options = 1
    for item in items_occurences:
        options *= (1 + item)
    return options

def GetTriangleNumber(n):
    return ((n * (n + 1)) / 2)

##def GetNumberOfOptionsToMultiply(n):
##    options = 1
##    d = n
##    for q in xrange(2, n - 1, 1):
##        if d == 1:
##            break
##        else:
##            c = 0
##            while d % q == 0:
##                d = d / q
##                c += 1
####            if c > 0 and IsPrime(q):
####                options *= (c + 1)
##            if c > 0:
##                options *= (c + 1)
##    if d == n:
##        options *= 2
##    return options

# Main
def main():
    n = 3
    divisors = 0
    triangle = 0
    
    while divisors < DIVISORS_MINIMUM:
        triangle = GetTriangleNumber(n)
        prime_factors = GetNumberPrimeFactors(triangle)
        divisors = GetNumberOfOptionsToMultiply(prime_factors.values())
        n += 1

    # 76576500
    print triangle
    
if __name__ == "__main__":
    main()
