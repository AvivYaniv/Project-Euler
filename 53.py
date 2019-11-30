
import math

N       = 100
LIMIT   = 1000000

def GetPremutationsNumber(n, r, factorials):    
    return (factorials[n]) / (factorials[r] * factorials[n-r])

def GetFactorials(n):
    i = 1
    factorials = [1] + [0] * n
    while i <= n:
        factorials[i] = factorials[i-1] * i
        i += 1
    return factorials

def GetFactorialAboveLimit(factorials, limit):
    n = 0
    while factorials[n] < limit:
        n += 1
    return n    

def GetPremutationsNumberAboveLimit(maximum, limit):
    counter = 0
    factorials = GetFactorials(maximum)
    minimum = GetFactorialAboveLimit(factorials, limit) 
    for n in xrange(minimum, maximum + 1, 1):
        r = n / 2
        while GetPremutationsNumber(n, r, factorials) > limit:
            counter += 1 if (r == n / 2) and (n% 2 != 0) else 2
            r -= 1        
    return counter

# Main
def main():
    
    # 4075
    print GetPremutationsNumberAboveLimit(N, LIMIT)
    
if __name__ == "__main__":
    main()
