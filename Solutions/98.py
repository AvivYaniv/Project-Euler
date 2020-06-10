import math
from functools import wraps
from time import time

import itertools

def is_square(n):
    return n == math.isqrt(n) ** 2

def get_anagramic_words(words):
    anagramic_words_dictionary = {}
    for word in words:
        anagramic_words_dictionary.setdefault(''.join(sorted(word)), set()).add(word)
    return dict(filter(lambda t: 1 < len(t[1]), anagramic_words_dictionary.items()))

def get_word_number_after_digit_assignment(word, letters_digits):
    return int(''.join(letters_digits[c] for c in word))

def get_anagramic_words_condition(all_words, condition_checker=is_square):
    all_words_numbers_after_digits_assignment = set()
    anagramic_words_dictionary = get_anagramic_words(all_words)
    for anagramic_words_as_sorted, anagramic_words in anagramic_words_dictionary.items():
        for word_1, word_2 in itertools.combinations(anagramic_words, 2):
            for digits_premutation in itertools.permutations('123456789', len(anagramic_words_as_sorted)):
                letters_digits                          = {letter : digits_premutation[letter_index] for letter_index, letter in enumerate(anagramic_words_as_sorted)}
                words_numbers_after_digits_assignment   = set([get_word_number_after_digit_assignment(word, letters_digits) for word in [word_1, word_2]])
                if all([condition_checker(x) for x in words_numbers_after_digits_assignment]):
                    all_words_numbers_after_digits_assignment |= words_numbers_after_digits_assignment
    return all_words_numbers_after_digits_assignment

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

    # Read words from file
    with open('words.txt', 'r') as words_file:
        words_file_words = [raw_word.replace('\"', '') for raw_word in words_file.read().split(',')]

    # 18769
    result = max(get_anagramic_words_condition(words_file_words))
    print(result)

if __name__ == "__main__":
    main()
