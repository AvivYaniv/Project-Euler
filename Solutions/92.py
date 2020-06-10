from functools import wraps
from time import time

import string
import collections
from functools import reduce
from itertools import combinations_with_replacement
from math import factorial
from operator import mul

def get_square_digit_chains_89_results(threshold=10000000):
    # Variable Definition
    threshold_digits_length             = len(str(threshold))
    threshold_trailing_digits_length    = threshold_digits_length - 1
    # Cache Functions
    digits_squares_cache                = { d: d**2 for d in range(10) }    
    def get_cahced_square(d):
        return digits_squares_cache[int(d)]
    factorials_cache                    = { x : factorial(x) for x in range(threshold_digits_length) }
    def get_cahced_factorial(n):
        return factorials_cache[n]
    # Chain Functions
    def get_square_digit_chain(number):
        number       = int(number)
        chain        = [ number ]
        if not 0 == number:
            while number not in (1, 89):
                number = sum(map(get_cahced_square, str(number)))
                chain.append(number)
        return chain
    # Code Section
    square_digit_chains_89_counter      = 0
    for number_digits in combinations_with_replacement(string.digits, threshold_trailing_digits_length):
            chain = get_square_digit_chain(''.join(number_digits))
            if 89 == chain[-1]:
                digits_histogram = collections.Counter(number_digits)
                square_digit_chains_89_counter +=                               \
                    get_cahced_factorial(threshold_trailing_digits_length) //   \
                    reduce(mul, map(get_cahced_factorial, digits_histogram.values()), 1)
    return square_digit_chains_89_counter

def measure_time_tresholded_decorator(RUNTIME_THRESHOLD=60):
    def measure_time_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start       = time()
            result      = f(*args, **kwargs)
            end         = time()
            time_diff   = end-start
            if 60 < time_diff:
                print(f'Fails {RUNTIME_THRESHOLD} runtime threshold ({time_diff}s)')
            else:
                print(f'Elapsed time: {time_diff}s')        
            return result
        return wrapper
    return measure_time_decorator

# Main
@measure_time_tresholded_decorator()
def main():
    
    # 8581146
    print(get_square_digit_chains_89_results())
    
if __name__ == "__main__":
    main()
    