
import math

def IsPrime(n):
    if n == 1:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

class HelixAntiClockwise:
    # Anticlockwise diagoals:
    # [n^2-2*(n-1)][n^2-3*(n-1)]
    # [n^2-1*(n-1)][n^2]
    def GetMatrixSizeDiagonalPrimesBelowPrecent(self, diagonal_precents):        
        n = 1
        diagonal_primes = 0
        while (n < 7) or diagonal_precents < (float(diagonal_primes) / (2*n - 1)):
            for m in xrange(1, 4, 1):
                if IsPrime(n**2 - m*(n-1)):
                    diagonal_primes += 1
            n += 2
        return n
        
# Main
def main():
    
    # 26241
    print str(HelixAntiClockwise().GetMatrixSizeDiagonalPrimesBelowPrecent(0.1)).replace(", [", "\n[")
    
if __name__ == "__main__":
    main()
