LIMIT = 1000000

def IsPalindrom(n):
    return str(n) == str(n)[::-1]

def DecimalToBinary(d):
    return "{0:#b}".format(d)[2:]

def GetDoubleBasedPalindroms(limit):
    double_based_palindroms = []
    for n in xrange(1, limit, 1):
        if IsPalindrom(n) and IsPalindrom(DecimalToBinary(n)):
            double_based_palindroms.append(n)
    return double_based_palindroms

# Main
def main():
    
    # 872187
    print sum(GetDoubleBasedPalindroms(LIMIT))
    
if __name__ == "__main__":
    main()

