DIGITS              = '0123456789'
PREMUTATION_NUMBER  = 1000000

import itertools

def GetNthPremutation(word, n):
    i = 0
    x = ''
    for p in itertools.permutations(word, len(word)):
        x = ''.join(p)
        i += 1
        if i == n:
            break
    return x

# Main
def main():
    # 2783915460
    print GetNthPremutation(DIGITS, PREMUTATION_NUMBER)
    
if __name__ == "__main__":
    main()
