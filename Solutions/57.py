
import math
from fractions import Fraction

EXPANSIONS  = 1000

def GetNumeratorMoreDigitsThanDenominatorSquareRoot2(expansions): 
    n = 2
    d = 1
    n, d = d, n
    repeat = 2
    numerator_more_digits_then_denominator = 0    
    for e in xrange(expansions):
        _n = repeat * d + n
        _d = d
        f_n = _n + _d
        f_d = _n
        n, d = _d, _n
        if len(str(f_n)) > len(str(f_d)):            
            numerator_more_digits_then_denominator += 1
    return numerator_more_digits_then_denominator

# Main
def main():
    
    # 153
    print GetNumeratorMoreDigitsThanDenominatorSquareRoot2(EXPANSIONS)
    
if __name__ == "__main__":
    main()
