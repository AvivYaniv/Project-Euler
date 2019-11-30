
import math

PRIME_FACTORS       = 4
CONSECUTIVE_PRIMES  = 4

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def Divide(d, q):
    c = 0
    while d % q == 0:
        d = d / q
        c += 1
    return (d, c)

def GetNumberPrimeFactors(n, primes):    
    d = n
    p = 2
    counter = 0
    prime_factors = dict()    
    if not (n % 2 == 0 and n > 2) and IsPrime(n):
        prime_factors[n] = 1
        primes.append(n)
        counter += 1
    else:
        for p in primes:
            if d == 1:
                break
            else:
                (d, c) = Divide(d, p)
                if c > 0:
                    prime_factors[p] = c
                    counter += 1
    return (counter, prime_factors)

def GetFirstConsecutiveByFactors(number, factors):
    n = 2    
    primes = []
    numbers = []
    numbers_counter = 0
    while numbers_counter < number:
        if GetNumberPrimeFactors(n, primes)[0] == factors:
            numbers.append(n)
            numbers_counter += 1
        else:
            numbers = []
            numbers_counter = 0
        n += 1
    return numbers

# Main
def main():
 
    # 134043
    print GetFirstConsecutiveByFactors(PRIME_FACTORS, CONSECUTIVE_PRIMES)[0]
    
if __name__ == "__main__":
    main()
