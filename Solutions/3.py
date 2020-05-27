import math

N       = 600851475143
N_SQRT  = math.sqrt(N)

def IsPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

# Main
def main():
    for i in range(int(N_SQRT), 3, -1):
        if IsPrime(i) and N % i == 0:
            # 6857
            print i
            break

if __name__ == "__main__":
    main()

