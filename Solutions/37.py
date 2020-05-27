
import math

NUMBER_OF_TRUNCATABLE_PRIMES = 11

def IsPrime(n):
    if n == 1:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def GetTruncateFromRight(n):
    n_as_string = str(n)
    for i in xrange(1, len(n_as_string), 1):
        yield int(n_as_string[:i])
        
def GetTruncateFromLeft(n):
    n_as_string = str(n)
    for i in xrange(1, len(n_as_string), 1):
        yield int(n_as_string[i:])

def GetTruncatablePrimes():
    n = 10
    truncatable_primes = []
    while len(truncatable_primes) < NUMBER_OF_TRUNCATABLE_PRIMES:
        isAllPrimes = True
        if IsPrime(n):
            n_as_string = str(n)
            for i in xrange(1, len(n_as_string), 1):
                r = int(n_as_string[:i])
                l = int(n_as_string[i:])
                if not IsPrime(r) or not IsPrime(l):
                    isAllPrimes = False
                    break
            if isAllPrimes:
                truncatable_primes.append(n)
        n += 1
    return truncatable_primes

# Main
def main():
    
    # 748317
    print sum(GetTruncatablePrimes())
    
if __name__ == "__main__":
    main()
