
import math

LIMIT   =   10000

def GetReapeatingSequenceLength(n):
    m = 0
    d = 1
    a_0 = math.floor(math.sqrt(n))
    a_n = a_0
    seen = [a_0]
    last_added = 0
    for i in xrange(n):        
        m = d * a_n - m
        d = (n - m * m) / d
        if d == 0:
            last_added = 0
            break
        a_n =  math.floor((a_0 + m) / d)
        if a_n not in seen:
            seen.append(a_n)
            last_added = i + 1        
    return last_added

def GetOddPeriodSquareRoots(limit):
    counter = 0    
    for n in xrange(2, limit+1, 1):
        if 0 != GetReapeatingSequenceLength(n) % 2:
            counter += 1
    return counter

# Main
def main():

    # 1322
    print GetOddPeriodSquareRoots(LIMIT)
   
if __name__ == "__main__":
    main()

import math



