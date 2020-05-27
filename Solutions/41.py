
DIGITS              = '123456789'

import math
import itertools

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def GetPremutation(word):
    for p in itertools.permutations(word, len(word)):
        yield ''.join(p)

def GetMaximalPandigitalPrime():
    current_digits = DIGITS
    while current_digits != "":
        maximal_pandigital = 0
        for p_as_string in GetPremutation(current_digits):
            p = int(p_as_string)
            if IsPrime(p) and maximal_pandigital < p:
                maximal_pandigital = p
        current_digits = current_digits[:(len(current_digits) - 1)]
        if 0 != maximal_pandigital:
            return maximal_pandigital
    return 0

# Main
def main():
    
    # 7652413
    print GetMaximalPandigitalPrime()
    
if __name__ == "__main__":
    main()
