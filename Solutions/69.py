
import math

LIMIT = 1000000

def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

# Euler's Totient Function, φ(n), Analysis:
# n / φ(n) = n / (n * ∏_{p|n}(1-1/p)) = 1 / ∏_{p|n}(1-1/p)
# max(n / φ(n)) => min(∏_{p|n}(1-1/p))
def GetTotientMaximum(limit):    
    primes_multipication = 1
    for n in xrange(2, limit, 1):
        if IsPrime(n):
            primes_multipication *= n
        if primes_multipication > limit:
            return primes_multipication / n

# Main
def main():
    
    # 510510
    print GetTotientMaximum(LIMIT)
    
if __name__ == "__main__":
    main()
