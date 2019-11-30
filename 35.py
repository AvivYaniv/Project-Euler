LIMIT = 1000000

import math

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def GetCircularPrimes(limit):
    circular_primes = set()
    for n in xrange(2, limit, 1):
        if n in circular_primes:
            continue
        elif IsPrime(n):
            isAllPrimes = True
            circular = []
            n_as_string = str(n)
            for i in xrange(len(n_as_string)):
                p = n_as_string[i:] + n_as_string[:i]
                if IsPrime(int(p)):                 
                    circular.append(int(p))
                else:
                    isAllPrimes = False
                    break
            if isAllPrimes:
                circular_primes.update(circular)
    return circular_primes

# Main
def main():

    # 55
    print len(GetCircularPrimes(LIMIT))
    
if __name__ == "__main__":
    main()
