
LIMIT               = 10000 
MAX_SUM_ITERATIONS  = 50

UNKNOWN             = -1
NO                  = 0
YES                 = 1

def ReverseString(n):
    return str(n)[::-1]

def GetReverseNumber(n):
    return int(ReverseString(n))

def IsPalindrom(n):
    return str(n) == str(n)[::-1]

def GetLychrelNumbers(limit):    
    lychrel_numbers = []
    is_lychrel_number = [NO] + [UNKNOWN] * limit
    for n in xrange(1, limit, 1):
        if UNKNOWN == is_lychrel_number[n]:
            m = n
            checked = []
            is_lychrel = True
            for i in xrange(MAX_SUM_ITERATIONS+1):
                if m < limit:
                    checked.append(m)
                m += GetReverseNumber(m)
                if m < limit:
                    if UNKNOWN != is_lychrel_number[m]:                    
                        is_lychrel = is_lychrel_number[m] == YES
                        break
                if IsPalindrom(m):
                    is_lychrel = False
                    break
            is_lychrel_result = YES if is_lychrel else NO
            for c in checked:
                is_lychrel_number[c] = is_lychrel_result
                if is_lychrel:
                    lychrel_numbers.append(c)
    return lychrel_numbers        

# Main
def main():
    
    # 249
    print len(GetLychrelNumbers(LIMIT))
    
if __name__ == "__main__":
    main()
