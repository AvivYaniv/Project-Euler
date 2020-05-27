N_LIMIT = 10000

import math

def GetDivisors(n):
    divisors = set([1])
    for i in xrange(2, int(math.sqrt(n) + 1), 1):
        if n % i == 0:
            divisors.update([i, n / i])
    return divisors

def GetAmicableNumbers(n_limit):
    amicable = set()
    divisors_sum_to_n = dict()

    for i in range(1, n_limit):
        divisors = GetDivisors(i)
        divisors_sum = sum(divisors)
        entry = divisors_sum_to_n.get(divisors_sum)
        if entry is None:
            divisors_sum_to_n[divisors_sum] = []
        divisors_sum_to_n[divisors_sum].append(i)

    for divisors_sum in divisors_sum_to_n.keys():
        numbers = divisors_sum_to_n[divisors_sum]

        for number in numbers:
            if divisors_sum != number:
                number_as_divisor_sum_entry = divisors_sum_to_n.get(number)
                if number_as_divisor_sum_entry is not None:
                    if divisors_sum in number_as_divisor_sum_entry:                    
                        amicable.update([divisors_sum, number]) 
    
    return amicable

# Main
def main():	
    # 31626
    print sum(GetAmicableNumbers(N_LIMIT))
    
if __name__ == "__main__":
    main()
