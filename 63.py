
def GetDigitsNumber(n):
    return len(str(n))

def GetDigitsEqualPowerNumbers():
    counter = 0
    for a in xrange(1, 10, 1):
        for b in xrange(22):
            if GetDigitsNumber(a ** b) == b:
                counter += 1
    return counter

# Main
def main():
    
    # 49
    print GetDigitsEqualPowerNumbers()
    
if __name__ == "__main__":
    main()

import math
