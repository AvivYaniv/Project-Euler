
N           =   100
A_MAXIMAL   =   N
B_MAXIMAL   =   N

def GetDigitsSum(n):
    digits_sum = 0
    c = n
    while 0 != c:
        digits_sum += c % 10
        c /= 10
    return digits_sum

def GetMostPowerfulDigitSum(a_maximum, b_maximum):
    most_powerful_digit_sum = 0
    most_powerful_digit_sum_a = 0
    most_powerful_digit_sum_b = 0

    for a in xrange(2, a_maximum, 1):
        for b in xrange(2, a_maximum, 1):
            power_digit_sum = GetDigitsSum(a ** b)
            if most_powerful_digit_sum < power_digit_sum:
                most_powerful_digit_sum = power_digit_sum
                most_powerful_digit_sum_a, most_powerful_digit_sum_b = a, b

    return most_powerful_digit_sum

# Main
def main():
    
    # 972
    print GetMostPowerfulDigitSum(A_MAXIMAL, B_MAXIMAL)
    
if __name__ == "__main__":
    main()
