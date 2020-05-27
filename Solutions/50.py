
import math

LIMIT = 1000000

def SieveOfEratosthenes(limit):
    numbers = [False] * 2 + [True] * (limit - 1)
    limit_sqrt = int(math.sqrt(limit)) + 1
    for n in xrange(2, limit_sqrt, 1):
        if numbers[n]:            
            for i in xrange(2 * n, limit, n):
                numbers[i] = False            
    return numbers

def GetPrimes(limit):  
    return GetPrimesWithSieve(limit, SieveOfEratosthenes(limit))

def GetPrimesWithSieve(limit, sieve):
    primes = []    
    for n in xrange(limit):
        if sieve[n]:
            primes.append(n)    
    return primes

def FindInSortedArray(v, arr, isReversed):
    for c in arr:
        if c == v:
            return True
        else:
            if (isReversed and c < v) or \
               (not isReversed and c > v):
                break
    return False

def GetMaximalConsecutivePrimesSumPrime(limit):
    sieve = SieveOfEratosthenes(limit)
    primes = GetPrimesWithSieve(limit, sieve)
    last_prime = primes[-1]
    number_of_primes = len(primes)
    maiximal_sum_prime = 0
    maximal_consecutive_length = 0
    for i in xrange(number_of_primes):
        s = 0
        for j in xrange(i + 1, number_of_primes, 1):
            s += primes[j]
            if s > last_prime:
                break
            else:
                consecutive_length = j - i
                if consecutive_length > maximal_consecutive_length and \
                    sieve[s]:
                    maiximal_sum_prime = s
                    maximal_consecutive_length = consecutive_length
    return (maiximal_sum_prime, maximal_consecutive_length)

# Main
def main():
    
    # 997651
    print GetMaximalConsecutivePrimesSumPrime(LIMIT)[0]
    
if __name__ == "__main__":
    main()
