from functools import wraps
from time import time

def get_last_digits(multipication, base, power, digits):
    mudolu = 10**digits
    return (multipication * pow(base, power, mudolu) + 1) % mudolu

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

    # 8739992577
    result = get_last_digits(28433, 2, 7830457, 10)
    print(result)

if __name__ == "__main__":
    main()
