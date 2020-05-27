
EXPANSIONS  =   100

def GetDigitSum(n):
    return sum([int(d) for d in str(n)])

def GetNomeratorOfe(expansions): 
    n = 2
    d = 1
    n, d = d, n    
    a = []
    for i in xrange(1, expansions / 3 + 2, 1):
        a.extend([1, 2 * i, 1])
    i = 0
    for e in xrange(expansions):        
        r = a[i]
        _n = r * d + n
        _d = d
        f_n = _n        
        n, d = _d, _n
        i += 1
    return n

# Main
def main():
    
    # 272
    print GetDigitSum(GetNomeratorOfe(EXPANSIONS))
    
if __name__ == "__main__":
    main()


