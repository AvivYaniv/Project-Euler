
DIGITS_FACTORIAL = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def GetDigitsFactorial(n):
    digits_factorial = []
    division = n
    while division != 0:
        digits_factorial.append(DIGITS_FACTORIAL[division % 10])
        division /= 10
    return digits_factorial

def GetDigitsFactorialNumbers():
    digits_factorial_numbers = []
    # if n>=8: n*9!<number -> limit=10**7
    for n in xrange(10, 10000000, 1):
        if n == sum(GetDigitsFactorial(n)):
            digits_factorial_numbers.append(n)
    return digits_factorial_numbers

# Main
def main():
	
    # 40730
    print sum(GetDigitsFactorialNumbers())
    
if __name__ == "__main__":
    main()
