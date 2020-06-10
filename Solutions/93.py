from functools import wraps
from time import time

from itertools import product
from itertools import permutations
from itertools import combinations

def is_positive_integer(n):
    return (0 < n) and (int(n) == n)

def get_arithmetic_expressions_results_for_numbers(digits           = range(1, 10),
                                                   operators        = ['+', '-', '*', '/'], 
                                                   condition_tester = is_positive_integer):
    operands_to_sequences = {}
    for operands in combinations(digits, 4):
        expression_results = set()
        for operator, operand in product(product(operators, repeat=3), permutations(operands)):
            expressions = [ \
                            f'({operand[0]}{operator[0]}{operand[1]}){operator[1]}({operand[2]}{operator[2]}{operand[3]})',
                            f'(({operand[0]}{operator[0]}{operand[1]}){operator[1]}{operand[2]}){operator[2]}{operand[3]}'
                          ]            
            for expression in expressions:
                result = eval(expression)
                if condition_tester(result): 
                    expression_results.add(int(result))        
        operands_to_sequences[operands] = expression_results
    return operands_to_sequences

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
    
    def get_consecutive_numbers_length(iteratebale):
        consecutive_numbers = []
        for n in range(1, len(iteratebale)):
            if n not in iteratebale:
                break
            else:
                consecutive_numbers.append(n)
        return len(consecutive_numbers)
    
    # 1258
    operands_to_sequences                                       = get_arithmetic_expressions_results_for_numbers()
    operands_to_sequences_sorted_by_consecutive_numbers_length  = sorted(operands_to_sequences, key=lambda k: get_consecutive_numbers_length(operands_to_sequences[k]))
    print(int(''.join(str(i) for i in operands_to_sequences_sorted_by_consecutive_numbers_length[-1])))
    
    
if __name__ == "__main__":
    main()
    