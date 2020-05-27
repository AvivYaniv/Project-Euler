import math

SINCE_N_ALL_TWO_ABUNDANTS_SUM = 28123

def GetDivisors(n):
    divisors = set([1])
    for i in xrange(2, int(math.sqrt(n) + 1), 1):
        if n % i == 0:
            divisors.update([i, n / i])
    return divisors

def GetAbundantNumbers(n_limit):
    abundant_set = set()
    for i in range(1, n_limit):
        divisors = GetDivisors(i)
        divisors_sum = sum(divisors)
        if divisors_sum > i:
            abundant_set.update([i])
    return abundant_set

def GetAllNumbersNotTwoAbudantsSum():
    abundants = GetAbundantNumbers(SINCE_N_ALL_TWO_ABUNDANTS_SUM)
    not_two_abudants_sum = set(range(1, SINCE_N_ALL_TWO_ABUNDANTS_SUM - 1, 1))
    for a1 in abundants:
        for a2 in abundants:
            abundants_sum = a1 + a2
            if abundants_sum >= SINCE_N_ALL_TWO_ABUNDANTS_SUM:
                break
            else:
                not_two_abudants_sum.discard(abundants_sum)
    return not_two_abudants_sum

# Main
def main():    
    # 4179871
    print sum(GetAllNumbersNotTwoAbudantsSum())
    
if __name__ == "__main__":
    main()
