
DIGITS              = '0123456789'

import itertools

def GetPremutation(word):
    for p in itertools.permutations(word, len(word)):
        yield ''.join(p)

def ConstructNumber(digits):
    power = 1
    number = 0
    digits_revered = digits[::-1]
    for d in digits_revered:
        number += int(d) * power
        power *= 10
    return number

def GetPandigitalSubStringDivisable(DIGITS):
    pandigital_substring_divisable = []    
    for p in GetPremutation(DIGITS):
        if p[0] == "0":
            continue
        if 0 == ConstructNumber([p[1], p[2], p[3]]) % 2 and \
           0 == ConstructNumber([p[2], p[3], p[4]]) % 3 and \
           0 == ConstructNumber([p[3], p[4], p[5]]) % 5 and \
           0 == ConstructNumber([p[4], p[5], p[6]]) % 7 and \
           0 == ConstructNumber([p[5], p[6], p[7]]) % 11 and \
           0 == ConstructNumber([p[6], p[7], p[8]]) % 13 and \
           0 == ConstructNumber([p[7], p[8], p[9]]) % 17:
            pandigital_substring_divisable.append(int(p))
    return pandigital_substring_divisable

# Main
def main():
    
    # 16695334890
    print sum(GetPandigitalSubStringDivisable(DIGITS))
    
if __name__ == "__main__":
    main()
