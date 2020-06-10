from functools import wraps
from time import time

import math

TRESHOLD                    = 50000000

primes                      = set()

class PowersMemoization:
    def __init__(self, power_lower, power_upper):
        self.power_lower    = power_lower
        self.power_upper    = power_upper
        self.memoization    = {}
    def get(self, n, power):
        if n not in self.memoization.keys():
            self.memoization[n] = [ n ** self.power_lower ]
            for power_number in range(self.power_lower + 1, self.power_upper + 1):
                self.memoization[n].append(n * self.memoization[n][power_number-self.power_lower-1])
        return self.memoization[n][power-self.power_lower]
        
def is_prime(a):
    if a in primes:
        return True
    if a <= 1:
        return False 
    for i in range(2, a//2 + 1): 
        if 0 == (a % i): 
            return False
    primes.add(a)
    return True
    
def get_primes_up_to_treshold(threshold):
    return [ n for n in range(threshold) if is_prime(n) ]

def get_expressible_as_sum_of_prime_square_prime_cube_prime_fourth_power(treshold=TRESHOLD):
    expressibles        = set()
    powers_memoization  = PowersMemoization(2, 4)
    primes_in_range     = get_primes_up_to_treshold(int(math.sqrt(treshold))+1)
    for x in primes_in_range:
        for y in primes_in_range:
            for z in primes_in_range:
                n = powers_memoization.get(x, 2)  + powers_memoization.get(y, 3) + powers_memoization.get(z, 4)
                if n > treshold:
                    break
                expressibles.add(n)                    
    return expressibles

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
    
    # 1097343
    print(len(get_expressible_as_sum_of_prime_square_prime_cube_prime_fourth_power()))
    
if __name__ == "__main__":
    main()
    