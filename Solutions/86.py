from functools import wraps
from time import time

import math

TOTAL_NUMBER_OF_SHORTEST_PATHES_THRESHOLD    =   1000000

def get_shortest_path_in_cuboid_tresholded(total_number_of_shortest_pathes_threshold = TOTAL_NUMBER_OF_SHORTEST_PATHES_THRESHOLD):
    """
    Cuboid dimenstions are (a, b, c):
    When unfolding it can be seen that distance between two corners is
    `path = sqrt(a^2 + (b+c)^2)`
    Lets denote `(b+c)` as simply `bc`       
    """
    # Functions Definition
    def is_integer(real_number):
        return int(real_number) == real_number
    def get_cuboid_shortest_path(a, bc):
        return math.sqrt(a**2 + bc**2)
    def get_shortest_pathes_in_cuboid(M):
        """
        We want to check cuboids such as:
        `1<=a<=M`
        `1<=b<=M`
        `1<=c<=M`
        It can be seen that the following satisfies too the requirements:
        `1<=a<=M`
        `1<=b+c<=2*M` 
        """
        a                       = M
        shortest_pathes_counter = 0
        # Looping through `1<=b+c<=2*M`
        for bc in range(2, 2 * M + 1):
            # If shortest path is integer                 
            if is_integer(get_cuboid_shortest_path(a, bc)):
                # In case `bc > M`:
                # Dimensions that satisfy the requirements:
                # (bc+1)/2 <= c <= M  
                if (bc > M):
                    shortest_pathes_counter += (M - (bc+1)/2) + 1
                # Else `bc <= M`:
                # Dimensions that satisfy the requirements:
                # (b=1, c=bc-1) ... (b=bc/2, c=bc/2)                  
                else:
                    shortest_pathes_counter += bc / 2
        return shortest_pathes_counter
    # Variables Definition
    M                       = 0
    shortest_pathes_counter = 0
    # Code Section
    # Finding first time total shortest paths exceeds threshold
    while (shortest_pathes_counter < total_number_of_shortest_pathes_threshold):
        M += 1
        shortest_pathes_counter += get_shortest_pathes_in_cuboid(M)       
    return M

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
    
    # 1818
    print(get_shortest_path_in_cuboid_tresholded())
    
if __name__ == "__main__":
    main()
    