
N               = 1000
LAST_DIGITS     = 10
TENS_POWERS     = [10**i for i in xrange(LAST_DIGITS)]

def DigitsToNumber(d):
    n = 0
    for i in xrange(len(d)):
        n += d[i] * TENS_POWERS[i]
    return n

def GetTillDigit(a, m):
    digits = []
    c = 0
    while a != 0:
        digits.append(a % 10)        
        a /= 10
        c += 1
        if c == m:
            break
    return digits

def AddTillDigit(a, b, m):
    r = 0
    mn = int('9' * m)
    for i in xrange(max(len(a), len(b))):
        if i > m:
            break
        av = 0 if i >= len(a) else a[i]
        bv = 0 if i >= len(b) else b[i]
        r += (av + bv) * TENS_POWERS[i]
    if r > mn:
        r = int(str(r)[-m:])      
    return r

def MultiplyTillDigit(a, b, m):
    r = 0
    mn = int('9' * m)
    for ai in xrange(len(a)):
        if ai > m:
            break
        for bi in xrange(len(b)):
            if bi > m:
                break
            elif ai + bi < m:
                r += (a[ai] * TENS_POWERS[ai]) * (b[bi] * TENS_POWERS[bi])
    if r > mn:
        r = int(str(r)[1:])      
    return r

def PowerTillDigit(a, b, m):
    d = GetTillDigit(a, m)
    p = d[::]
    for i in xrange(b - 1):        
        p = GetTillDigit(MultiplyTillDigit(d, p, m), m)
    return p

def SumSelfPowersStragightForward(n, d):
    r = 0
    for i in xrange(1, n + 1, 1):
        r += i**i
    return int(str(r)[-d:]) 

def SumSelfPowers(n, d):
    r = [0]
    for i in xrange(1, n + 1, 1):
        r = GetTillDigit(AddTillDigit(r, PowerTillDigit(i, i, d), d), d)
    return DigitsToNumber(r)

# Main
def main():
    
    # 9110846700
    print SumSelfPowers(N, LAST_DIGITS)
    
if __name__ == "__main__":
    main()
