
import math
from functools import wraps
from time import time

from iteration_utilities import first

def get_divisors(n):
    divisors = set([1])
    for i in range(2, int(math.sqrt(n) + 1), 1):
        if 0 == n % i:
            divisors.update([i, int(n / i)])
    return divisors

class DivisorsSumGenerator:
    def __init__(self, threshold):
        self.threshold = threshold
        self._init_divisors_sum_cache()

    def _init_divisors_sum_cache(self):
        divisors_sum_cache = [0, 1]
        for number in range(2, self.threshold + 1):
            divisors_sum_cache.append(sum(get_divisors(number)))
        self.divisors_sum_cache = divisors_sum_cache

    def get_divisors_sum_generator(self, current_member):
        while current_member <= self.threshold:
            current_member = self.divisors_sum_cache[current_member]
            yield current_member

def get_amicable_chains(threshold=1_000_000):
    length_to_amicable_chain = {}
    divisors_sum_generator = DivisorsSumGenerator(threshold)
    for chain_start_member in range(1, threshold + 1):
        amicable_chain_members = set()
        for member in divisors_sum_generator.get_divisors_sum_generator(chain_start_member):
            # If chain returns to an existing member
            if member in amicable_chain_members:
                break
            amicable_chain_members.add(member)
            # If chain ends cycle
            if member == chain_start_member:
                length_to_amicable_chain.setdefault(len(amicable_chain_members), set()).add(frozenset(amicable_chain_members))
                break
    return length_to_amicable_chain

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

    # 14316
    length_to_amicable_chain = get_amicable_chains()
    result = min(first(length_to_amicable_chain[max(length_to_amicable_chain.keys())]))
    print(result)
    

if __name__ == "__main__":
    main()
