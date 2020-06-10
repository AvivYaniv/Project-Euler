from functools import wraps
from time import time

import re

roman_numerals_reduction = { 'IIII' : 'IV', 'XXXX' : 'XL', 'CCCC' : 'CD', 'VIV' : 'IX', 'LXL' : 'XC', 'DCD' : 'CM' }

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

def roman_numeral_to_minimal_from(raw_roman_numbers):
    roman_numbers = []
    # Converting each roman number to its minimal form
    for roman_number in raw_roman_numbers:
        roman_number_minimal_form = roman_number
        for pattern, reduced_pattern in roman_numerals_reduction.items():
            roman_number_minimal_form = re.sub(pattern, reduced_pattern, roman_number_minimal_form)
        roman_numbers.append(roman_number_minimal_form)
    return roman_numbers

# Main
@measure_time_tresholded_decorator()
def main():

    with open('roman.txt', 'r') as f:
        raw_roman_numbers = f.readlines()
    
    # 743
    print(
        sum(len(roman_number) for roman_number in raw_roman_numbers) - 
        sum(len(roman_number) for roman_number in roman_numeral_to_minimal_from(raw_roman_numbers)))
    
if __name__ == "__main__":
    main()
    