
import math

LIMIT   =   1000

def IsInteger(f):
    return int(f) == f

def PellsEquationMinimalSolutionForX(D):
    sqrtD_float = math.sqrt(D)
    if IsInteger(sqrtD_float):        
        return (0, 0)
    sqrtD = int(sqrtD_float)    
    m = 0
    d = 1
    q = sqrtD 
    n_, d_ = 1, 0
    x, y = q, 1 
    while x*x - D*y*y != 1:
        m = d * q - m
        d = (D - m**2) / d
        q = (sqrtD + m) / d
        n_n, d_n = n_, d_       
        n_, d_ = x, y
        x, y = q*n_ + n_n, q*d_ + d_n
    return (x, y)

# Main
def main():

    maximal_x = 0
    D_for_maximal_x = 0

    for D in xrange(1, LIMIT + 1, 1):
        x, y = PellsEquationMinimalSolutionForX(D)
        if maximal_x < x:
            maximal_x = x
            D_for_maximal_x = D

    # 661
    print D_for_maximal_x
   
if __name__ == "__main__":
    main()
