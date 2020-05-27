N = 1000

import math

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def GetPrimesTill(n):
    primes = [2]
    for p in xrange(3, n + 1, 1):
        if IsPrime(p):
            primes.append(p)
    return primes

def GetLongestCycleTillDenominator(n):
    # Going from greatest denominator to smallest
    # as we search for the longest cycle
    for p in GetPrimesTill(n)[::-1]:
        cycle = 1
        # According to Fermat's little theorem
        while 10**cycle % p != 1:
            cycle += 1
        # Longest cycle for prime p, is of p-1 length
        if p-1 == cycle:
            break
    return p

# Main
def main():	
    # 983    
    print GetLongestCycleTillDenominator(N)
    
if __name__ == "__main__":
    main()
    
