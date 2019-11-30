
import operator
import functools

DIGITS_NUMBERS = [1, 10, 100, 1000, 10000, 100000, 1000000]

def GetChampernowneConstantDigits(digits_numbers):
    n = 1
    digit_number = 1
    desirted_digits = []
    reverse_desirted_digit_numbers = digits_numbers[::-1] 
    current_desirted_digit_number = reverse_desirted_digit_numbers.pop()    
    while 0 != len(reverse_desirted_digit_numbers):
        n_as_string = str(n)
        for d in n_as_string:
            if digit_number == current_desirted_digit_number:
                desirted_digits.append(int(d))
                if 0 == len(reverse_desirted_digit_numbers):
                    break
                current_desirted_digit_number = reverse_desirted_digit_numbers.pop()
            digit_number += 1        
        n += 1
    return desirted_digits    

# Main
def main():
    
    # 210
    print functools.reduce(operator.mul, GetChampernowneConstantDigits(DIGITS_NUMBERS), 1)
    
if __name__ == "__main__":
    main()
