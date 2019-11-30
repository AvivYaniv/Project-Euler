
MULTIPLES = [2, 3, 4, 5, 6]

def GetDigitsCount(a):
    digits_counter = [0] * 10
    while a != 0:
        digits_counter[a % 10] += 1
        a /= 10        
    return digits_counter

def IsPremutation(a, b):
    a_count = GetDigitsCount(a)
    b_count = GetDigitsCount(b)
    for i in xrange(len(a_count)):
        if a_count[i] != b_count[i]:
            return False
    return True

def GetMultiplesPermutation(multiples):
    n = 1
    while True:
        allPremutation = True
        p = n * multiples[0]
        for mi in xrange(1, len(multiples), 1):
            c = n * multiples[mi]
            if not IsPremutation(c, p):
                allPremutation = False
                break
            p = c
        if allPremutation:
            return n
        n += 1

# Main
def main():
    
    # 142857    
    print GetMultiplesPermutation(MULTIPLES)
    
if __name__ == "__main__":
    main()
