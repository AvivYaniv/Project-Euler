from functools import wraps
from time import time
 
def get_almost_equilateral_triangle_generator():
    """
    Almost equilateral triangle is built from two identical stitched right angle triangles:
    The right angle triangles sides, can be set such as a<b<c:
    1) Side 'a'    ; would be half of the base of the almost_equilateral_triangle
    2) Side 'b'    ; would be the height of the almost_equilateral_triangle
    3) Side 'c'    ; would be the equal side of the almost_equilateral_triangle   
    Each of the right angle triangles, can be expressed with pythagorean triple
    The following formula steams form parent-child relationships of the pythagorean triples
    Such as : {Parent}={2a-c=1} => {Child}={-2a+c=1}
    """
    a, b, c = 3, 4, 5    
    while True:
        yield [c, 2*a, c]
        a, b, c = -2*a+b+2*c, -a+2*b+2*c, -2*a+2*b+3*c
 
def get_almost_equilateral_triangle_perimeters(perimeter_threshold):
    almost_equilateral_triangle_perimeters      = []
    almost_equilateral_triangle_generator       = get_almost_equilateral_triangle_generator()
    almost_equilateral_triangle_perimeter       = sum(next(almost_equilateral_triangle_generator))
    while almost_equilateral_triangle_perimeter < perimeter_threshold:
        almost_equilateral_triangle_perimeters.append(almost_equilateral_triangle_perimeter)
        almost_equilateral_triangle_perimeter   = sum(next(almost_equilateral_triangle_generator))
    return almost_equilateral_triangle_perimeters
    
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
    
    # 518408346
    sum_almost_equilateral_triangle_perimeters_under_treshold = sum(get_almost_equilateral_triangle_perimeters(perimeter_threshold=1_000_000_000))
    print(sum_almost_equilateral_triangle_perimeters_under_treshold)    
    
if __name__ == "__main__":
    main()
    