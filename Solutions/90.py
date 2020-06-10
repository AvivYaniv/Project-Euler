from functools import wraps
from time import time

from itertools import product
from itertools import permutations
from itertools import combinations
   
CUBE_SIDES  =   6
   
def number_to_tuple(number, tuple_length=None, digit_replacement={}):
    number_as_string    = str(number)
    number_length       = len(number_as_string)
    tuple_length        = tuple_length if tuple_length else number_length 
    zero_padding        = [0] * (tuple_length - number_length)
    number_digits       = [int(d) for d in number_as_string]
    if digit_replacement:
        number_digits   = [ d if d not in digit_replacement.keys() else digit_replacement[d] for d in number_digits ]
    return tuple(zero_padding + number_digits)
    
def is_numbers_cube_repesentable(number, cubes, digit_replacement={}):
    number_as_tuple = number_to_tuple(number, len(cubes), digit_replacement)
    return any(number_permutation in product(*cubes) 
               for number_permutation in permutations(number_as_tuple))
    
def are_numbers_cube_repesentable(numbers, cubes, digit_replacement={}):
    return all(is_numbers_cube_repesentable(number, cubes, digit_replacement) for number in numbers)

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

def get_numbers_representables_cubes(numbers, digit_replacement={}):
    numbers_representable_cubes     = []
    other_cube                      = []
    cubes_digits                    = [ d if d not in digit_replacement.keys() else digit_replacement[d] for d in range(10) ]
    for cube_1 in list(combinations(cubes_digits, CUBE_SIDES)):
        for cube_2 in other_cube:
            cubes = (cube_1, cube_2)
            if are_numbers_cube_repesentable(numbers, cubes, digit_replacement):
                numbers_representable_cubes.append(cubes)
        other_cube.append(cube_1)
    return numbers_representable_cubes

# Main
@measure_time_tresholded_decorator()
def main():
    
    # 1217
    numbers_representable_cubes = get_numbers_representables_cubes([ x**2 for x in range(1, 10) ], digit_replacement={ 9 : 6 })
    print(len(numbers_representable_cubes))
    
if __name__ == "__main__":
    main()
    