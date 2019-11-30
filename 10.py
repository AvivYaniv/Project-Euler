N = 2000000

import math

def IsPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

# Main
def main():
    
    primes = [2]
    for n in range(3, N, 2):
        if IsPrime(n):
            primes.append(n)

    # 142913828922
    print sum(primes)
    
if __name__ == "__main__":
    main()
