from functools import wraps
from time import time

from math import log

def measure_time_tresholded_decorator(RUNTIME_THRESHOLD=60):
    def measure_time_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = time()
            result = f(*args, **kwargs)
            end = time()
            time_diff = end - start
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

    base_exponents = []
    # Read exponents from file
    with open('base_exp.txt', 'r') as base_exp_file:
        base_exponents = [line.split(',') for line in base_exp_file.readlines()]

    values = []
    for base, exponent in base_exponents:
        '''
        log_a(x^y)=y*log_a(x)
        '''
        values.append(int(exponent) * log(int(base)))

    # 709
    result = 1+values.index(max(values))
    print(result)

if __name__ == "__main__":
    main()
