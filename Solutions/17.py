N_LIMIT = 1000

TEENS = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
UNITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
TENS = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
HUNDREND = 'Hundred'
THOUSAND = 'Thousand'
BRITISH_NUMBER_CONCATING_DELIMITER = 'and'

def NumberAsWord(n):
    n_as_word = ''
    n_as_string = str(n)
    n_length = len(n_as_string)    
    if n_length == 1:
        n_as_word = UNITS[n - 1]
    elif n_length == 2:
        if 10 < n < 20:
            n_as_word = TEENS[(n % 10) - 1]
        else:
            units = n % 10
            if units == 0:
                units_as_word = ''
            else:
                units_as_word = NumberAsWord(units)
            tens = n / 10
            tens_as_word = TENS[tens - 1]
            n_as_word = tens_as_word + ' ' + \
                        units_as_word
    elif n_length == 3:
        hundrends = n / 100        
        tens_and_units = n % 100
        if tens_and_units == 0:
            tens_and_units_as_word = ''
        else:
            tens_and_units_as_word = \
                ' ' + \
                BRITISH_NUMBER_CONCATING_DELIMITER + ' ' + \
                NumberAsWord(tens_and_units)
        n_as_word = UNITS[hundrends - 1] + ' ' + HUNDREND + \
                    tens_and_units_as_word
    elif n_length == 4:
        thousands = n / 1000
        hundrends_tens_and_units = n % 1000
        if hundrends_tens_and_units == 0:
            hundrends_tens_and_units_as_word = ''
        else:
            hundrends_tens_and_units_as_word = \
                ' ' + \
                NumberAsWord(hundrends_tens_and_units)
        n_as_word = UNITS[thousands - 1] + ' ' + THOUSAND + \
                    hundrends_tens_and_units_as_word
    return n_as_word        

def LettersInNumber(number_as_word):
    return len(number_as_word.replace(' ', ''))

# Main
def main(): 
    sum_letters = 0
    for n in xrange(1, N_LIMIT + 1, 1):
        sum_letters += LettersInNumber(NumberAsWord(n))
        
    # 21124
    print sum_letters
    
if __name__ == "__main__":
    main()
