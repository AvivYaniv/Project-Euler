
import re

FILE_NAME = 'keylog.txt'

import itertools

def GetNumberPremutation(array):
    for p in itertools.permutations(array, len(array)):
        p_as_string = ''.join(p)
        if '0' != p_as_string:
            yield p_as_string

def ReadListFile(name):
    lines = []
    with open(name) as f:
        lines = [l.strip() for l in f.readlines()]  
    return lines

def GetNumberDigits(n):
    return [str(d) for d in str(n)]

def RemoveArrayDuplicates(array):
    return list(set(array))

def IsDigitsOrderedInNumber(number, ordered_digits):
    index = 0    
    last_digit_index = -1
    number_lenth = len(number)
    digits_to_check = len(ordered_digits)
    while index < digits_to_check and index < number_lenth:
        current_digit = ordered_digits[index]
        current_digit_index = index + number[index:].find(current_digit)
        if -1 == current_digit_index or \
          current_digit_index <= last_digit_index:
            return False
        index += 1
        last_digit_index = current_digit_index
    return index == digits_to_check

def GetDigits(numbers):
    digits = set()
    for number in numbers:
        digits.update(GetNumberDigits(number))
    return list(digits)

def IsContainDigits(number, digits):
    for digit in digits:
        if digit not in number:
            return False
    return True

def DerivePasscode(login_attempts):
    unique_login_attempts = RemoveArrayDuplicates(login_attempts)
    known_digits = GetDigits(login_attempts)
    for password in GetNumberPremutation(known_digits):
        password_as_string = password      
        if IsContainDigits(password, known_digits):            
            not_all_checked = False
            for attempt in unique_login_attempts:
                ordered_digits = GetNumberDigits(attempt)            
                if not IsDigitsOrderedInNumber(password, ordered_digits):
                    not_all_checked = True
                    break
            if not not_all_checked:
                break
    return password

# Main
def main():

    login_attempts = ReadListFile(FILE_NAME)
    
    # 73162890    
    print DerivePasscode(login_attempts)
    
if __name__ == "__main__":
    main()

