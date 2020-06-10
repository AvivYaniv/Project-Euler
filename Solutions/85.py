from functools import wraps
from time import time

import sys
from functools import reduce

RECTANGLES_NUMBER   =   2000000

def get_triangular_number(n):
    return (n*n+n) // 2

def get_rectangels_possibilities(a, b):
    return get_triangular_number(a) * get_triangular_number(b)

def get_closest_rectangles_number(rectangles_number):
    # Initializing with rectangle with `rectangles_number` area
    a                   = rectangles_number
    b                   = 1
    nearest_difference  = sys.maxsize
    dimentions          = [ a, b ]
    # Searching for closest rectangles number
    while a >= b:
        rectangels_possibilities    = get_rectangels_possibilities(a, b)
        current_diffrence           = rectangels_possibilities - rectangles_number
        current_diffrence_abs       = abs(current_diffrence)
        # If current difference is smaller
        if nearest_difference > current_diffrence_abs:
            nearest_difference      = current_diffrence_abs
            dimentions              = [ a, b ]
        if 0 < current_diffrence:
            a -= 1
        else:
            b += 1        
    return dimentions
       
def get_area(dimentions):
    return reduce(lambda x, y: x*y, dimentions)

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
    # 2772
    print(get_area(get_closest_rectangles_number(RECTANGLES_NUMBER)))      
    
if __name__ == "__main__":
    main()
    