
import math
from decimal import *

LAST_NUMBER                     =   100
PRECISION                       =   100
NO_ROUNDING_PRECISION_ADDUP     =   5

getcontext().prec   =   PRECISION + NO_ROUNDING_PRECISION_ADDUP

def GetSqureRootDigits(n):
    n_sqrt = str(Decimal(n).sqrt())
    if "." not in n_sqrt:
        return (int(n_sqrt), 0)
    n_sqrt_splitted = n_sqrt.split(".") 
    return [n_sqrt_splitted[0], n_sqrt_splitted[1]]

def GetIrrationlSquareRootsDigits(last_number):
    sqrt_digits_after_point = [0] * (last_number + 1)
    for number in xrange(2, last_number + 1):
        sqrt_digits = GetSqureRootDigits(number)
        if 0 != int(sqrt_digits[1]):
            sqrt_digits_after_point[number] = \
                str(sqrt_digits[0]) + \
                str(sqrt_digits[1])[:PRECISION-len(str(sqrt_digits[0]))]              
    return sqrt_digits_after_point

def SumNumberDigits(n):
    return sum([int(d) for d in str(n)])

# Main
def main():
    
    # 40886
    print sum([SumNumberDigits(n) for n in GetIrrationlSquareRootsDigits(LAST_NUMBER)])
    
if __name__ == "__main__":
    main()
