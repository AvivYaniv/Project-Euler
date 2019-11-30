
import math

PARTITIONS_NUMBER = 5000

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

def GetPrimePartitions(partitions_number):
    primes = GetPrimes(partitions_number)
    n = 2
    ways = [1] + [0]*n 
    while ways[n-1] < partitions_number:
        n += 1
        ways = [1] + [0]*n      
        for prime in primes:
            for sum in xrange(prime, n + 1, 1):
                ways[sum] += ways[sum - prime]        
    return n - 1
               
# Main
def main():
    
    # 71
    print GetPrimePartitions(PARTITIONS_NUMBER)
   
if __name__ == "__main__":
    main()
