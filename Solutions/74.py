
DESIRED_TERMS_NUMBER    = 60
STARTING_NUMBER_LIMIT   = 1000000

def GetDigitFactorialArray():
    digit_factorial_array = [1] * 10
    for d in xrange(2, 10, 1):
        digit_factorial_array[d] *= d * digit_factorial_array[d - 1]
    return digit_factorial_array

DIGIT_FACTORIAL_ARRAY = GetDigitFactorialArray()

def GetNumberDigitFactorial(n):
    return [DIGIT_FACTORIAL_ARRAY[int(d)] for d in str(n)]

def GetNumberDigitFactorialSum(n):
    return sum(GetNumberDigitFactorial(n))

def GetDigitFactorialSumCycles(starting_number_limit):
    digit_factorial_sum_cycles = [0] * starting_number_limit    
    for n in xrange(11, starting_number_limit, 1):               
        if 0 == digit_factorial_sum_cycles[n]:
            cycle = []
            cycle_length = 0
            current_n = n
            while current_n not in cycle:
                cycle.append(current_n)
                cycle_length += 1
                current_n = GetNumberDigitFactorialSum(current_n)
                if current_n < starting_number_limit:
                    current_chain_length = digit_factorial_sum_cycles[current_n]
                    if 0 != current_chain_length:
                        cycle_length += current_chain_length - 1
                        break
            cycle_members = len(cycle)
            for ni in xrange(cycle_members):
                current_n = cycle[ni]
                if current_n < starting_number_limit:
                    if cycle_members == cycle_length:
                        digit_factorial_sum_cycles[current_n] = \
                            cycle_length - ni
                    else:
                        digit_factorial_sum_cycles[current_n] = \
                            current_chain_length + cycle_members - ni
    return digit_factorial_sum_cycles

# Main
def main():

    # 402
    print len(filter(lambda x: DESIRED_TERMS_NUMBER == x, GetDigitFactorialSumCycles(STARTING_NUMBER_LIMIT)))
    
if __name__ == "__main__":
    main()
