
import math
import fractions

PERIMITER_LIMIT             =   1500000
DESIRED_SOLUTIONS_NUMBER    =   1

def SetPowers(array):
    for i in xrange(len(array)):
        array[i] = i*i

# Euclid's Formula:
# Given: m, n
#   Such as:
#       1. m > m
#       2. m - n is odd
#       3. m & n are coprime
#
# Generate Pythagorean triple: k ∈ ℕ
#   a = k(m^2-n^2)
#   b = 2kmn
#   c = k(m^2+n^2)
# 
def GetRightAngleTrianglesSolutionsNumberByPerimeter(perimeter_limit):
    powers = [0] * (perimeter_limit + 1)
    SetPowers(powers)
    perimeter_solutions = [0] * (perimeter_limit + 1)    
    for m in xrange(2, 1 + int(math.sqrt(perimeter_limit / 2)), 1):
        for n in xrange(1, m, 1):
            if 0 != (m - n) % 2 and \
               1 == fractions.gcd(m, n):
                a = powers[m] - powers[n]
                b = 2*m*n
                c = powers[m] + powers[n]
                abc_sum = sum([a, b, c])
                p = abc_sum
                while p <= perimeter_limit:
                    perimeter_solutions[p] += 1
                    p += abc_sum
    return perimeter_solutions

# Main
def main():
    
    # 161667
    print len(filter(lambda s: DESIRED_SOLUTIONS_NUMBER == s, GetRightAngleTrianglesSolutionsNumberByPerimeter(PERIMITER_LIMIT)))
    
if __name__ == "__main__":
    main()
