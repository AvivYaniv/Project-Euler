import math

NUMBER_OF_PRIMES    =   10001

def IsPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

# Main
def main():
    c = 1
    n = 3
    p = n
    
    while c < NUMBER_OF_PRIMES:
        if IsPrime(n):
            p = n
            c = c + 1
        n = n + 2        
    
    # 104743
    print p

if __name__ == "__main__":
    main()
