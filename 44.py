
import math

def IsInteger(f):
    return int(f) == f

def GetPentagonalNumberIndex(x):
    return (1 + math.sqrt(1 + 24*x)) / 6

def IsPentagonalNumber(x):
    return IsInteger(GetPentagonalNumberIndex(x))

def GetPentagonalNumber(n):
    return int((n * (3*n-1))/2)

def GetMinimumPentagonalDiffrence():
    j = 1    
    Pj = GetPentagonalNumber(j)
    Pj_1 = 0
    min_diff = -1
    # Stop when diffrence [P(j) - P(j-1)] is more than minimum
    while (Pj - Pj_1) > min_diff:
        Pk = Pj_1
        for k in xrange(j - 1, 0, -1):       
            diff = Pj - Pk
            if IsPentagonalNumber(diff) and \
                IsPentagonalNumber(Pj + Pk):
                if -1 == min_diff or \
                   min_diff > diff:
                    min_diff = diff
            if -1 != min_diff and \
                diff > min_diff:
                break
            Pk = GetPentagonalNumber(k)
        j += 1
        Pj_1 = Pj
        Pj = GetPentagonalNumber(j)
    return min_diff
        
# Main
def main():
    
    # 5482660
    print GetMinimumPentagonalDiffrence()
    
if __name__ == "__main__":
    main()
