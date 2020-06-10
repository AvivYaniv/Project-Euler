from functools import wraps
from time import time

from math import gcd

def get_right_triangles_with_integer_coordinates(boundry):
    # Triangles in:
    # 1. Right angle in axis origin   : (0<p<=boundry, 0) and (0, 0<q<=boundry)     => Total : boundry**2
    # 2. Right angle in axis X        : (0<p<=boundry, 0) and (p, 0<q<=boundry)     => Total : boundry**2
    # 3. Right angle in axis Y        : (0, 0<p<=boundry) and (0<q<=boundry, p)     => Total : boundry**2
    triangles = 3 * (boundry**2)
    # Find triangles inside quadrant
    for x in range(1, boundry+1):
        for y in range(1, boundry+1):
            slope_gcd = gcd(x, y)
            triangles += 2 * (min((boundry - x)*slope_gcd//y, y*slope_gcd//x))
    return triangles

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
    
    # 14234
    print(get_right_triangles_with_integer_coordinates(50))
    
if __name__ == "__main__":
    main()
    