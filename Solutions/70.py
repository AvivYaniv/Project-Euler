
import math

LIMIT = 10000000

def SieveOfEratosthenes(limit):
    numbers = [False] * 2 + [True] * (limit - 1)
    limit_sqrt = int(math.sqrt(limit)) + 1
    for n in xrange(2, limit_sqrt, 1):
        if numbers[n]:            
            for i in xrange(2 * n, limit, n):
                numbers[i] = False            
    return numbers

def GetPrimesWithSieve(limit, sieve):
    primes = []    
    for n in xrange(limit):
        if sieve[n]:
            primes.append(n)    
    return primes

def GetPrimes(limit):  
    return GetPrimesWithSieve(limit, SieveOfEratosthenes(limit))

def GetDigits(n):
    return [str(d) for d in str(n)]

def IsPremutation(a, b):
    if len(str(a)) != len(str(b)):
        return False
    return sorted(GetDigits(a)) == sorted(GetDigits(b))

# Euler's Totient Function, φ(n), Analysis:
# n / φ(n) = n / (n * ∏_{p|n}(1-1/p)) = 1 / ∏_{p|n}(1-1/p)
# min(n / φ(n)) => max(∏_{p|n}(1-1/p))
# Therefore finding biggest two primes such as:
# φ(n) = (p_{1}-1)*(p_{2}-1)
def GetTotientPermutation(limit):
    d = int(limit * 0.0001)
    limit_sqrt = math.sqrt(limit)
    primes = filter(lambda p: limit_sqrt - d < p and p < limit_sqrt + d , GetPrimes(limit)) 
    p1i = 0
    minimum_n = 0
    minimum_n_divide_phi = 2
    for p1 in primes:        
        for p2 in primes[(1+p1i):]:
            n = p1 * p2
            if n > limit:
                return minimum_n
            phi = (p1 - 1) * (p2 - 1)
            n_divide_phi = float(n) /float(phi) 
            if n_divide_phi < minimum_n_divide_phi and \
               IsPremutation(n, phi):
                minimum_n = n
                minimum_n_divide_phi = n_divide_phi
        p1i += 1
        
# Main
def main():
    
    # 8319823
    print GetTotientPermutation(LIMIT)
    
if __name__ == "__main__":
    main()
