from functools import wraps
from time import time

import math
from itertools import product

class Factorizer:
    def __init__(self, treshold):        
        self.n_to_factorization          = dict()        
    
    def factorize(self, n):
        # If n has not already been factorized
        if n not in self.n_to_factorization.keys():            
            # Factorize n
            n_factorinzations = { (n,) }
            # Going over all possible factors of n
            # 2 <= possible_factor <= math.sqrt(n)
            for factor in [possible_factor for possible_factor in range(2, int(math.sqrt(n))+1) if not n % possible_factor]:
                # Factor divides number, adding factor's factors and division factors combination
                for factors_factor, factors_division_factor in product(self.factorize(factor), self.factorize(n // factor)):
                    n_factorinzations.add(tuple(sorted(list(factors_factor+factors_division_factor))))
            self.n_to_factorization[n] = n_factorinzations
        return self.n_to_factorization[n]

def find_k_to_mps_in_range(lower_bound, upper_bound):    
    k_to_mps    = dict()
    factorizer  = Factorizer(upper_bound)
    # For minimal-product-sum k, is bounded by: k <= MPS <= 2k
    # The upper bound can be created as:
    # 2k = 2 + k + (k-2) * [1]     
    for n in range(lower_bound*2, upper_bound*2+1):
        for n_factor in [ n_factor for n_factor in factorizer.factorize(n) if 1 != len(n_factor)]:
            product_of_factors, sum_of_factors, number_of_factors = n, sum(n_factor), len(n_factor)
            # Any k can be a valid minimal-product-sum, by the following recipe
            k = product_of_factors - sum_of_factors + number_of_factors
            # If mps found for k - it's not the minimal
            if k in k_to_mps.keys():
                continue
            # If k is valid 
            if lower_bound <= k <= upper_bound:
                k_to_mps[k] = n
    return k_to_mps

def find_mps_in_range(lower_bound, upper_bound):
    return set( mps for mps in find_k_to_mps_in_range(lower_bound, upper_bound).values() )

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
    
    # 7587457
    print(sum(find_mps_in_range(lower_bound=2, upper_bound=12000)))
    
if __name__ == "__main__":
    main()
    