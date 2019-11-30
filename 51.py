
import math

FAMILY_SIZE     =   8
DIGITS          =   "0123456789"

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def ReplaceDigit(number, i, d):
    number_as_string = str(number)
    if i == 0 and d == '0':
        return (False, number_as_string)
    if number_as_string[i] == d:
        return (False, number_as_string)    
    replaced = ""
    for p in xrange(len(number_as_string)):
        if p == i:
            replaced += d
        else:
            replaced += number_as_string[p]
    return (True, replaced)

def RepalceThreeDigits(number):    
    replacements = []
    number_as_string = str(number)
    skip_i = False
    for i in xrange(len(number_as_string) - 1):        
        for j in xrange(i, len(number_as_string), 1):
            for k in xrange(i, len(number_as_string), 1):
                family = []
                for d in DIGITS:
                    replace_i = ReplaceDigit(number, i, d)
                    if not replace_i[0]:
                        continue
                    replace_ij = ReplaceDigit(replace_i[1], j, d)
                    if not replace_ij[0]:
                        continue
                    replace_ijk = ReplaceDigit(replace_ij[1], k, d)
                    if not replace_ijk[0]:
                        continue
                    family.append(int(replace_ijk[1]))
                if not family:
                    continue
                yield family

def GetDigitsCount(a):
    digits_counter = [0] * 10
    while a != 0:
        digits_counter[a % 10] += 1
        a /= 10        
    return digits_counter

def Is8ReplacementsFamilyPrime(n):
    n_as_string = str(n)
    isRepeatFound = False
    digit_count = GetDigitsCount(n)
    for c in DIGITS[:-(FAMILY_SIZE-1)]:
        if digit_count[int(c)] == 3:
            isRepeatFound = True
            break
    if not isRepeatFound:
        return False
    return IsPrime(n)

def Ge8ReplacementsFamilyPrimes():
    n = 111111
    family_members = 0
    while family_members < FAMILY_SIZE:        
        if Is8ReplacementsFamilyPrime(n):
            family = []
            family.append(n)
            family_members = 1
            for repalce_family in RepalceThreeDigits(n):
                checked = 0
                replacments_number = len(repalce_family)
                if family:
                    if family_members < FAMILY_SIZE:
                        family = []                    
                        family.append(n)
                        family_members = 1
                for r in repalce_family:                    
                    if replacments_number - checked + family_members < FAMILY_SIZE:
                        break
                    
                    checked += 1
                    if IsPrime(r):
                        family.append(r)
                        family_members += 1
                        
                    if family_members == FAMILY_SIZE:
                        return family
        n += 1
    return family

# Main
def main():
    
    # 121313
    print Ge8ReplacementsFamilyPrimes()[0]
    
if __name__ == "__main__":
    main()
