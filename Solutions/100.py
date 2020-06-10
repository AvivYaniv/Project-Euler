from functools import wraps
from time import time


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

    '''
    (s^2-s)/(s^2-s)=1/2
    Therefore Diophantine equation:
    2s^2-2s-t^2+t=0
    '''

    current_special       = 15
    current_total         = 21

    while 1_000_000_000_000 > current_total:
        current_special, current_total = 3 * current_special + 2 * current_total - 2, 4 * current_special + 3 * current_total - 3

    # 756872327473
    result = current_special
    print(result)

if __name__ == "__main__":
    main()
