import math

A_B_ABSOLUTE_VALUE = 1000 - 1

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def QuadraticsEquation(a, b, x):
    return x**2 + a * x + b

def GetConsecutivePrimesOfQuadraticsEquation(a, b):
    n = 0
    primes_counter = 0       
    while True:
        p = QuadraticsEquation(a, b, n)
        if p <= 0 or not IsPrime(p):
            break
        else:
            n += 1
            primes_counter += 1            
    return primes_counter    

def GetMaximalConsecutivePrimesOfQuadraticsEquation(coefficients_absolute_value):
    maximal_consecutive_a = 0
    maximal_consecutive_b = 0
    maximal_consecutive_primes = -1
    for a in xrange(-1 * coefficients_absolute_value, coefficients_absolute_value, 1):
        for b in xrange(-1 * coefficients_absolute_value, coefficients_absolute_value, 1):
            consecutive_primes = \
                GetConsecutivePrimesOfQuadraticsEquation(a, b)
            if consecutive_primes > maximal_consecutive_primes:
                maximal_consecutive_primes = consecutive_primes
                maximal_consecutive_a = a
                maximal_consecutive_b = b
    return (maximal_consecutive_a, maximal_consecutive_b, maximal_consecutive_primes)

# Main
def main():
    
    maximal_consecutive = GetMaximalConsecutivePrimesOfQuadraticsEquation(A_B_ABSOLUTE_VALUE)
    
    # -59231
    print maximal_consecutive[0] * maximal_consecutive[1]
    
if __name__ == "__main__":
    main()
